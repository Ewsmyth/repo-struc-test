from flask import Blueprint, render_template
import subprocess

auth = Blueprint('auth', __name__)

@auth.route('/')
def authLogin():
    return render_template('auth-login.html')

@auth.route('/api/update', methods=['POST'])
def update_container():
    # Minimal placeholder logic
    # In real systems you'd need shell access, sudo/systemd or Docker socket
    subprocess.run(["/usr/bin/docker", "pull", "ghcr.io/ewsmyth/repo-struc-test:latest"])
    subprocess.run(["/usr/bin/docker", "container", "restart", "repo-struc-test"])
    return "Update triggered!"
