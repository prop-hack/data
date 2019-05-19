#!/usr/bin/env python3

import argparse
from urllib import request
from datetime import datetime

published = datetime.strptime('2019-02', '%Y-%m')
base_url = 'http://publicdata.landregistry.gov.uk/market-trend-data/house-price-index-data/'
types = {
    'hpi-full': 'UK-HPI-full-file-2019-02.csv',
    'avg-price': 'Average-prices',
    'avg-by-property': 'Average-prices-Property-Type',
    'sales': 'Sales',
    'cash-mortgage-sales': 'Cash-mortgage-sales',
    'ftb-and-foc': 'First-Time-Buyer-Former-Owner-Occupied',
    'new-build-and-resold': 'New-and-Old',
    'index': 'Indices',
    'index-seasonal': 'Indices-seasonally-adjusted',
    'avg-seasonal': 'Average-price-seasonally-adjusted',
    'reposessions': 'Repossession'
}

parser = argparse.ArgumentParser()
parser.add_argument('type', help='Which data to download', choices=types.keys())
parser.add_argument('-p', '--published', help='The published date in YYYY-MM to get the files from, defaults to 2019-02')

args = parser.parse_args()

if args.published:
    published = datetime.strptime(args.published, '%Y-%m')

filename = types[args.type] + '-' + published.strftime('%Y-%m') + '.csv'

try:
    request.urlretrieve(base_url+filename, filename)
except request.HTTPError as e:
    print('Error getting file -', e)
