from flask import Flask # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_migrate import Migrate # type: ignore
from .config import Config
from flask_cors import CORS

db = SQLAlchemy()

def create_app(): 
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from . import routes
        db.create_all()

    return app
