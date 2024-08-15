from flask import Flask, jsonify
from fussballdescraper import get_teams, get_matches
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def format_url(url: str) -> str:
    url = 'https://www.fussball.de/' + url
    url = url.replace('SLASH', '/')
    return url + '#!/'


@app.route('/get-teams/<string:league_url>', methods=['GET'])
def request_teams(league_url: str):
    url = format_url(league_url)
    return jsonify(get_teams(url)), 201


if __name__ == '__main__':
    app.run(debug=True)
