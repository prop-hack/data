#!/usr/bin/env python3

import argparse
import json
import os
from urllib import request

API_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json?key={key}&query={query}&location={loc}&radius={radius}'

parser = argparse.ArgumentParser()
parser.add_argument('lat', help='Latitude')
parser.add_argument('lng', help='Longitude')
parser.add_argument('-k', '--key', help='The Google API key, will override any GOOGLE_API_KEY env variable')
parser.add_argument('-p', '--page', help='The next page token if available')
args = parser.parse_args()

api_key =  args.key or os.environ['GOOGLE_API_KEY']

req_url = API_URL.format(key=api_key, query='shop', loc=args.lat+','+args.lng, radius='500')

if (args.page):
    req_url = req_url+'&pagetoken='+args.page

with request.urlopen(req_url) as resp:
    json_resp = json.loads(resp.read())
    print(json.dumps(json_resp, indent=2))
