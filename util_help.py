import sys,json
import spotipy
import spotipy.util as util

def dump_dict_to_file(file,dict):
    with open(file,'w+') as f:
        f.write(json.dumps(dict,indent=4))
