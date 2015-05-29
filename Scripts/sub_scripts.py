import sys
import csv

# this program take a file of pie database client_id's exported from machup
# as a comma delimited file with quotes.
# the file is then formated for cutting and pasting into an
# SQL query to select all domains associated with those client_id's

def clean_client_ids(input_file,out_file):
    data = csv.reader(input_file,delimiter=',')
    data = [row for row in input_file]
    count = 0
    new_file = ''
    for i in data:
        if len(i) > 3:
            new_file = new_file + i[:-1].replace("\"","'") + ",\n"
    out_file.write(new_file[:-2])

## below is for testing without drag and drop functionality. 
# def strip_suffix(name):  #strip suffix to create output file name w/'.csv'
#    return name[:-4]

# file_ext = '.ff'

# fname = 'client_id_test.Csv'
# with open(fname, 'r') as input_file, open(strip_suffix(fname) + file_ext, 'w') as out_file:
#                clean_client_ids(input_file, out_file)

