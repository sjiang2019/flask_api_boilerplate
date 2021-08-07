from flask import Blueprint, Flask
from flask_migrate import Migrate

from exts import db
from config import Config


def register_extensions(app):
    db.init_app(app)

    api = Blueprint('api', __name__, url_prefix='/api/1')

    from api.cars import cars
    api.register_blueprint(cars)

    app.register_blueprint(api)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    return app


app = create_app()
migrate = Migrate(app, db)


@app.route('/')
def hello():
    return {"hello": "world"}


if __name__ == '__main__':
    app.run(debug=True)


