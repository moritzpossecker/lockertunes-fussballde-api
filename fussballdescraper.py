from bs4 import BeautifulSoup
import requests
from models.match import Match
from resources.fussballde_constants import *


"""
Web-scraper for fussball.de
Should import get_teams and get_matches
"""


def get_url(url: str, section_name: str) -> str:
    section_divider = SECTION_DIVIDER
    if not url.endswith('/'):
        section_divider = '/' + section_name

    url += section_divider + section_name

    if section_name == MATCH_PLAN_SECTION_NAME:
        return url.replace(MATCHES_URL_PREFIX, MATCH_PLAN_URL_PREFIX)
    if section_name == MATCHES_SECTION_NAME:
        return url.replace(MATCH_PLAN_URL_PREFIX, MATCHES_URL_PREFIX)


def get_soup(url: str, section_name: str) -> BeautifulSoup:
    url = get_url(url, section_name)
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')


def get_team_names(league_url: str, section_name: str) -> list[str]:
    soup = get_soup(league_url, section_name)
    return soup.findAll('div', attrs={'class': TEAM_NAME_CLASS})


def get_team_logo(league_url: str, section_name: str) -> list[str]:
    soup = get_soup(league_url, section_name)
    return soup.findAll('div', attrs={'class': TEAM_LOGO_CLASS})


def get_match_plan_teams(league_url: str) -> list[dict[str, str]]:
    team_names = get_team_names(league_url, MATCH_PLAN_SECTION_NAME)
    team_logos = get_team_logo(league_url, MATCH_PLAN_SECTION_NAME)
    res = []
    for i in range(len(team_names)):
        res.append({
            'team_name': team_names[i],
            'team_logo': team_logos[i],
        })

    return res


def get_match_plan_results(league_url: str):
    soup = get_soup(league_url, MATCH_PLAN_SECTION_NAME)
    return soup.findAll('td', attrs={'class': MATCH_RESULT_CLASS})


def get_league_team_names(league_url: str) -> list[str]:
    return get_team_names(league_url, MATCHES_SECTION_NAME)


def format_team_name(team_name) -> str:
    team_name = team_name.text
    return team_name.strip(' \t\n\r')


def format_team_logo_src(team_logo) -> str:
    team_logo = team_logo.find('img').attrs['src']
    team_logo = team_logo.replace('getLogo/format/3/id', 'getLogo/format/2/id')
    team_logo = team_logo.replace('//', '')
    return team_logo


def get_matches(team_name: str, league_url: str, game_span: int) -> list[Match]:
    """
    Gets all matches related to a team

    Returns a list of all matches related to a team
    """
    matches = []
    teams = get_match_plan_teams(league_url)
    results = get_match_plan_results(league_url)

    j = 0

    codes = []
    for i in range(0, len(teams), 2):
        if len(matches) == game_span:
            break

        home_team = teams[i]
        away_team = teams[i + 1]

        home_team_name = format_team_name(home_team['team_name'])
        away_team_name = format_team_name(away_team['team_name'])

        if away_team_name != team_name and home_team_name != team_name:
            continue

        score_left = results[j].find('span', attrs={'class': 'score-left'})
        j += 1

        if score_left is None:
            continue

        encoding = 'shift_jis'
        score = score_left.get_text(strip=True).encode(encoding=encoding)

        decoded_string = score.decode(encoding=encoding)
        for char in decoded_string:
            print(f"&#{hex(ord(char))[1::]}")

        scoreString = ''
        for s in score:
            scoreString += str(s) + '/'
        codes.append(scoreString)

        if score_left.text == '2':
            continue

        home_team_logo = format_team_logo_src(home_team['team_logo'])
        away_team_logo = format_team_logo_src(away_team['team_logo'])

        if home_team_name == team_name:
            matches.append(Match(len(matches) + 1, home_team_name, home_team_logo,
                                 away_team_name, away_team_logo, True))

        if away_team_name == team_name:
            matches.append(Match(len(matches) + 1, away_team_name, away_team_logo,
                                 home_team_name, home_team_logo, False))

    codes = codes[1::]
    print(len(codes))
    final_codes_set = set(codes)
    print(len(final_codes_set))
    for code in final_codes_set:
        print(code)

    return matches


def get_teams(league_url: str) -> list[str]:
    """
    Gets all teams which are in a specific league

    Returns a list of all teams which are in a specific league
    """
    team_names = get_league_team_names(league_url)

    teams_set = set(team_names)

    formated_teams = []
    for team in teams_set:
        formated_teams.append(format_team_name(team))

    return formated_teams


if __name__ == '__main__':
    team_name = 'SG Taucha 99'
    url = 'https://www.fussball.de/spieltagsuebersicht/sachsenliga-sachsen-landesliga-sachsen-herren-saison2425-sachsen/-/staffel/02PNS2TBRC000003VS5489B3VSSIBR6U-G#!/'
    game_span = 10000

    matches = get_matches(team_name, url, game_span)

    print(len(matches))
    #for match in matches:
        #print(match)