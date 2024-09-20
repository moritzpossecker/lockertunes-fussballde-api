from models.match import Match
from utils.match_plan_utils import get_match_plan_teams
from utils.teams_utils import format_team_name, format_team_logo_src


def get_matches(team_name: str, league_url: str, game_span: int) -> list[Match]:
    """
    Gets all matches related to a team

    Returns a list of all matches related to a team
    """
    matches = []
    teams = get_match_plan_teams(league_url)

    for i in range(0, len(teams), 2):
        if len(matches) == game_span:
            break

        home_team = teams[i]
        away_team = teams[i + 1]

        home_team_name = format_team_name(home_team['team_name'])
        away_team_name = format_team_name(away_team['team_name'])

        if away_team_name != team_name and home_team_name != team_name:
            continue

        home_team_logo = format_team_logo_src(home_team['team_logo'])
        away_team_logo = format_team_logo_src(away_team['team_logo'])

        if home_team_name == team_name:
            matches.append(Match(len(matches) + 1, home_team_name, home_team_logo,
                                 away_team_name, away_team_logo, True))

        if away_team_name == team_name:
            matches.append(Match(len(matches) + 1, away_team_name, away_team_logo,
                                 home_team_name, home_team_logo, False))

    return matches
