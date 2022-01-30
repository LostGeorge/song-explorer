from flask import Flask, send_from_directory, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from backend.TemplateHandler import TemplateHandler
from requests import Request, post 
from backend.auth import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
import json 

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

@app.route("/get-auth-url", methods=['GET'])
def auth(): 
    scopes = 'playlist-read-private'
    url = Request('GET', 'https://accounts.spotify.com/authorize', params={
        'scope': scopes, 
        'response_type': 'code', 
        'redirect_uri': SPOTIPY_REDIRECT_URI, 
        'client_id': SPOTIPY_CLIENT_ID
    }).prepare().url

    response = app.response_class(
        response=json.dumps({'url': url}), 
        status=200, 
        mimetype='application/json'
    )
    print(url)
    return response

@app.route("/spotify-callback", methods=['GET'])
def spotify_callback(): 
    args = request.args
    print("HELLO")
    return {}

api.add_resource(TemplateHandler, '/flask/hello')