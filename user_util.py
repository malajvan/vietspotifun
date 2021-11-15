import spotipy
import json
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from authenticate import authenticate
import util_help as uh


token=authenticate("eyyolk","user-library-read","409f2b568b5146298d8db0ff754ce726","c85512ab0ea94debae3c39f5adae1c44","https://www.facebook.com/hiiamvan")

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

def main():
    print()
    uh.dump_dict_to_file('ih.json',get_playlist_tracks('4Bn45usEjhVURzkuIlg61s'))

if __name__ == '__main__':
    main()