import csv
import requests
import pickle
import config

with open('./ssheets/2021_06_John_dels.csv', newline='') as f:
    reader = csv.reader(f)
    maps = list(reader)

headers = {'Authorization': 'Token ' + config.georef_key}

maps = [['002OSD000000001U00008000']]
responses = []
for map in maps:
    print(map[0])
    response = requests.get('http://api.oldmapsonline.org/1.0/maps/external/' + map[0], headers=headers)
    # map.append(response.json()['external_id'])
    # responses.append(map)
    response = requests.get('http://api.oldmapsonline.org/1.0/maps/' + response.json()['id'] + '/georeferences', headers=headers)
    print(response.json())

# writer = csv.writer(open('./ssheets/2021_06_John_dels_ext.csv', 'w'))
# for row in responses:
#     writer.writerow(row)
