#!/usr/bin/env python3

import argparse
from urllib import request
from datetime import datetime
from dateutil.relativedelta import relativedelta

parser = argparse.ArgumentParser()
parser.add_argument('type', help='Which data to download',
    choices=['applications-all', 'transactions-for-value', 'by-regions', 'by-authority', 'searches'])
parser.add_argument('-s', '--start', help='The date in YYYY-MM to get files from, defaults to today')
parser.add_argument('-e', '--end', help='The date in YYYY-MM to retrive files to, defaults to start date or today')

args = parser.parse_args()
base_url = 'http://publicdata.landregistry.gov.uk/transaction-data/'
from_date = to_date = today = datetime.today()
types = {
    'applications-all' : 'Number-and-types-of-applications-by-all-account-customers',
    'transactions-for-value' : 'Number-and-types-of-transactions-for-value-by-all-account-customers',
    'by-regions' : 'Number-of-applications-in-England-and-Wales-divided-by-region',
    'by-authority' : 'Number-of-applications-in-England-and-Wales-divided-by-local-authority',
    'searches' : 'Number-of-searches-by-all-account-customers'
}

if args.start:
    from_date = datetime.strptime(args.start, '%Y-%m')
    to_date = from_date
if args.end:
    to_date = datetime.strptime(args.end, '%Y-%m')

def downloadFile(type, date):
    filename = types[type] + '-' + date + '.csv'
    request.urlretrieve(base_url+filename, filename)

i = from_date
while i <= to_date:
    downloadFile(args.type, i.strftime('%Y-%m'))
    i = i + relativedelta(months=1)
