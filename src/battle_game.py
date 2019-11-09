"""
battle_game.py
"""
import os
import requests
import game
import grid
import player
import ship_piece
import battle_server

NOT_DONE = 0
DONE = 1

class GameClient:
    """ GameClient """
    def __init__(self):
        """ __init__ """
        self.state = NOT_DONE
        try:
            params = {'name': 'battle_server'}
            response = requests.post('127.0.0.1:5150/game', data=params)
        except Exception as e:
            print(e)
        return response

    def create_player(self, player_name):
        """ create_player """
        player_info = {'player_name': player_name}
        response = requests.post('http://127.0.0.1:5150/player', data=player_info)
        return response

    def quit_game(self):
        """ quit_game """
        response = requests.post('http://127.0.0.1:5150/quitter')
        return response

    def player_input(self):
        """ player_input """
        command = raw_input("Enter player command: ")
        if command == "quit":
            self.state = DONE
            self.quit_game()
        return command

def play():
    """ play """
    command = raw_input("Enter your name: ")
    print("name = {}".format(command))
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
    CLIENT_OBJ = GameClient()
    while CLIENT_OBJ.state is NOT_DONE:
        COMMAND_INPUT = CLIENT_OBJ.player_input()
        print("Executing command: {}".format(COMMAND_INPUT))
