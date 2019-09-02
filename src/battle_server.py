"""
battle_server.py
"""
from flask import Flask, abort, request
from flask import jsonify
import sys

APP = Flask(__name__)

@APP.route('/status')
def get_status():
    """ get_status """
    return jsonify(
        system_status="ok",
        game_status=""
        )

@APP.route('/quitter', methods=["POST"])
def quitter():
    """
    quitter 
    """
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return jsonify(system_status="quitting", game_status="")
    
if __name__ == "__main__":
    """
    debug=True allows for auto-reload on file changes
    """
    APP.run(host='0.0.0.0', port=5150, debug=True)

