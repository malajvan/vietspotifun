import matplotlib.pyplot as plt
import artist_util as util
import user_util as ut
import pandas as pd
import numpy as np
import spotipy
import json
import networkx as nx


def keys(artist_uri): #return bar graph of keycount of artist
    a=(util.get_artist_keys(artist_uri))
    df=pd.json_normalize(a)
    keys=list(df.columns)
    count=list(df.values)[0]
    plt.bar(keys,count)
    plt.show()

def key_trend():
    keys=dict()
    keys['ngot']=util.get_artist_keys("0V2DfUrZvBuUReS1LFo5ZI")
    keys['vtv']=util.get_artist_keys("5ptgjFDE2abY6Xwo4ytufN")
    keys['chh']=util.get_artist_keys("2j3AXmye1FJXoGOXr6tufj")
    keys['vu.']=util.get_artist_keys("57g2v7gJZepcwsuwssIfZs")

    dfs = []
    for file in keys:
        json_data = pd.json_normalize(keys[file])
        json_data['artist']=file
        dfs.append(json_data)
    df = pd.concat(dfs, sort=False).set_index("artist")
    cols=df.columns
    df[cols]=df[cols].div(df[cols].sum(axis=1), axis=0).multiply(100)
    df=df.T
    print(df)
    df.plot.bar()
    plt.show()


def popularity_map():
    def mapin(artist_id):
        df=pd.DataFrame.from_dict(util.albums_popu(artist_id)).T
        df['release_date']=pd.to_datetime(df['release_date'],format='%Y-%m-%d')
        #df.set_index(['release_date'],inplace=True)
        return df
    df=mapin("5ptgjFDE2abY6Xwo4ytufN")
    df.plot(x='release_date',y='popularity')
    df2=mapin("2j3AXmye1FJXoGOXr6tufj")
    df2.plot(x='release_date',y='popularity')
    plt.show()


def audio_features_map():
    def get_audio_feature(playlist_id):
        a=(ut.get_playlist_tracks(playlist_id))
        df=pd.json_normalize(a)
        ids=df['id'].tolist()
        features=ut.toke().audio_features(ids)
        df=pd.json_normalize(features)
        df2=df.drop(columns=['key','type','id','uri','loudness','track_href','analysis_url','mode','time_signature','tempo','duration_ms'])
        return df2
    a=get_audio_feature("5i13ZgtKHMrqFpsQSCfV6v")
    labels=list(a)
    playlist_fea=a.mean().tolist()
    hothits_vietnam=get_audio_feature("37i9dQZF1DX0F4i7Q9pshJ").mean().tolist()


    label_loc = np.linspace(start=0, stop=2*np.pi, num=len(labels), endpoint=False)
    fig = plt.figure(figsize = (10,10))

    ax = fig.add_subplot( polar=True)
    ax.plot(label_loc, playlist_fea, 'o-', linewidth=2, label = "My playlist", color= 'blue')
    ax.fill(label_loc, playlist_fea, alpha=0.5,facecolor='blue')
    ax.set_thetagrids(label_loc * 180/np.pi, labels , fontsize = 13)


    plt.yticks([0.1 , 0.2 , 0.3 , 0.4, 0.5,  0.6, 0.7], ["0.1",'0.2', "0.3", "0.4", "0.5", "0.6", "0.7"], size=12)

    ax.plot(label_loc, hothits_vietnam, 'o-', linewidth=2, label = "Hot Hits Vietnam", color= 'pink')
    ax.fill(label_loc, hothits_vietnam, alpha=0.5, facecolor='pink')
    ax.grid(True)
    plt.legend()

    plt.show()



def main():
    audio_features_map()



if __name__ == '__main__':
    main()
