

import json
import requests

url = 'http://www.omdbapi.com'
title = input('Type a movie title: ')

args = {'t': title}

resp = requests.get(url, params=args)

js_data = resp.json()

try:
	print('title:', js_data['Title'])
	print('plot:', js_data['Plot'])
	print('year:', js_data['Year'])
	print('IMDB ID:', js_data['imdbID'])
	print('Plex_Title:', js_data['Title'],'(',js_data['Year'],')')
except:
	print('Sorry, no match for', title)
