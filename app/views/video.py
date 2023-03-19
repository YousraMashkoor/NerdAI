from flask import request
from flask_restful import Resource
from yt_dlp import YoutubeDL
import os
import whisper


def audio_to_script(path):
    '''
    uses wisper to convert mp3 file to text.
    '''
    model = whisper.load_model("tiny")
    result = model.transcribe(path)
    return (result["text"])

class ManageScript(Resource):

    # def post(self):
    #     account = Account(
    #         account_id = request.json['account_id'],
    #         status = request.json['status'],
    #         balance = request.json['balance']
    #     )
    #     db.session.add(account)
    #     db.session.commit()

    #     output = {
    #         'message': 'Account Created',
    #         'resource_id': account.account_id,
    #         'status': 200
    #     }

    #     return output


    def get(self):

        video_url = request.json['url']
        video_info = YoutubeDL().extract_info(url = video_url,download=False)
        filename = f"{video_info['title']}.mp3"
        options={
            'format':'worstaudio',
            'keepvideo':False,
            'outtmpl':filename,
        }

        with YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        print("Download complete... {}".format(filename))
        script = audio_to_script(filename)
        return {
            'message': 'Object rendered successfully.',
            'context': script,
            'status_code': 200
            }