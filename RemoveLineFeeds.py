# Remove the Line Feeds from fields in the CSV file
__author__ = 'Tony Herrington'

import argparse
import csv
import pandas
import sys

# Get input args
parser = argparse.ArgumentParser(description='Remove Line Feeds from fields in CSV file')
parser.add_argument('input', help='Input CSV file name')
parser.add_argument('output', help='Output CSV file name')
args = parser.parse_args()

print('Input file: %s' % args.input)
print('Output file: %s' % args.output)

# Read input CSV file
try:
    data_frame = pandas.read_csv(args.input, dtype=str)

except:
    print('Error: Could not read file: %s' % args.input)
    sys.exit(1)

# Remove Line Feeds from fields
print('Removing line feeds in fields')
data_frame = data_frame.replace({'\n': ' '}, regex=True)
data_frame = data_frame.replace({'\r': ' '}, regex=True)
print(data_frame.head)

# Write output CSV file without Line Feeds in fields
try:
    print('Creating output file')
    data_frame.to_csv(args.output, index=False, quoting=csv.QUOTE_ALL, encoding='utf-8')
except:
    print('Error: Could not write file: %s' % args.output)
    sys.exit(1)

print('Complete')
