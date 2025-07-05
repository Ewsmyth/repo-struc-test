from flask import Flask
import os

def create_app():
    app = Flask(__name__, static_folder='static')

    version = os.environ.get("VERSION", "unknown")

    @app.route("/version")
    def versionRoute():
        return f"Version: {version}", 200

    from .auth import auth

    app.register_blueprint(auth)

    return app