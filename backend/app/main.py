from flask import Flask
from flask_cors import CORS
import logging
import sys


# https://stackoverflow.com/questions/26578733/why-is-flask-application-not-creating-any-logs-when-hosted-by-gunicorn


# stream handler needed to get logging to write to standard output so we can see it in Docker logs (if we aren't using Gunicorn)
# logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.INFO, handlers=[logging.StreamHandler(stream=sys.stdout)])
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.INFO)
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    logger = logging.getLogger()
    logger.info("Hitting the hello world")
    return {'message': 'Hello, world'}