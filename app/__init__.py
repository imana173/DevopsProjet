from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialisation des extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialisation
    db.init_app(app)
    migrate.init_app(app, db)

    # Enregistrement du Blueprint
    from .routes import api
    app.register_blueprint(api, url_prefix='/api')

    return app


