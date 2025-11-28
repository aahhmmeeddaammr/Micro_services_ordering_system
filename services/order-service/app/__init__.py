from flask import Flask
from dotenv import load_dotenv
from .config.config import configure_app

def create_app():
    load_dotenv()
    app = Flask(__name__)
    configure_app(app)

    from .routes.routes import register_routes
    register_routes(app)

    return app