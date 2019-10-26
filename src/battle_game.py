"""
battle_game.py
"""
import game
import grid
import player
import ship_piece
import battle_server
import requests
import os

class GameClient:
    def __init__(self):
        try:
            params = {'name': 'battle_server'}
            response = requests.post('127.0.0.1:5150/game', data=params)
        except Exception as e:
            print(e)
        requests.post('http://127.0.0.1:5150/quitter')

def play():
    command = raw_input("Enter your name: ")
    # params = {'name': 'battle_server'}
    # response = requests.post('http://127.0.0.1:5150/game', data=params)
    # if response.status_code is not 200:
    #     print("Problem with starting game...")
    # player_name = {'player_name': 'MacArthur'}
    # response = requests.post('http://127.0.0.1:5150/player', data=player_name)
    # if response.status_code is not 200:
    #     print("Problem with creating player")
    # response = requests.post('http://127.0.0.1:5150/player/fire')
    # if response.status_code is not 201:
    #     print("Problem firing a shot")
    # requests.post('http://127.0.0.1:5150/quitter')

    
if __name__ == "__main__":
    client_obj = GameClient()
