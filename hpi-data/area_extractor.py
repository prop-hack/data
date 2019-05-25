#!/usr/bin/env python3

import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('file', help='Which CSV to open')

args = parser.parse_args()
filename = args.file
unique_area = {}

with open('extracted.csv', 'w') as save_file:

    with open(filename, 'r') as file:
        for line in file:
            line_split = line.split(',')
            unique_area[line_split[2]] = line_split[1]

    for code in unique_area:
        print(code, unique_area[code])
        save_file.write(code + ', ' + unique_area[code] + '\n')
