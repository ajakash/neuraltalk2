"""
This code preprocesses captions from a CSV file, and saves it as a json.

json file will have the form (a list of dictionaries)
[{ file_loc: 'path/to/image/set/',
    file_names: ['1.jpg', '2.jpg', ...],
    captions: ['sentence_1', 'sentence_2', ...],
    id: <create an id here for now?> },  ...]

TO UPDATE: Modify so that it processes folders with <10 images as well
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

        #print row

        filenames = [x[0].split('/')[-1] for x in data_paths]
        loc = filenames.index(row[0])
        #print loc
        #print data_paths[loc]

        # Currently taking
        if len(data_paths[loc][2]) == 10:
            set_info = {}
            set_info['file_loc'] = data_paths[loc][0]
            set_info['file_names'] = data_paths[loc][2]

            caption = row[1].split('.')
            if caption[-1]=='':
                caption = caption[:-1]

            set_info['captions'] = caption
            set_info['id'] = loc

            #print set_info
            out.append(set_info)

    json.dump(out, open('sets_raw.json', 'w'))

    #print out