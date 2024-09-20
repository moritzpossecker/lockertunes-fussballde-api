from flask import Flask, jsonify
from match_getter import get_matches
from teams_getter import get_teams
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def format_url(url: str) -> str:
    url = 'https://www.fussball.de/' + url
    url = url.replace('SLASH', '/')
    return url + '#!/'


def format_team_name(team_name: str) -> str:
    return team_name.replace('SPACE', ' ')


@app.route('/get-teams/<string:league_url>', methods=['GET'])
def request_teams(league_url: str):
    url = format_url(league_url)
    return jsonify(get_teams(url)), 201


@app.route('/get-matches/<string:team_name>/<string:league_url>/<int:game_span>', methods=['GET'])
def request_matches(team_name: str, league_url: str, game_span: int):
    team_name = format_team_name(team_name)
    league_url = format_url(league_url)
    matches_dict = []
    matches = get_matches(team_name, league_url, game_span)
    for match in matches:
        matches_dict.append(match.to_dict())

    return jsonify(matches_dict), 202


if __name__ == '__main__':
    app.run(debug=True)
