import os

from celery import Celery
from flask import Flask

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = os.getenv("CELERY_BROKER_URL")
app.config['RESULT_BACKEND'] = os.getenv("RESULT_BACKEND")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

celery = Celery(app.import_name,
                backend=app.config['RESULT_BACKEND'], broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
