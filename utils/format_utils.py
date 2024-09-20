def format_url(url: str) -> str:
    url = 'https://www.fussball.de/' + url
    url = url.replace('SLASH', '/')
    return url + '#!/'


def format_team_name(team_name: str) -> str:
    return team_name.replace('SPACE', ' ')
