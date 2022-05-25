#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import sys
import random

print("What is your anime planet username?")
user = sys.stdin.readline()

page = 1
animeList = []
totalAnime = 1

while (len(animeList) < totalAnime):
    watchlist_url = "https://www.anime-planet.com/users/" + user.rstrip() + "/anime/wanttowatch?page=" + str(page)
    #print(watchlist_url)
    html = requests.get(watchlist_url).text
    soup = BeautifulSoup(html, 'html.parser')

    totalAnime = int(soup.find("b").get_text())
    for anime in soup.find_all('h3'):
        animeList.append(anime.get_text())

    page += 1

print("Your random anime is:")
print(random.choice(animeList))
