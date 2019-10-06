"""
test_server.py

All tests will be in @pytest markup format.

test_status
...
test_last
"""
import pytest
import requests
import subprocess
import time 

@pytest.mark.test_id(0)
def test_start_server():
    subprocess.Popen(['./launch_server.sh'], shell=True)
    time.sleep(10)
    assert True

@pytest.mark.test_id(2)
def test_status():
    """ test_status
    Confirms that the running server will return a 200 status_code
    when a get is performed on it.
    """
    response = requests.get('http://127.0.0.1:5150/status')
    assert response.status_code == 200

@pytest.mark.test_id(4)
def test_create_player():
    """ test_create_player
    Creates a player - no game created
    """
    response = requests.post('http://127.0.0.1:5150/player')
    assert response.status_code == 404

@pytest.mark.test_id(5)
def test_retrieve_player_list():
    """ test_retrieve_player_list
    Get player list - stubbed at first 
    """
    response = requests.get('http://127.0.0.1:5150/player')
    assert response.status_code == 500

@pytest.mark.test_id(6)
def test_create_game():
    """ test_create_game
    Creates a game - stubbed at first 
    """
    params = {'name': 'amazing...'}
    response = requests.post('http://127.0.0.1:5150/game', data=params)
    assert response.status_code == 200
    requests.delete('http://127.0.0.1:5150/player')

@pytest.mark.test_id(7)
def test_retrieve_game_status():
    """ test_retrieve_game_list
    Get game list - stubbed at first 
    """
    response = requests.get('http://127.0.0.1:5150/game')
    assert response.status_code == 200

@pytest.mark.test_id(8)
def test_create_game_then_player():
    """ test_create_player
    Creates a player - stubbed at first 
    """
    params = {'name': 'amazing...'}    
    response = requests.post('http://127.0.0.1:5150/game', data=params)
    assert response.status_code == 200
    player_name = {'player_name': 'kinky'}
    response = requests.post('http://127.0.0.1:5150/player', data=player_name)
    assert response.status_code == 200
    requests.delete('http://127.0.0.1:5150/player')

@pytest.mark.test_id(9)
def test_create_game_then_two_player():
    """ test_create_player
    Creates two players - stubbed at first 
    """
    params = {'name': 'amazing...'}    
    response = requests.post('http://127.0.0.1:5150/game', data=params)
    assert response.status_code == 200
    player_name = {'player_name': 'kinky'}
    response = requests.post('http://127.0.0.1:5150/player', data=player_name)
    player_name = {'player_name': 'boots'}
    response = requests.post('http://127.0.0.1:5150/player', data=player_name)
    assert response.status_code == 200

@pytest.mark.test_id(10)
def test_create_game_then_three_players():
    """ test_create_player
    Creates three players - stubbed at first 
    """
    params = {'name': 'amazing...'}    
    response = requests.post('http://127.0.0.1:5150/game', data=params)
    assert response.status_code == 200
    player_name = {'player_name': 'kinky'}
    response = requests.post('http://127.0.0.1:5150/player', data=player_name)
    assert response.status_code == 200    
    player_name = {'player_name': 'boots'}
    response = requests.post('http://127.0.0.1:5150/player', data=player_name)
    assert response.status_code == 200    
    player_name = {'player_name': 'caligula'}
    response = requests.post('http://127.0.0.1:5150/player', data=player_name)    
    assert response.status_code == 500

@pytest.mark.test_id(11)
def test_get_list_of_players():
    """ test_get_list_of_players
    Creates three players - stubbed at first 
    """
    player_list = requests.get('http://127.0.0.1:5150/player')
    print(player_list)
    
@pytest.mark.test_id(9999)
def test_quitter():
    """
    """
    response = requests.post('http://127.0.0.1:5150/quitter')
    assert response.status_code == 200
    
@pytest.mark.test_id(10000)
def test_last():
    """ test_last """
    assert True
