import unittest

from main import app # Flask instance of the API


def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 404
 
def test_get_teams_no():
    response = app.test_client().get('/get-teams/fghrt')

    assert response.status_code == 201
    assert response.data.decode('utf-8') == '[]\n'

def test_get_teams_route():
    response = app.test_client().get(
        '/get-teams/spieltagsuebersichtSLASHnofv-oberliga-sued-deutschland'\
        '-oberliga-herren-saison2425-deutschlandSLASH-SLASHstaffelSLASH'\
        '02PUNGDIE800000AVS5489B4VVTKJJ35-G#!')

    assert response.status_code == 201
    assert response.data.decode('utf-8').split(",").sort() == [
        "BSG Wismut Gera","1. FC Magdeburg II","VfL Halle 96","FC Grimma",
        "FC Einheit Rudolstadt","VfB Germania Halberstadt",
        "Bischofswerdaer FV 08","Ludwigsfelder FC","FSV Budissa Bautzen",
        "SC Freital","SV Blau-Weiß Zorbau","SG Union Sandersdorf",
        "FC Einheit Wernigerode","VfB 1921 Krieschow","RSV Eintracht 1949",
        "VfB Auerbach"].sort()
    assert len(response.data.decode('utf-8').split(",")) == 16
    

def test_get_matches_no():
    response = app.test_client().get('/get-matches/hhh/hh/5')

    assert response.status_code == 202
    assert response.data.decode('utf-8') == '[]\n'

def test_get_matches_route():
    response = app.test_client().get(
        '/get-matches/spieltagsuebersichtSLASHnofv-oberliga-sued-deutschland'\
        '-oberliga-herren-saison2425-deutschlandSLASH-SLASHstaffelSLASH'\
        '02PUNGDIE800000AVS5489B4VVTKJJ35/FCSPACEGrimma/12')

    assert response.status_code == 202
    assert response.data.decode('utf-8') == '[]\n'
