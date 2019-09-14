"""
battle_server.py
"""
from flask import Flask, request, jsonify

APP = Flask(__name__)

@APP.route('/status', methods=["GET"])
def get_status():
    """
    get_status - returns the game status - once it's implemented
    """
    return jsonify(system_status="ok", game_status="")

@APP.route('/quitter', methods=["POST"])
def quitter():
    """
    quitter - shutsdown the werkzeug server
    """
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return jsonify(system_status="quitting", game_status="")

@APP.route('/player', methods=["POST"])
def player():
    """
    player - first Create (POST)
    """
    return jsonify(status="Created", game_stsatus="")



if __name__ == "__main__":
    # If debug set to True allows for auto-reload on file changes
    APP.run(host='0.0.0.0', port=5150, debug=True)
