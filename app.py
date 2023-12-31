from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from db import db
from routes import blp as RoutesBlueprint
from views import blp as PagesBlueprint
from handlers import error_pages

def create_app():
    app = Flask(__name__)
    app.config["API_TITLE"] = "Dummy Api"
    app.config['SECRET_KEY'] = 'key'
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app,db)

    with app.app_context():
        db.create_all()

    api = Api(app)
    api.register_blueprint(RoutesBlueprint)
    api.register_blueprint(PagesBlueprint)
    api.register_blueprint(error_pages)

    return app





