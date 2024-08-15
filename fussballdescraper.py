from bs4 import BeautifulSoup
import requests
from models.match import Match
from resources.fussballde_constants import *


"""
Web-scraper for fussball.de
Should import get_teams and get_matches
"""


def get_soup(url: str, section_name: str) -> BeautifulSoup:
    section_divider = SECTION_DIVIDER
    if not url.endswith('/'):
        section_divider = '/' + section_name

    url += section_divider + section_name

    if section_name == MATCH_PLAN_SECTION_NAME:
        url = url.replace(MATCHES_URL_PREFIX, MATCH_PLAN_URL_PREFIX)
    elif section_name == MATCHES_SECTION_NAME:
        url = url.replace(MATCH_PLAN_URL_PREFIX, MATCHES_URL_PREFIX)

    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')


def get_team_names(league_url: str, section_name: str) -> list[str]:
    soup = get_soup(league_url, section_name)
    return soup.findAll('div', attrs={'class': TEAM_NAME_CLASS})


def get_match_plan_team_names(league_url: str) -> list[str]:
    return get_team_names(league_url, MATCH_PLAN_SECTION_NAME)


def get_league_team_names(league_url: str) -> list[str]:
    return get_team_names(league_url, MATCHES_SECTION_NAME)


def format_team_name(team_name) -> str:
    team_name = team_name.text
    return team_name.strip(' \t\n\r')


def get_matches(team_name: str, league_url: str) -> list[Match]:
    """
    Gets all matches related to a team

    Returns a list of all matches related to a team
    """
    matches = []
    team_names = get_match_plan_team_names(league_url)

    for i in range(0, len(team_names), 2):
        home_team = format_team_name(team_names[i])
        away_team = format_team_name(team_names[i + 1])

        if home_team == team_name or away_team == team_name:
            matches.append(Match(len(matches) + 1, home_team, away_team))

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
