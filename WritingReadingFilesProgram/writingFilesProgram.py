# Python writing files (.txt .json .csv)

import json
import csv # comma separated values

#employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

# employee = {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "cook"
# }

employees = [["Name", "Age", "Job"], 
             ["Alex", 30, "Cook"], 
             ["Patrick", 37, "Unemployed"], 
             ["Sandy", 27, "Scientist"]]

# txt_data = "I like pizza!"

file_path = "output.csv"

# file_path = "output.txt"
# file_path = "C://Users//gancea//Desktop//output.txt"

try:
    with open(file=file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        # json.dump(employee, file, indent=4)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")