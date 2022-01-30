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
    #print(url)
    return response

@app.route("/spotify-callback", methods=['GET'])
def spotify_callback(): 
    args = request.args
    code = args['code']

    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code', 
        'code': code,
        'redirect_uri': SPOTIPY_REDIRECT_URI,
        'client_id': SPOTIPY_CLIENT_ID, 
        'client_secret': SPOTIPY_CLIENT_SECRET
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    err = response.get('error')
    print(access_token, token_type, refresh_token, expires_in, err)
    return {}

api.add_resource(TemplateHandler, '/flask/hello')