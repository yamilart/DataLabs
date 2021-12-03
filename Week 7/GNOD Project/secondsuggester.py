#!/usr/bin/env python
# coding: utf-8

# # GNOD Song Suggester

# ## Web Scraping Hot 100 from Billboard

#  Scraping the current top 100 songs and their respective artists from https://www.billboard.com/charts/hot-100, and putting the information into a pandas dataframe.

# In[1]:


# importing libraries

from bs4 import BeautifulSoup
import re 
import requests
import pandas as pd
from tqdm.notebook import tqdm
import random
from random import randint
import warnings
warnings.filterwarnings("ignore")


# ### Getting the info from the web

# In[2]:


# storing link in a variable
url = "https://www.billboard.com/charts/hot-100"
# downloading  html with a get request
response = requests.get(url)
# check response status code 
response.status_code


# In[3]:


# parsing and storing the contents of the url call
billboardsoup = BeautifulSoup(response.content, 'html.parser')


# In[4]:


# looping the songs
top_100 = len(billboardsoup.select('h3.c-title.a-no-trucate'))
song = []
artist = []

for i in tqdm(range(top_100)):
    song.append(billboardsoup.select('h3.c-title.a-no-trucate')[i].get_text(strip=True))
    artist.append(billboardsoup.select('span.c-label.a-font-primary-s')[i].get_text(strip=True))


# ### Getting the dataframe and storing it

# In[5]:


billboard_top100 = pd.DataFrame({'song':song,'artist':artist})


# ## Spotipy (API Wrappers)

# In[6]:


# more libraries, you can never have enough

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import getpass
import pprint


# In[7]:


client_id = str(getpass.getpass('client_id: '))
client_secret = str(getpass.getpass('client_secret: '))
# embedding getpass credentials in the access key
sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret))


# ### Choosing some playlist to create a dataframe

# ### Supernatural soundtrack

# In[8]:


first_playlist = sp.user_playlist_tracks("solitude collective", "1IEQ8C3G1qT0W80muYgROT")


# In[9]:


def get_tracks(user_id, playlist_id):
    results = sp.user_playlist_tracks(user_id, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
first_results = get_tracks("solitude collective", "1IEQ8C3G1qT0W80muYgROT")


# In[10]:


song_name = []
song_uri = []
song_id = []
song_artists = []
playlist = first_results
for r in first_results:
    song_name.append(r['track']['name'])
    song_uri.append(r['track']['uri'])
    song_id.append(r['track']['id'])
    song_artists.append(r['track']['artists'][0]['name'])
playlist_info = pd.DataFrame({'song_name':song_name, 'song_id':song_id, 'artist':song_artists})


# In[11]:


features_info = pd.DataFrame(sp.audio_features(tracks = song_id[0:99]))
features_info2 = pd.DataFrame(sp.audio_features(tracks = song_id[99:199]))
features_info3 = pd.DataFrame(sp.audio_features(tracks = song_id[199:299]))
features_info4 = pd.DataFrame(sp.audio_features(tracks = song_id[299:399]))
features_info5 = pd.DataFrame(sp.audio_features(tracks = song_id[399:]))
features = pd.concat([features_info, features_info2, features_info3, features_info4, features_info5])
features.reset_index(drop=True, inplace=True)


# In[12]:


first_playlist = pd.concat([playlist_info, features], axis=1)
first_playlist.reset_index()


# ### All out 80s

# In[13]:


second_playlist = sp.user_playlist_tracks("Spotify", "37i9dQZF1DX4UtSsGT1Sbe")


# In[14]:


def get_tracks(user_id, playlist_id):
    results = sp.user_playlist_tracks(user_id, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
second_results = get_tracks("Spotify", "37i9dQZF1DX4UtSsGT1Sbe")


# In[15]:


song_name = []
song_uri = []
song_id = []
song_artists = []
playlist = second_results
for r in second_results:
    song_name.append(r['track']['name'])
    song_uri.append(r['track']['uri'])
    song_id.append(r['track']['id'])
    song_artists.append(r['track']['artists'][0]['name'])
playlist2_info = pd.DataFrame({'song_name':song_name, 'song_id':song_id, 'artist':song_artists})


# In[16]:


features2_info = pd.DataFrame(sp.audio_features(tracks = song_id[0:99]))
features2_info2 = pd.DataFrame(sp.audio_features(tracks = song_id[99:]))
features2 = pd.concat([features2_info, features2_info2])
features2.reset_index(drop=True, inplace=True)


# In[17]:


second_playlist = pd.concat([playlist2_info, features2], axis=1)
second_playlist.reset_index()


# ### All time top 1000 songs

# In[18]:


third_playlist = sp.user_playlist_tracks("Peter Nordestgaard", "0lNwm5xFEgRx4iDP2DLx3j")


# In[19]:


def get_tracks(user_id, playlist_id):
    results = sp.user_playlist_tracks(user_id, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
third_results = get_tracks("Peter Nordestgaard", "0lNwm5xFEgRx4iDP2DLx3j")


# In[20]:


song_name = []
song_uri = []
song_id = []
song_artists = []
playlist = third_results
for r in third_results:
    song_name.append(r['track']['name'])
    song_uri.append(r['track']['uri'])
    song_id.append(r['track']['id'])
    song_artists.append(r['track']['artists'][0]['name'])
playlist3_info = pd.DataFrame({'song_name':song_name, 'song_id':song_id, 'artist':song_artists})


# In[21]:


features3_info = pd.DataFrame(sp.audio_features(tracks = song_id[0:99]))
features3_info1 = pd.DataFrame(sp.audio_features(tracks = song_id[99:199]))
features3_info2 = pd.DataFrame(sp.audio_features(tracks = song_id[199:299]))
features3_info3 = pd.DataFrame(sp.audio_features(tracks = song_id[299:399]))
features3_info4 = pd.DataFrame(sp.audio_features(tracks = song_id[399:499]))
features3_info5 = pd.DataFrame(sp.audio_features(tracks = song_id[499:599]))
features3_info6 = pd.DataFrame(sp.audio_features(tracks = song_id[599:699]))
features3_info7 = pd.DataFrame(sp.audio_features(tracks = song_id[699:799]))
features3_info8 = pd.DataFrame(sp.audio_features(tracks = song_id[799:899]))
features3_info9 = pd.DataFrame(sp.audio_features(tracks = song_id[899:999]))
features3_info10 = pd.DataFrame(sp.audio_features(tracks = song_id[999:]))
features3 = pd.concat([features3_info, features3_info1, features3_info2, features3_info3, features3_info4, features3_info5, features3_info6, features3_info7, features3_info8, features3_info9, features3_info10])
features3.reset_index(drop=True, inplace=True)


# In[22]:


third_playlist = pd.concat([playlist3_info, features3_info], axis=1)
third_playlist.reset_index()


# ### Modern Chill Rock

# In[23]:


fourth_playlist = sp.user_playlist_tracks("Spotify", "37i9dQZF1DX2UXfvEIZvDK")


# In[24]:


def get_tracks(user_id, playlist_id):
    results = sp.user_playlist_tracks(user_id, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
fourth_results = get_tracks("Spotify", "37i9dQZF1DX2UXfvEIZvDK")


# In[25]:


song_name = []
song_uri = []
song_id = []
song_artists = []
playlist = fourth_results
for r in fourth_results:
    song_name.append(r['track']['name'])
    song_uri.append(r['track']['uri'])
    song_id.append(r['track']['id'])
    song_artists.append(r['track']['artists'][0]['name'])
playlist4_info = pd.DataFrame({'song_name':song_name, 'song_id':song_id, 'artist':song_artists})


# In[26]:


features4_info = pd.DataFrame(sp.audio_features(tracks = song_id[0:]))


# In[27]:


fourth_playlist = pd.concat([playlist4_info, features4_info], axis=1)
fourth_playlist.reset_index()


# ### Soulful Blend

# In[28]:


fifth_playlist = sp.user_playlist_tracks("Spotify", "37i9dQZF1DX8Md3JnnrexB")


# In[29]:


def get_tracks(user_id, playlist_id):
    results = sp.user_playlist_tracks(user_id, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
fifth_results = get_tracks("Spotify", "37i9dQZF1DX8Md3JnnrexB")


# In[30]:


song_name = []
song_uri = []
song_id = []
song_artists = []
playlist = fifth_results
for r in fifth_results:
    song_name.append(r['track']['name'])
    song_uri.append(r['track']['uri'])
    song_id.append(r['track']['id'])
    song_artists.append(r['track']['artists'][0]['name'])
playlist5_info = pd.DataFrame({'song_name':song_name, 'song_id':song_id, 'artist':song_artists})


# In[31]:


features5_info = pd.DataFrame(sp.audio_features(tracks = song_id[0:]))


# In[32]:


fifth_playlist = pd.concat([playlist5_info, features5_info], axis=1)
fifth_playlist.reset_index()


# ### Morning Coffee

# In[33]:


sixth_playlist = sp.user_playlist_tracks("Spotify", "37i9dQZF1DXcgZcN2HVMoe")


# In[34]:


def get_tracks(user_id, playlist_id):
    results = sp.user_playlist_tracks(user_id, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
sixth_results = get_tracks("Spotify", "37i9dQZF1DXcgZcN2HVMoe")


# In[35]:


song_name = []
song_uri = []
song_id = []
song_artists = []
playlist = sixth_results
for r in sixth_results:
    song_name.append(r['track']['name'])
    song_uri.append(r['track']['uri'])
    song_id.append(r['track']['id'])
    song_artists.append(r['track']['artists'][0]['name'])
playlist6_info = pd.DataFrame({'song_name':song_name, 'song_id':song_id, 'artist':song_artists})


# In[36]:


features6_info = pd.DataFrame(sp.audio_features(tracks = song_id[0:99]))
features6_info2 = pd.DataFrame(sp.audio_features(tracks = song_id[99:199]))
features6_info3 = pd.DataFrame(sp.audio_features(tracks = song_id[199:]))
features6 = pd.concat([features6_info, features6_info2, features6_info3])
features6.reset_index(drop=True, inplace=True)


# In[37]:


sixth_playlist = pd.concat([playlist6_info, features6], axis=1)
sixth_playlist.reset_index()


# ### 500 best songs of all times

# In[38]:


seventh_playlist = sp.user_playlist_tracks("Arian", "5dxn0i8MPl6XFVVxNatd6U")


# In[39]:


def get_tracks(user_id, playlist_id):
    results = sp.user_playlist_tracks(user_id, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
seventh_results = get_tracks("Arian", "5dxn0i8MPl6XFVVxNatd6U")


# In[40]:


song_name = []
song_uri = []
song_id = []
song_artists = []
playlist = seventh_results
for r in seventh_results:
    song_name.append(r['track']['name'])
    song_uri.append(r['track']['uri'])
    song_id.append(r['track']['id'])
    song_artists.append(r['track']['artists'][0]['name'])
playlist7_info = pd.DataFrame({'song_name':song_name, 'song_id':song_id, 'artist':song_artists})


# In[41]:


features7_info = pd.DataFrame(sp.audio_features(tracks = song_id[0:99]))
features7_info2 = pd.DataFrame(sp.audio_features(tracks = song_id[99:199]))
features7_info3 = pd.DataFrame(sp.audio_features(tracks = song_id[199:299]))
features7_info4 = pd.DataFrame(sp.audio_features(tracks = song_id[299:399]))
features7_info5 = pd.DataFrame(sp.audio_features(tracks = song_id[399:499]))
features7_info6 = pd.DataFrame(sp.audio_features(tracks = song_id[499:]))
features7 = pd.concat([features7_info, features7_info2, features7_info3, features7_info4, features7_info5, features7_info6])
features7.reset_index(drop=True, inplace=True)


# In[42]:


seventh_playlist = pd.concat([playlist7_info, features7], axis=1)
seventh_playlist.reset_index()


# ### Best fo the Oldies

# In[43]:


eighth_playlist = sp.user_playlist_tracks("Marcel", "6OAF6gkxAe4lqHdSLmGpdd")


# In[44]:


def get_tracks(user_id, playlist_id):
    results = sp.user_playlist_tracks(user_id, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
eighth_results = get_tracks("Marcel", "6OAF6gkxAe4lqHdSLmGpdd")


# In[45]:


song_name = []
song_uri = []
song_id = []
song_artists = []
playlist = eighth_results
for r in eighth_results:
    song_name.append(r['track']['name'])
    song_uri.append(r['track']['uri'])
    song_id.append(r['track']['id'])
    song_artists.append(r['track']['artists'][0]['name'])
playlist8_info = pd.DataFrame({'song_name':song_name, 'song_id':song_id, 'artist':song_artists})


# In[46]:


features8_info = pd.DataFrame(sp.audio_features(tracks = song_id[0:99]))
features8_info2 = pd.DataFrame(sp.audio_features(tracks = song_id[99:199]))
features8_info3 = pd.DataFrame(sp.audio_features(tracks = song_id[199:299]))
features8_info4 = pd.DataFrame(sp.audio_features(tracks = song_id[299:399]))
features8_info5 = pd.DataFrame(sp.audio_features(tracks = song_id[399:499]))
features8_info6 = pd.DataFrame(sp.audio_features(tracks = song_id[499:599]))
features8_info7 = pd.DataFrame(sp.audio_features(tracks = song_id[599:699]))
features8_info8 = pd.DataFrame(sp.audio_features(tracks = song_id[699:799]))
features8_info9 = pd.DataFrame(sp.audio_features(tracks = song_id[799:899]))
features8_info10 = pd.DataFrame(sp.audio_features(tracks = song_id[899:999]))
features8_info11 = pd.DataFrame(sp.audio_features(tracks = song_id[999:]))
features8 = pd.concat([features8_info, features8_info2, features8_info3, features8_info4, features8_info5, features8_info6, features8_info7, features8_info8, features8_info9, features8_info10, features8_info11])
features8.reset_index(drop=True, inplace=True)


# In[47]:


eighth_playlist = pd.concat([playlist8_info, features8], axis=1)
eighth_playlist.reset_index()


# ### 1001 songs you need to hear before you die

# In[48]:


ninth_playlist = sp.user_playlist_tracks("Jimmy Alexander", "6aCHA5HeRfz5gJjllGZ7Of")


# In[49]:


def get_tracks(user_id, playlist_id):
    results = sp.user_playlist_tracks(user_id, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
ninth_results = get_tracks("Jimmy Alexander", "6aCHA5HeRfz5gJjllGZ7Of")


# In[50]:


song_name = []
song_uri = []
song_id = []
song_artists = []
playlist = ninth_results
for r in ninth_results:
    song_name.append(r['track']['name'])
    song_uri.append(r['track']['uri'])
    song_id.append(r['track']['id'])
    song_artists.append(r['track']['artists'][0]['name'])
playlist9_info = pd.DataFrame({'song_name':song_name, 'song_id':song_id, 'artist':song_artists})


# In[51]:


features9_info = pd.DataFrame(sp.audio_features(tracks = song_id[0:99]))
features9_info2 = pd.DataFrame(sp.audio_features(tracks = song_id[99:199]))
features9_info3 = pd.DataFrame(sp.audio_features(tracks = song_id[199:299]))
features9_info4 = pd.DataFrame(sp.audio_features(tracks = song_id[299:399]))
features9_info5 = pd.DataFrame(sp.audio_features(tracks = song_id[399:499]))
features9_info6 = pd.DataFrame(sp.audio_features(tracks = song_id[499:599]))
features9_info7 = pd.DataFrame(sp.audio_features(tracks = song_id[599:699]))
features9_info8 = pd.DataFrame(sp.audio_features(tracks = song_id[699:799]))
features9_info9 = pd.DataFrame(sp.audio_features(tracks = song_id[799:899]))
features9_info10 = pd.DataFrame(sp.audio_features(tracks = song_id[899:999]))
features9_info11 = pd.DataFrame(sp.audio_features(tracks = song_id[999:]))
features9 = pd.concat([features9_info, features9_info2, features9_info3, features9_info4, features9_info5, features9_info6, features9_info7, features9_info8, features9_info9, features9_info10, features9_info11])
features9.reset_index(drop=True, inplace=True)


# In[52]:


ninth_playlist = pd.concat([playlist9_info, features9], axis=1)
ninth_playlist.reset_index()


# ### The ultimate huge playlist

# In[53]:


tenth_playlist = sp.user_playlist_tracks("AROL", "20JT4SnBRiiXBeIXr5f2c0")


# In[54]:


def get_tracks(user_id, playlist_id):
    results = sp.user_playlist_tracks(user_id, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
tenth_results = get_tracks("AROL", "20JT4SnBRiiXBeIXr5f2c0")


# In[55]:


song_name = []
song_uri = []
song_id = []
song_artists = []
playlist = tenth_results
for r in tenth_results:
    song_name.append(r['track']['name'])
    song_uri.append(r['track']['uri'])
    song_id.append(r['track']['id'])
    song_artists.append(r['track']['artists'][0]['name'])
playlist10_info = pd.DataFrame({'song_name':song_name, 'song_id':song_id, 'artist':song_artists})


# In[56]:


features10_info = pd.DataFrame(sp.audio_features(tracks = song_id[0:99]))
features10_info2 = pd.DataFrame(sp.audio_features(tracks = song_id[99:199]))
features10_info3 = pd.DataFrame(sp.audio_features(tracks = song_id[199:299]))
features10_info4 = pd.DataFrame(sp.audio_features(tracks = song_id[299:399]))
features10_info5 = pd.DataFrame(sp.audio_features(tracks = song_id[399:499]))
features10_info6 = pd.DataFrame(sp.audio_features(tracks = song_id[499:599]))
features10_info7 = pd.DataFrame(sp.audio_features(tracks = song_id[599:699]))
features10_info8 = pd.DataFrame(sp.audio_features(tracks = song_id[699:799]))
features10_info9 = pd.DataFrame(sp.audio_features(tracks = song_id[799:899]))
features10_info10 = pd.DataFrame(sp.audio_features(tracks = song_id[899:999]))
features10_info11 = pd.DataFrame(sp.audio_features(tracks = song_id[999:1099]))
features10_info12 = pd.DataFrame(sp.audio_features(tracks = song_id[1099:1199]))
features10_info13 = pd.DataFrame(sp.audio_features(tracks = song_id[1199:1299]))
features10_info14 = pd.DataFrame(sp.audio_features(tracks = song_id[1299:1399]))
features10_info15 = pd.DataFrame(sp.audio_features(tracks = song_id[1399:1499]))
features10_info16 = pd.DataFrame(sp.audio_features(tracks = song_id[1499:1599]))
features10_info17 = pd.DataFrame(sp.audio_features(tracks = song_id[1599:1699]))
features10_info18 = pd.DataFrame(sp.audio_features(tracks = song_id[1699:1799]))
features10_info19 = pd.DataFrame(sp.audio_features(tracks = song_id[1799:1899]))
features10_info20 = pd.DataFrame(sp.audio_features(tracks = song_id[1899:1999]))
features10_info21 = pd.DataFrame(sp.audio_features(tracks = song_id[1999:2099]))
features10_info22 = pd.DataFrame(sp.audio_features(tracks = song_id[2099:2199]))
features10_info23 = pd.DataFrame(sp.audio_features(tracks = song_id[2199:2299]))
features10_info24 = pd.DataFrame(sp.audio_features(tracks = song_id[2299:2399]))
features10_info25 = pd.DataFrame(sp.audio_features(tracks = song_id[2399:2499]))
features10_info26 = pd.DataFrame(sp.audio_features(tracks = song_id[2499:2599]))
features10_info27 = pd.DataFrame(sp.audio_features(tracks = song_id[2599:2699]))
features10_info28 = pd.DataFrame(sp.audio_features(tracks = song_id[2699:2799]))
features10_info29 = pd.DataFrame(sp.audio_features(tracks = song_id[2799:2899]))
features10_info30 = pd.DataFrame(sp.audio_features(tracks = song_id[2899:2999]))
features10_info31 = pd.DataFrame(sp.audio_features(tracks = song_id[2999:3099]))
features10_info32 = pd.DataFrame(sp.audio_features(tracks = song_id[3099:3199]))
features10_info33 = pd.DataFrame(sp.audio_features(tracks = song_id[3199:3299]))
features10_info34 = pd.DataFrame(sp.audio_features(tracks = song_id[3299:3399]))
features10_info35 = pd.DataFrame(sp.audio_features(tracks = song_id[3399:3499]))
features10_info36 = pd.DataFrame(sp.audio_features(tracks = song_id[3499:3599]))
features10_info37 = pd.DataFrame(sp.audio_features(tracks = song_id[3599:3699]))
features10_info38 = pd.DataFrame(sp.audio_features(tracks = song_id[3699:3799]))
features10_info39 = pd.DataFrame(sp.audio_features(tracks = song_id[3799:3899]))
features10_info40 = pd.DataFrame(sp.audio_features(tracks = song_id[3899:3999]))
features10_info41 = pd.DataFrame(sp.audio_features(tracks = song_id[3999:4099]))
features10_info42 = pd.DataFrame(sp.audio_features(tracks = song_id[4099:4199]))
features10_info43 = pd.DataFrame(sp.audio_features(tracks = song_id[4199:4299]))
features10_info44 = pd.DataFrame(sp.audio_features(tracks = song_id[4299:4399]))
features10_info45 = pd.DataFrame(sp.audio_features(tracks = song_id[4399:4499]))
features10_info46 = pd.DataFrame(sp.audio_features(tracks = song_id[4499:4599]))
features10_info47 = pd.DataFrame(sp.audio_features(tracks = song_id[4599:]))
features10 = pd.concat([features9_info, features10_info2, features10_info3, features10_info4, 
                        features10_info5, features10_info6, features10_info7, features10_info8, 
                        features10_info9, features10_info10, features10_info11, features10_info12, 
                        features10_info13, features10_info14, features10_info15, features10_info16, 
                        features10_info17, features10_info18, features10_info19, features10_info20, 
                        features10_info21, features10_info22, features10_info23, features10_info24, 
                        features10_info25, features10_info26, features10_info27, features10_info28, 
                        features10_info29, features10_info30, features10_info31, features10_info32, 
                        features10_info33, features10_info34, features10_info35, features10_info36, 
                        features10_info37, features10_info38, features10_info39, features10_info40, 
                        features10_info41, features10_info42, features10_info43, features10_info44, 
                        features10_info45, features10_info46, features10_info47])
features10.reset_index(drop=True, inplace=True)


# In[57]:


tenth_playlist = pd.concat([playlist10_info, features10], axis=1)
tenth_playlist.reset_index()


# ### Creating the big dataframe

# In[58]:


huge_playlist = pd.concat([first_playlist, second_playlist, third_playlist, fourth_playlist, 
                           fifth_playlist, sixth_playlist, seventh_playlist, eighth_playlist, 
                           ninth_playlist, tenth_playlist])
huge_playlist.reset_index(drop=True, inplace=True)


# In[59]:


# count duplicated values and dropping them
huge_playlist.duplicated(subset='song_name', keep='first').sum()
huge_playlist = huge_playlist.drop_duplicates()
huge_playlist.reset_index(drop=True, inplace=True)
huge_playlist = huge_playlist.dropna()
huge_playlist.reset_index(drop=True, inplace=True)


# ## Clustering

# In[60]:


# even MORE packages!
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import plotly 
import plotly.graph_objs as go
from sklearn.cluster import KMeans 
from sklearn import datasets 
from sklearn.preprocessing import StandardScaler 


# In[61]:


# copying the playlist just in case
hugeplaylist = huge_playlist.copy()


# In[62]:


# dropping extra columns, leaving only the song to use later as index
hugeplaylist.drop(['artist', 'song_id', 'id', 'uri', 'track_href', 'mode', 'analysis_url', 
                   'duration_ms', 'time_signature', 'type'], axis = 1, inplace = True)


# In[63]:


# Song as index! yay!
hugeplaylist.index = hugeplaylist.iloc[:,0]
# pick first column and turn it to index [:,_] - location


# In[64]:


#keep rest of columns
hugeplaylist = hugeplaylist.iloc[:,1:]


# In[65]:


# remove the header name
hugeplaylist.rename_axis(None,inplace=True)


# ### Scaling

# In[66]:


hugeplaylist_scaled = StandardScaler().fit_transform(hugeplaylist)


# In[67]:


hugeplaylist_scaled_df = pd.DataFrame(hugeplaylist_scaled,columns = ['danceability', 'energy', 
                                                                     'key', 'loudness', 
                                                                     'speechiness', 'acousticness', 
                                                                     'instrumentalness', 'liveness', 
                                                                     'valence', 'tempo'])


# #### Using the 'right' number of clusters now

# In[68]:


kmeans = KMeans(n_clusters = 52)


# In[69]:


cluster = kmeans.fit(hugeplaylist_scaled_df)


# In[70]:


#bring cluster into data frame
hugeplaylist_c = hugeplaylist.copy()
hugeplaylist_c['cluster'] = cluster.labels_


# In[71]:


### Adding the cluster column to the original dataframe and reoganizing the data


# In[72]:


huge_playlist['cluster'] = hugeplaylist_c['cluster'].values


# In[179]:


# creating the cluster thingy
from IPython.core.display import display
from IPython.display import IFrame


def song_cluster(song):
    song = sp.search(q = song, limit = 1)
    song_id = song['tracks']
    song_id = song_id['items'][0]['id']
    song_features = sp.audio_features(song_id)
    song_data = pd.DataFrame(song_features, index= [0])
   # droping the numeric columns i didn't use
    song_data.drop(['mode', 'duration_ms', 'time_signature'], axis = 1, inplace = True)  
    song_num = song_data._get_numeric_data()
    song_scaled = StandardScaler().fit_transform(song_num)
    cluster = kmeans.predict(song_scaled)
    song_cluster = huge_playlist.loc[huge_playlist['cluster'] == int(cluster)]
    song_cluster.reset_index(drop=True, inplace=True) 
    song_name_id = random.choice(song_cluster["id"])
    songname = sp.track(song_name_id)['name']
    artist = sp.track(song_name_id)['artists'][0]['name']
    def recommend(song_name_id):
        display(IFrame(src=f"https://open.spotify.com/embed/track/{song_name_id}",
                        width="320",
                        height="80",
                        frameborder="0",
                        allowtransparency="true",
                        allow="encrypted-media",))
    return print("\033[1m" + 'That song is not hot right now. But listen to ' + songname + ' by ' + artist + ". I think you'll like it!."), recommend(song_name_id)


# ## The Ultimate Suggester

# In[185]:


# new suggester attempt

def second_suggester():
    song = str(input( "\033[1m" + """
    Welcome to the awesome song recommender!
    What song do you have in mind?: 
    """).lower().replace(" ", ''))
    # check hot 100
    check = billboard_top100[billboard_top100['song'].str.lower().str.replace(" ","").str.contains(song)]
    # get index
    index = check.index.tolist()
    if len(check) == 0:
        song_cluster(song)
        song2 = str(input("\033[1m" + "Want to try again? [y/n]: ")).lower().replace(" ", '')
        if song2 == 'y':
            print("\033[1m" + 'Awesome! Here, have another go:')
            second_suggester()
        elif song2 != 'n':
            print("\033[1m" + "Oh, come on, that's not an answer")
        elif song2 == 'n':
            print("\033[1m" + 'Oh well, your bad, this is an awesome recommender')
            return
    else:
        answer1 = input("\033[1m" + "Are you thinking about '" + billboard_top100.song[index].values[0] + "' by '" + billboard_top100.artist[index].values[0] + "'? [y/n]: ")
        #make a song suggestion
        if answer1.lower() == 'y':
            suggestion = billboard_top100.sample().index.tolist()
            print("\033[1m" + "That's a hot song! Listen to '" + billboard_top100['song'][suggestion].item() + "' by '" + billboard_top100['artist'][suggestion].item() + "' I think you'll like it.")
            song2 = str(input("\033[1m" + "Want to try again? [y/n]: ")).lower().replace(" ", '')
            if song2 == 'y':
                print("\033[1m" + 'Awesome! Here, have another go:')
                second_suggester()
            elif song2 != 'n':
                print("\033[1m" + "Oh, come on, that's not an answer")
            elif song2 == 'n':
                print("\033[1m" + 'Oh well, your bad, this is an awesome recommender')
                return
        elif answer1.lower() != 'n':
            print("\033[1m" + "Oh, come on, that's not an answer")
            song2 = str(input("\033[1m" + "Want to try again? [y/n]: ")).lower().replace(" ", '')
            second_suggester()
        elif answer1.lower() == 'n':
            song_cluster(song)
            song2 = str(input("\033[1m" + "Want to try again? [y/n]: ")).lower().replace(" ", '')
            if song2 == 'y':
                print("\033[1m" + 'Awesome! Here, have another go:')
                second_suggester()
            elif song2 != 'n':
                print("\033[1m" + "Oh, come on, that's not an answer")
            elif song2 == 'n':
                print("\033[1m" + 'Oh well, your bad, this is an awesome recommender')
                return
        elif song2 != 'n':
            print("\033[1m" + "Oh, come on, that's not an answer")
        elif song2 == 'n':
            print("\033[1m" + 'Oh well, your bad, this is an awesome recommender')
            return
second_suggester()


# In[ ]:




