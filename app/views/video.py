from flask import request
from flask_restful import Resource
from yt_dlp import YoutubeDL
import os
import whisper
import openai

openai.api_key = os.environ.get('OPENAI_KEY')
model = "text-ada-001"


def audio_to_script(path):
    '''
    uses wisper to convert mp3 file to text.
    '''
    model = whisper.load_model("tiny")
    result = model.transcribe(path)
    return (result["text"])

class ManageScript(Resource):

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
    

class ChatGPT(Resource):

    def post(self):
        # Get the message from the POST request
        context = f'You are answering questions regarding a video who\'s transcript'\
                  f'is as follows: {request.json.get("context")}'
        
        messages =[{"role": "system", "content": context}]
        # Send the message to OpenAI's API and receive the response

        user_message = {"role": "user", "content": request.json.get("question")}
        messages.append(user_message)
        
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=140
        )
        if completion.choices[0].message!=None:
            return completion.choices[0].message

        else :
            return 'Failed to Generate response!'
    
class Summary(Resource):

    def get(self):

        context = f'Summarize a video who\'s transcript'\
                  f'is as following: {request.json.get("context")}'
        
        messages =[{"role": "system", "content": context}]

        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=140
        )

        if completion.choices[0].message!=None:
            return completion.choices[0].message

        else :
            return 'Failed to Generate response!'
        

class Quiz(Resource):

    def get(self):

        context = f'Generate three multiple choice question using the following'\
                  f'context: {request.json.get("context")}'
        
        messages =[{"role": "system", "content": context}]
        
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
        )
        if completion.choices[0].message!=None:
            return completion.choices[0].message

        else :
            return 'Failed to Generate response!'
