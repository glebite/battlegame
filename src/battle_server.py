"""
battle_server.py
"""
import os
import logging
from flask import Flask, request, jsonify, Response
from game import *

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT, level=os.environ.get("LOGLEVEL", "DEBUG"))
LOG = logging.getLogger(__name__)

APP = Flask(__name__)
GAME_OBJ = None

@APP.route('/status', methods=["GET"])
def get_status():
    """
    get_status - returns the game status - once it's implemented
    """
    LOG.debug("GET /status")
    return jsonify(system_status="ok", game_status="")

@APP.route('/quitter', methods=["POST"])
def quitter():
    """
    quitter - shutsdown the werkzeug server
    """
    LOG.debug("POST /quitter")
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return jsonify(system_status="quitting", game_status="")

@APP.route('/player', methods=["GET", "POST", "DELETE"])
def player():
    """
    player - first Create (POST)
    """
    global GAME_OBJ
    if request.method == 'POST':
        LOG.debug("POST /player")
        if GAME_OBJ is None:
            return Response("Game not created.", status=404)
        else:
            GAME_OBJ.add_player(request.form['player_name'])
            return jsonify(status=201, game_status="")
    elif request.method == 'GET':
        LOG.debug("GET /player")
        LOG.debug("Players: {}".format(GAME_OBJ.return_players()))
        LOG.debug("All is good here...")
        return Response(jsonify(players=GAME_OBJ.return_players()), status=200)
    elif request.method == 'DELETE':
        LOG.debug("DEL /player")
        GAME_OBJ.players = list()
        return jsonify(status=201)

@APP.route('/player/fire', methods=["POST"])
def fire():
    """
    fire - fire a shot into the grid
    """
    global GAME_OBJ
    if request.method == 'POST':
        LOG.debug("POST /player/fire")
        return jsonify(status=201)
    else:
        LOG.debug("Received unexpected POST endpoint {}".format(request.method))
        return jsonify(status=503)
    
    
@APP.route('/game', methods=["GET", "POST"])
def game():
    """
    game
    """
    global GAME_OBJ
    if request.method == 'POST':
        LOG.debug("POST /game - starting a game")
        name = request.form['name']
        GAME_OBJ = Game(name)
        return jsonify(status="Coolio")
    elif request.method == 'GET':
        LOG.debug("GET /game - tell me more about the game...")
        return jsonify(status="And the gang")


if __name__ == "__main__":
    # If debug set to True allows for auto-reload on file changes
    APP.run(host='0.0.0.0', port=5150, debug=True)
