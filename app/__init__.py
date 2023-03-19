

import flask
import os
import enum
from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    from .views import base_bp, script_bp, chat_bp, summary_bp, quiz_bp
    
    app.register_blueprint(base_bp, url_prefix='/')
    app.register_blueprint(script_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(summary_bp)
    app.register_blueprint(quiz_bp)



    return app