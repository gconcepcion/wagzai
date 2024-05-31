from flask import Flask
from flask_migrate import Migrate

from wagzai.chat import chat_blueprint
from wagzai.config import Config
from wagzai.extensions import db, login_manager, ma
from wagzai.views import app_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)  # Initialize login manager
    # Register blueprint for the routes
    app.register_blueprint(app_blueprint)
    app.register_blueprint(chat_blueprint)  # Register the new chat blueprint

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=False)
