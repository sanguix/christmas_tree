#!/usr/bin/env python3
from flask import Flask
from flask import request

from lib.strip import Strip

app = Flask(__name__)

strip = Strip()

def check_color(color):
    if not isinstance(color, list):
        raise TypeError(f'Color should be a list type variable')

    if len(color) != 3:
        raise ValueError(f'Color should be a list of 3 integer, not {color}')

    for item in color:
        print(type(item))
        print(item)
        if not isinstance(item, int):
            raise ValueError(f'Color should be a list of 3 integer, but {item} was found')

        if item < 0 or item > 255:
            raise ValueError(f'Color values should be between 0 and 255, but {item} was found')

@app.route("/monochrome", methods=['POST'])
def monochrome():
    data = request.get_json(force=True)
    color = data.get('color')
    try:
        check_color(color)
    except Exception as e:
        return str(e), 400

    if color:
        strip.monochrome(color=color)
    else:
        strip.monochrome()
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
