#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import re


# Get JSON script and load
headers = {"User-Agent": "Mozilla/5.0"}
url = "https://www.imdb.com/chart/top/"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text 
    soup = BeautifulSoup(html, "html.parser")
    
movie_list = soup.find("script", type="application/ld+json")

jason_text = movie_list.get_text(strip=True)
data = json.loads(jason_text)

items = data['itemListElement']

res = []
movies = []


# Scrape all important information
for idx, item in enumerate(items):
    
    tmp = {
        "name":"",
        "rank":"",
        "year":1000,
        "genre":"",
        "duration":"",
        "rating":1.1,
        "url":""
    }
    
    ## 1. Movie Titles
    tmp['name'] = item['item']['name']

    ## 2. Rankings
    rank = idx+1
    tmp['rank'] = rank

    ## 3. Genre
    tmp['genre'] = item['item']['genre']

    ## 4. Rating
    tmp['rating'] = item['item']['aggregateRating']['ratingValue']

    ## 5. Year
    tmp['url'] = item['item']['url']
    res.append(tmp)

for idx, x in enumerate(res):
    response = requests.get(x['url'], headers=headers)
    if response.status_code == 200:
        html = response.text 
        soup = BeautifulSoup(html, "html.parser")
        year_tag = soup.find("a", href=re.compile(r"/title/tt\d+/releaseinfo"))
        year = year_tag.get_text(strip=True)
        x['year'] = year
    
    ## 6. duration
    for li in soup.find_all("li", class_="ipc-inline-list__item"):
        if not li.find("a"):
            text = li.get_text(strip=True)
            if "h" in text:    
                runtime = text
                x['duration'] = runtime
                break
    print(x)            
         

df = pd.DataFrame(res)
df.to_csv("imdb_top250_basic.csv", index=False)
print(df.head())

