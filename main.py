from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import openai
import hjson

app = Flask(__name__)
api = Api(app)
CORS(app)

class OpenAi(Resource):
    def get(self):
        ask = request.args.get('ask') 

        openai.api_key = os.getenv("OPENAI_API_KEY")

        response = openai.Completion.create(
          model="code-davinci-002",
          prompt=ask,
          temperature=0,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )

        hjson.dump(response, open("response.json", "w"))

        res=response['choices'][0]['text']

        return res 

    def post(self):
        return "hi"

    def delete(self):
        return "hi"

    def put(self):
        return "hi"

    def patch(self):
        return "hi"

    
api.add_resource(OpenAi, '/') # Route_1




if __name__ == '__main__':
     app.run(port='5002')