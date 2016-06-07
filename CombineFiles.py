# Combine the File from the Aruba Team with the two from Jason with Location IDs
__author__ = 'Tony Herrington'

import argparse
import csv
import pandas
import sys

# Get input args
parser = argparse.ArgumentParser(description='Combine the first CSV file with a second one matching on Deal Reg Number.\nNote: The second file must only have 2 columns the first one with\nDeal Reg Number and the second with the Location ID')
parser.add_argument('first_file', help='First Input CSV file name')
parser.add_argument('second_file', help='Second Input CSV file name')
args = parser.parse_args()

print('First Input file: %s' % args.first_file)
print('Second Input file: %s' % args.second_file)
output_file = 'combined_output.csv'
print('Output file: %s' % output_file)

# Read first input CSV file
print('Reading first file')
try:
    df_first = pandas.read_csv(args.first_file, dtype=str)
except:
    print('Error: Could not read first file: %s' % args.first_file)
    sys.exit(1)

# Read second input CSV file
print('Reading second file')
try:
    df_second = pandas.read_csv(args.second_file, dtype=str)
    #df_second = pandas.read_excel(args.second_file)
except:
    print('Error: Could not read second file: %s' % args.second_file)
    sys.exit(1)

print(df_second.head)

# Remove Line Feeds from fields
# data_frame = data_frame.replace({'\n': ' '}, regex=True)

#Merge the two data frames
print('Merging files')
df_merged = pandas.merge(df_first, df_second, left_on='Deal Registration Number', right_on='Deal Registration Number', how='left')

# Write combined CSV file
try:
    print('Creating output file.')
    df_merged.to_csv(output_file, index=False, quoting=csv.QUOTE_ALL, encoding='utf-8')
except:
    print('Error: Could not write output file: %s' % output_file)
    sys.exit(1)

print('Completed')