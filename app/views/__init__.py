from flask import Blueprint
from flask_restful import Api
from .video import ManageScript, ChatGPT, Summary, Quiz

script_bp = Blueprint('script_bp',__name__)
chat_bp = Blueprint('chat_bp',__name__)
summary_bp = Blueprint('summary_bp',__name__)
quiz_bp = Blueprint('quiz_bp',__name__)

script_api = Api(script_bp)
script_api.add_resource(ManageScript,'/script')

chat_api = Api(chat_bp)
chat_api.add_resource(ChatGPT,'/chat')

summary_api = Api(summary_bp)
summary_api.add_resource(Summary,'/summary')

quiz_api = Api(quiz_bp)
quiz_api.add_resource(Quiz,'/quiz')


from .base import base_bp