import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

for i in range(len(data)):
    print(data[i]["title"])

list = [1,2,3,4,5]
for i in range(list):
    print(list[i])
