import unittest

from main import app # Flask instance of the API


def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 404
 
def test_get_teams_route():
    response = app.test_client().get('/get-teams/fghrt')

    assert response.status_code == 201
    assert response.data.decode('utf-8') == '[]\n'

def test_get_matches_route():
    response = app.test_client().get('/get-matches/hhh/hh/5')

    assert response.status_code == 202
    assert response.data.decode('utf-8') == '[]\n'
