import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate


app = Flask(__name__)

app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ctc:ctc@localhost/blogtest'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#>>>>>>> 902aa4cf1883adb4c5ceffe0c770034f0e094c61

db = SQLAlchemy(app)
#db.app = app
#db.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)

if not app.debug:
	import logging
	from logging.handlers import RotatingFileHandler
	file_handler = RotatingFileHandler('tmp/blogtest.log', 'a', 1 * 1024 * 1024, 10)
	file_handler.setLevel(logging.INFO)
	file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	app.logger.addHandler(file_handler)
	app.logger.setLevel(logging.INFO)
	app.logger.info('blogtest startup')
	
from app import models
from app import views
#>>>>>>> 902aa4cf1883adb4c5ceffe0c770034f0e094c61
