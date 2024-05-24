from flask_babel import Babel
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Create the login manager instance
login_manager = LoginManager()

# Create the SQLAlchemy instance
db = SQLAlchemy()

# Create the Babel instance
babel = Babel()
