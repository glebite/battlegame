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
            self.game_started = True
            return response
        except Exception as e:
            self.game_started = False
            print(e)
        return

    def create_player(self, player_name):
        """ create_player """
        if self.game_started:
            player_info = {'player_name': player_name}
            response = requests.post('http://127.0.0.1:5150/player', data=player_info)
        else:
            print("Nope! - can't create a game as the server isn't running...")
        return response
    
    def quit_game(self):
        """ quit_game """
        print("Executing quit_game...")
        if self.game_started:
            response = requests.post('http://127.0.0.1:5150/quitter')
        else:
            response = ""
        print("Bye!")
        return response

def play():
    """ play """
    client_obj = GameClient()
    while client_obj.state == NOT_DONE:
        command = input("command? ")
        print("command = {}".format(command))
        if command == "quit":
            client_obj.quit_game()
            return
        elif command == "create_player":
            player_name = input("Enter player name: ")
            client_obj.create_player(player_name)
        else:
            print("unknown command...")

if __name__ == "__main__":
    play()
