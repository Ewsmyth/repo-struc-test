from flask import Flask, jsonify
import requests

VERSION = "v1.0.0"

def create_app():
    app = Flask(__name__, static_folder='static')

    @app.route('/version')
    def version():
        return jsonify({'version': VERSION})

    @app.route('/api/latest-version/')
    def latestVersion():
        resp = requests.get("https://ghcr.io/v2/ewsmyth/repo-struc-test/tags/list")
        tags = resp.json().get("tags", [])
        tags.sort(reverse=True)
        return jsonify({"latest": tags[0] if tags else "unknown"})
    
    def getVersion():
        try:
            with open("/app/version.txt") as f:
                return f.read().strip()
        except:
            return "unknown"
    
    @app.route('/api/version')
    def currentVersion():
        return jsonify({"version": getVersion()})

    from .auth import auth

    app.register_blueprint(auth)

    return app