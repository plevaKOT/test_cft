from cv2 import error
from flask import *
from pixels import count_pixels

import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

logHandler = logging.FileHandler('default.json')
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", error=0)


@app.route("/get_colors", methods=['POST'])
def get_colors():
    img = request.files['photo'].read()
    hex = request.form['hex']

    counts = count_pixels(img, hex)
    if not counts:
        return render_template("index.html", error=1)
    else:
        return render_template("results.html", counts=counts, hex=hex)