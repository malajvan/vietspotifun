import spotipy
import json
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from authenticate import authenticate
import util_help as uh


token=authenticate("eyyolk","user-library-read","409f2b568b5146298d8db0ff754ce726","c85512ab0ea94debae3c39f5adae1c44","https://www.facebook.com/hiiamvan")
def toke():
    return token
def get_user_playlists():
    '''
    ~get current user's playlists~
    -----
    parameters:
    return:
        --> list of dicts :[{name;id}]
    '''
    results=token.current_user_playlists()
    playlists=list()
    for i in results['items']:
        playlists.append({'name': i['name'],'id':i['id']})
    return playlists

def get_playlist_tracks(playlist_id):
    '''
    ~get all tracks from a playlist~
    ----
    parameters:
        * playlist_id: playlist's id
    return:
        --> list of dicts :[{name;id}]
    '''
    results= token.playlist_items(playlist_id,fields='items')
    tracks=list()
    uh.dump_dict_to_file('hi.json',results)
    for a in results['items']:
        i=a['track']
        artists=[]
        for ar in i['artists']:
            artists.append({'name':ar['name'],'id':ar['id']})
        tracks.append({'name': i['name'],'artists':artists,'id':i['id']})
    return tracks

def get_playlist_danceability(playlist_id):
    '''
    ~get average danceability of songs in the playlist~
    ----
    parameters:
        * id: album's id / artist's uri
    return:
        --> float
    '''
    tracks=get_playlist_tracks(playlist_id)

    track_info=list()
    danceability=0
    for song in tracks:
        track_info+=token.audio_features(song['id'])
    for song in track_info:
        danceability+= (song['danceability'])
    print(len(track_info))
    return (danceability/len(track_info))

def main():
    print(get_playlist_danceability('1oO49Ne3q4iwDAnN3RyoP1'))

if __name__ == '__main__':
    main()
