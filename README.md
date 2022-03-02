# vietspotifun
A Spotify API data exploration project to analyse music consumption trend of Vietnamese market.

## Background
I saw many such projects for predominantly English-speaking countries. As music streaming services, especially Spotify, become increasingly popular in Vietnam, I took it upon myself to answer some questions and debunk myths that has always surrounded the music scene, with the help of Spotify's web API and Python. 

## Methods
I used the Python library Spotipy to assist fetching data from Spotify. I also wrote some helper functions ([user_util.py](https://github.com/malajvan/vietspotifun/blob/main/user_util.py) and [artist_util.py](https://github.com/malajvan/vietspotifun/blob/main/artist_util.py)) to assist getting and compiling desirable data with pandas. For data visualization, I used matplotlib library to create graphs and plots to demonstrate my findings in [plottings.py](https://github.com/malajvan/vietspotifun/blob/main/plottings.py).

## Data
Collected Spotify Web API with [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/) with addition to some utility codes.

## Discussions
I concluded 3 main points:
1. It is not true that Vietnamese artists that I looked at prefer to write song in C major/A minor compared to other keys.
![key_stuff](https://user-images.githubusercontent.com/64571718/156438342-6a9e5cb9-f133-4a3f-99e7-7c66cb86b472.png)
2. My vietnamese personal playlist songs' features closely resemble that of the Hot Hits Vietnam playlist. 
![Figure_1](https://user-images.githubusercontent.com/64571718/156438220-2e97b5c2-7d5a-456c-81dd-bfe8295e4e72.png)

3. Hot Hits Vietnam playlist follow the same feature trend as the Hot Hits US, however, there is an interesting peak in acousticness in popular songs, meaning compared to its US/UK counterpart, Vietnamese audience enjoys acoustic music or acoustic elements in songs more. This align with my own impression of my peers' listening trend.
![hothitsusa](https://user-images.githubusercontent.com/64571718/156439085-8d9985fb-67e8-44c7-a050-4759ef3919fb.png)


It was really interesting to see how this plays out, all conclusions totally suprised me! You can download my code and change the artist ID or country plalist ID to mess around and discover your own country's trend or personal playlist trends. 

## Authors

Hong Van Pham :
[Email](mailto:vanhongpham01@gmail.com), [Linkedin](https://www.linkedin.com/in/vanhpham/), [Facebook](https://www.facebook.com/hiiamvan)


## Acknowledgments
I have taken inspirations as well as references from 
[Spotify Data Visualization and Analysis using Python](https://medium.com/geekculture/spotify-data-visualization-and-analysis-using-python-4af81c5531a7) by Rohit Kumar Thakur
