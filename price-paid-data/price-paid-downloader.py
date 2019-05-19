#!/usr/bin/env python3

import argparse
from urllib import request
from datetime import datetime
from dateutil.relativedelta import relativedelta

base_url = 'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/'
from_date = to_date = datetime.today()

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--start', help='The start year in YYYY to get files from, defaults to current year')
parser.add_argument('-e', '--end', help='The end year in YYYY to retrive files to, defaults to start or current year')

args = parser.parse_args()

if args.start:
    from_date = datetime.strptime(args.start, '%Y')
    to_date = from_date
if args.end:
    to_date = datetime.strptime(args.end, '%Y')

def downloadFile(date):
    filename = 'pp-' + date + '.csv'
    try:
        request.urlretrieve(base_url+filename, filename)
    except request.HTTPError as e:
        print('Error getting file -', e)

i = from_date
while i <= to_date:
    downloadFile(i.strftime('%Y'))
    i = i + relativedelta(years=1)
