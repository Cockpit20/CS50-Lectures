import csv
import re

counter=0

with open("favourites.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        Genre=row["Genre"].strip().upper()
        if re.search("^(COMEDY|THE.COMEDY)$",Genre):
            counter+=1

print(f"Number of people who like Comedy: {counter}")
