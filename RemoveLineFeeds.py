# Remove the Line Feeds from fields in the CSV file
__author__ = 'Tony Herrington'

import argparse, csv, pandas, sys

# Get input args
parser = argparse.ArgumentParser(description='Remove Line Feeds from fields in CSV file')
parser.add_argument('-i', '--input', help='Input CSV file name', required=True)
parser.add_argument('-o', '--output', help='Output CSV file name', required=True)
args = parser.parse_args()

print('Input file: %s' % args.input)
print('Output file: %s' % args.output)

# Read input CSV file
try:
    df = pandas.read_csv(args.input)
except:
    print('Error: Could not read file: %s' % args.input)
    sys.exit(1)

# Remove Line Feeds from fields
df = df.replace({'\n': ' '}, regex=True)

# Write output CSV file without Line Feeds in fields
try:
    print('Creating output file.')
    df.to_csv(args.output, index=False, quoting=csv.QUOTE_ALL, encoding='utf-8')
except:
    print('Error: Could not write file: %s' % args.output)
    sys.exit(1)

