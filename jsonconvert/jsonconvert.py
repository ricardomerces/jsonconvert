import json
import csv

def convert(*args):
    keys = ()
    data = []
    for item in args:
        keys += item,

    with open('file.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, keys)
        for row in reader:
            data.append(dict(row))

    with open('file.json', 'w') as jsonfile:
        jsonfile.write(json.dumps(data))

    print(json.dumps(data, indent=4))