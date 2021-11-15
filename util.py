import spotipy
import json,re
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from authenticate import authenticate
import util_help as uh


token=authenticate("eyyolk","user-library-read","409f2b568b5146298d8db0ff754ce726","c85512ab0ea94debae3c39f5adae1c44","https://www.facebook.com/hiiamvan")

ngot = '57g2v7gJZepcwsuwssIfZs'



def get_albums(artist_uri,type=None):
    '''
    ~get an artist's albums depends on album_type (singles, albums,...)~
    -----
    parameters:
        * artist_uri: artist's uri
        * type: type of album (‘album’, ‘single’, ‘appears_on’, ‘compilation’)
    return:
        --> list of dicts :[{name;id}]
    '''
    results = token.artist_albums(artist_uri, album_type=type)
    albums=list()
    for i in results['items']:
        albums.append({'name': i['name'],'id':i['id']})

    return albums


def get_tracks(album_id):
    '''
    ~get all tracks from an album ~
    ----
    parameters:
        * album_id: album's id
    return:
        --> list of dicts :[{name;id}]
    '''
    results= token.album_tracks(album_id)
    tracks=list()
    for i in results['items']:
        tracks.append({'name': i['name'],'id':i['id']})
    return tracks


def get_artist_tracks(artist_uri):
    '''
    ~get all tracks of an artists~
    ----
    parameters:
        * album_id: album's id
    return:
        --> list of dicts :[{name;id}]
    '''
    tracks=list()
    albums=get_albums(artist_uri)
    for i in albums:
        tracks+= get_tracks(i['id'])

    #remove possible duplicates
    done = set()
    result = []
    for d in tracks:
        if d['name'] not in done:
            done.add(d['name'])
            result.append(d)
    return result


def get_artist_keys(artist_uri):
    '''
    ~get key count for each artist~
    ----
    parameters:
        * artist_uri: artist's uri
    return:
        --> dict :{key:count}
    '''
    tracks=get_artist_tracks(artist_uri)
    track_info=list()
    key_count=dict()
    for song in tracks:
        track_info+=token.audio_features(song['id'])
    for song in track_info:
        a=str(song['key'])+' '+str(song['mode'])
        if a not in key_count:
            key_count[a]=1
        else:
            key_count[a]+=1
    pitch_notation=['C','Db','D','Eb','E','F','F#','G','Ab','A','Bb','B'] #see more on https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-audio-features
    mode_notation=['minor','major']
    result=dict() #rename key name and major minor
    for i in key_count:
        p=i.split()
        result[pitch_notation[int(p[0])]+"-"+mode_notation[int(p[1])]]=key_count[i]

    return result


def main():
    ngot



if __name__ == '__main__':
    main()