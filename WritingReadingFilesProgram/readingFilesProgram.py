# Python reading files (.txt, .json, .csv)

import json
import csv

file_path = "output.csv"

try:
    with open(file_path, 'r') as file:
        # content = json.load(file)
        content = csv.reader(file)
        for line in content:
            print(line[0])
        # print(content["name"])
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")
