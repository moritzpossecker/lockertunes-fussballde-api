from utils.teams_utils import *


def get_teams(league_url: str) -> list[str]:
    """
    Gets all teams which are in a specific league

    Returns a list of all teams which are in a specific league
    """
    team_names = get_team_names(league_url, MATCHES_SECTION_NAME)

    teams_set = set(team_names)

    formated_teams = []
    for team in teams_set:
        formated_teams.append(format_team_name(team))

    return formated_teams
