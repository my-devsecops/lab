from flask import Flask
import traceback
import logging
app = Flask(__name__)


def do_computation():
    raise Exception("Secret info")


# BAD
@app.route('/bad')
def server_bad():
    try:
        do_computation()
    except Exception as e:
        return traceback.format_exc()


# GOOD
@app.route('/good')
def server_good():
    try:
        do_computation()
    except Exception as e:
        logging.warning(traceback.format_exc())
        return "An internal error has occurred!"