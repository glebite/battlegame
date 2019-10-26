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

def play():
    params = {'name': 'battle_server'}
    response = requests.post('http://127.0.0.1:5150/game', data=params)
    if response.status_code is not 200:
        print("Problem with starting game...")
        os.exit(1)
    player_name = {'player_name': 'MacArthur'}
    response = requests.post('http://127.0.0.1:5150/player', data=player_name)

    requests.post('http://127.0.0.1:5150/quitter')

    
if __name__ == "__main__":
    play()
