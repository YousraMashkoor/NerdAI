from flask import Blueprint
from flask_restful import Api
from .video import ManageScript

script_bp = Blueprint('script_bp',__name__)

script_api = Api(script_bp)
script_api.add_resource(ManageScript,'/script')


from .base import base_bp