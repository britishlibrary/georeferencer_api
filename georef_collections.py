import csv
import requests
import pickle
import config


headers = {'Authorization': 'Token ' + config.georef_key}

r = requests.get('http://api.oldmapsonline.org/1.0/collections', headers=headers)

for re in r:
    print(re)
