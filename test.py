import spotipy
import json
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from authenticate import authenticate
import util_help as uh


token=authenticate("eyyolk","user-library-read","409f2b568b5146298d8db0ff754ce726","c85512ab0ea94debae3c39f5adae1c44","https://www.facebook.com/hiiamvan")
print(token.track("6GJi4nSZOiTOU2FhsgxWyH?si=d216500e2099447f")['popularity'])
