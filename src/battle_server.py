"""
battle_server.py
"""
from flask import Flask
from flask import jsonify

APP = Flask(__name__)

@APP.route('/status')
def get_status():
    """ get_status """
    return jsonify(
        system_status="ok",
        game_status=""
        )

if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=5150)
