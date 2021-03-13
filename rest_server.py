from flask import Flask
from flask import request

from lib.strip import Strip

app = Flask(__name__)

strip = Strip()

@app.route("/progress_fill", methods=['POST'])
def progress_fill():
    data = request.get_json(force=True)
    color = data.get('color')
    if color:
        strip.progressive_fill(color=color)
    else:
        strip.progressive_fill()
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

