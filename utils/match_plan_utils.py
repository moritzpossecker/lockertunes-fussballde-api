from utils.teams_utils import get_team_logo, get_team_names
from resources.fussballde_constants import *


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
