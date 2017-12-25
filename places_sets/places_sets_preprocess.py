"""
This code preprocesses captions from a CSV file, and saves it as a json.

json file will have the form (a list of dictionaries)
[{ file_loc: 'path/to/image/set/',
    file_names: ['1.jpg', '2.jpg', ...],
    caption: ['sentence_1', 'sentence_2', ...],
    id: <create an id here for now?> },  ...]

"""

import os
import json
import csv

data_paths = list(os.walk('/local-scratch2/ajakash/aabdujyo/2017_set_compression/Data/Sets_12500'))

with open('Category Image Description - Sheet1.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
#    reader_utf_8 = utf_8_encoder(reader)

    out = []
    # Add a dictionary of items per image set
    for row in reader:
        if row[1] == 'Description' or row[1] == 'Empty':
            continue

        print row

        filenames = [x[0].split('/')[-1] for x in data_paths]
        loc = filenames.index(row[0])
        print loc
        print data_paths[loc]