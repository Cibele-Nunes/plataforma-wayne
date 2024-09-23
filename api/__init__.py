from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:secret@localhost/wayne_login'

login_manager = LoginManager(app)
db = SQLAlchemy(app)

