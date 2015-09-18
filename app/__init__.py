from flask import Flask
import config
import logging

app = Flask(__name__)
app.config.from_object(config)
stream_handler = logging.StreamHandler()
app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('cat in a hat startup')

from app import views