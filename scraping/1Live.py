import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as soup
import csv

# setting up cols and list for dataframe
cols = ["Title","Artist"]
tracksL = []
times = []

# get html of the desired page
URL = "https://www1.wdr.de/radio/1live/on-air/1live-playlist/index.jsp#searchPlaylistResult"
page = requests.get(URL)

# parse with BeautifulSoup
soup = soup(page.content, 'html.parser')

# find right container
results = soup.find(id='searchPlaylistResult')

# cache tracks + artists + time 
tracks = results.find_all('tr', class_ = "data")

# we start at i=1 because 0 is the header
i=1

# extract relevant information + strip html
while i < 11:
    track_ele = tracks[i].find_all('td', class_= 'entry')[0]
    artist_ele = tracks[i].find_all('td', class_= 'entry')[1]
    time_ele = tracks[i].find('th', class_='entry')
    tracksL.append([track_ele.text.strip(),artist_ele.text.strip()])
    times.append(time_ele.text.strip())
    i += 1
    
d = pd.DataFrame(tracksL, columns=cols, index=times)

d.to_csv('einsLive.csv', mode='a', header=False)




    





