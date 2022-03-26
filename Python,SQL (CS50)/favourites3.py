import csv

Genre =input("Title: ").strip().upper()

counter=0

with open("favourites.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        if row["Genre"].strip().upper()== Genre:
            counter+=1

print(counter)
