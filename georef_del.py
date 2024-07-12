import csv
import requests
import pickle
import config
import pdb

with open('./ssheets/ktop_jh_del.csv', newline='') as f:
    reader = csv.reader(f)
    maps = list(reader)

headers = {'Authorization': 'Token ' + config.georef_key}

responses = []
for map in maps[1:]:
    r = requests.get('http://api.oldmapsonline.org/1.0/maps/external/' + map[0], headers=headers)
    r_get = requests.get('http://api.oldmapsonline.org/1.0/maps/' + r.json()['id'] + '/georeferences', headers=headers)
    georef_response = r_get.json() #['items']

    # Delete if no gcps
    if 'items' in georef_response:
        if len(georef_response['items'][0]['gcps']) == 0:
            response_del = requests.delete('http://api.oldmapsonline.org/1.0/maps/' + map[0], headers=headers)
            print(map[0])
            # response_del = requests.get('http://api.oldmapsonline.org/1.0/maps/' + map[0], headers=headers)
            for r in response_del:
                responses.append(r)

print(len(responses))

# georefs = []
# for mapid in mapids:
#     r = requests.get('http://api.oldmapsonline.org/1.0/maps/' + mapid[4] + '/georeferences', headers=headers)
#     georef = r.json()['items'][0]
#     georef['external_id'] = mapid[0]
#     georefs.append(georef)
