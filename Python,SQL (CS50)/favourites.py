import csv

Genres = {}

with open("favourites.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        Genre=row["Genre"].strip().upper()
        if not Genre in Genres:
            Genres[Genre]=0
        Genres[Genre]+=1

for Genre in sorted(Genres, key=lambda Genre: Genres[Genre], reverse=True):
    print(Genre, Genres[Genre])
