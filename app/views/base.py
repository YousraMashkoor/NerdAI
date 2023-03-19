from flask import Blueprint

base_bp = Blueprint('base_bp', __name__)

@base_bp.route("/")
def home():
    return "App running on flask server" 
