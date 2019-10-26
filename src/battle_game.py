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

NOT_DONE = 0
DONE = 1

class GameClient:
    def __init__(self):
        self.state = NOT_DONE
        try:
            params = {'name': 'battle_server'}
            response = requests.post('127.0.0.1:5150/game', data=params)
        except Exception as e:
            print(e)

    def quit_game(self):
        response = requests.post('http://127.0.0.1:5150/quitter')
        return
    
    def player_input(self):
        command = raw_input("Enter player command: ")
        if command == "quit":
            self.state = DONE
            self.quit_game()
        return command

    
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
    while client_obj.state is NOT_DONE:
        command = client_obj.player_input()
        print("Executing command: {}".format(command))
