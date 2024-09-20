from resources.fussballde_constants import *


def get_url(url: str, section_name: str) -> str:
    section_divider = SECTION_DIVIDER
    if not url.endswith('/'):
        section_divider = '/' + section_name

    url += section_divider + section_name

    if section_name == MATCH_PLAN_SECTION_NAME:
        return url.replace(MATCHES_URL_PREFIX, MATCH_PLAN_URL_PREFIX)
    if section_name == MATCHES_SECTION_NAME:
        return url.replace(MATCH_PLAN_URL_PREFIX, MATCHES_URL_PREFIX)
