from soup_utils import get_soup
from resources.fussballde_constants import *


def get_team_names(league_url: str, section_name: str) -> list[str]:
    soup = get_soup(league_url, section_name)
    return soup.findAll('div', attrs={'class': TEAM_NAME_CLASS})


def get_team_logo(league_url: str, section_name: str) -> list[str]:
    soup = get_soup(league_url, section_name)
    return soup.findAll('div', attrs={'class': TEAM_LOGO_CLASS})


def format_team_name(team_name) -> str:
    team_name = team_name.text
    return team_name.strip(' \t\n\r')


def format_team_logo_src(team_logo) -> str:
    team_logo = team_logo.find('img').attrs['src']
    team_logo = team_logo.replace('getLogo/format/3/id', 'getLogo/format/2/id')
    team_logo = team_logo.replace('//', '')
    return team_logo
