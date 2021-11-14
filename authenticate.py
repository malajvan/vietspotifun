import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

def authenticate(username, scope,client_id,client_secret,redirect_uri):

    sp = spotipy.Spotify(SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    if token:
        sp = spotipy.Spotify(auth=token)
    else:
        print("Can't get token for", username)
    return sp
