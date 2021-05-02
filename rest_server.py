#!/usr/bin/env python3
from flask import Flask
from flask import request

from lib.strip import Strip

app = Flask(__name__)

strip = Strip()

@app.route("/progress_fill", methods=['POST'])
def progress_fill():
    data = request.get_json(force=True)
    color = hexa_to_rgb(data.get('color'))
    strip.progressive_fill(color=color)
    return "OK"


@app.route("/off", methods=['POST'])
def turn_off():
    strip.turn_off()
    return "OK"


@app.route("/go_and_back", methods=['POST'])
def go_and_back():
    data = request.get_json(force=True)
    color = hexa_to_rgb(data.get('color'))
    strip.go_and_back(color=color, times=3)
    return "OK"


def hexa_to_rgb(hex_color):
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

