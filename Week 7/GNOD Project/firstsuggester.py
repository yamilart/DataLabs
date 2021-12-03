#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# importing libraries

from bs4 import BeautifulSoup
import re 
import requests
import pandas as pd
from tqdm.notebook import tqdm
from random import randint


# In[ ]:


# storing link in a variable
url = "https://www.billboard.com/charts/hot-100"
# downloading  html with a get request
response = requests.get(url)
# check response status code 
response.status_code


# In[ ]:


# parsing and storing the contents of the url call
billboardsoup = BeautifulSoup(response.content, 'html.parser')
top_100 = len(billboardsoup.select('h3.c-title.a-no-trucate'))


# In[ ]:


# looping the songs/artists
song = []
artist = []

for i in tqdm(range(top_100)):
    song.append(billboardsoup.select('h3.c-title.a-no-trucate')[i].get_text(strip=True))
    artist.append(billboardsoup.select('span.c-label.a-font-primary-s')[i].get_text(strip=True))


# In[ ]:


billboard_top100 = pd.DataFrame({'song':song,'artist':artist})


# In[ ]:


def suggester():
    song = str(input("What song do you have in mind?: ").lower().replace(" ", ''))
    # check hot 100
    check = billboard_top100[billboard_top100['song'].str.lower().str.replace(" ","").str.contains(song)]
    # get index
    index = check.index.tolist()
    if len(check) == 0:
        print("Oh well, my bad, but that song is not hot. Anyway! Good for you for not following the crowds!")
        song2 = str(input("Want to try again? [y/n]: ")).lower().replace(" ", '')
        if song2 == 'y':
            print('Awesome! Here, have another go:')
            suggester()
        else:
            print('Oh well, your bad, this is an awesome recommender')
    else:
        answer1 = input("Are you thinking about '" + billboard_top100.song[index].values[0] + "' by '" + billboard_top100.artist[index].values[0] + "'? [y/n]: ")
    #make a song suggestion
        if answer1.lower() == 'y':
            suggestion = billboard_top100.sample().index.tolist()
            print("Then listen to '" + billboard_top100['song'][suggestion].item() + "' by '" + billboard_top100['artist'][suggestion].item() + "' I think you'll like it.")
            song2 = str(input("Want to try again? [y/n]: ")).lower().replace(" ", '')
            if song2 == 'y':
                print('Awesome! Here, have another go:')
                suggester()
            else:
                print('Oh well, your bad, this is an awesome recommender')
        else:
            print("That song is not hot, good for you for not following the crowds!")
            song2 = str(input("Want to try again? [y/n]: ")).lower().replace(" ", '')
            if song2 == 'y':
                print('Awesome! Here, have another go:')
                suggester()
            else:
                print('Oh well, your bad, this is an awesome recommender')
            
suggester()

