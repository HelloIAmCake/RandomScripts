#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import sys
import random

print("What is your anime planet username?")
user = sys.stdin.readline()

result_num = 0
while (result_num < 1):
    print("How many results do you want to return?")
    result_num = int(sys.stdin.readline())

    if (result_num < 1):
        print("Number must be 1 or greater.")

page = 1
animeList = []
totalAnime = 1

while (len(animeList) < totalAnime):
    watchlist_url = "https://www.anime-planet.com/users/" + user.rstrip() + "/anime/wanttowatch?page=" + str(page)
    get = requests.get(watchlist_url)
    html = get.text
    soup = BeautifulSoup(html, 'html.parser')

    totalAnime = int(soup.find("b").get_text())
    if (result_num > totalAnime):
        print("You requested more anime than what is in your want to watch list")
        exit()

    for anime in soup.find_all('h3'):
        animeList.append(anime.get_text())

    page += 1

print("\nYour random result" + (" is:" if result_num == 1 else "s are:"))
for result in random.sample(animeList, result_num):
    print(result)
