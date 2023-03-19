

import flask
import os
import enum
from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    from .views import base_bp, script_bp
    
    app.register_blueprint(base_bp, url_prefix='/')
    app.register_blueprint(script_bp)


    return app