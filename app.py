import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

""" for i in range(len(data)):
    print(data[i]["title"])  """


""" answer = input("after what year do you want to see the movies of?")
while answer >= 1961:
    check = data >= answer
    print(check[answer]["title"]) """

genrelist = ["Drama",
             "Crime",
             "War",
             "Comedy",
             "Fantasy",
             "Independent",
             "Noir",
             "Thriller",
             "Historical",
             "Action",
             "Romance",
             "Western",
             "Mystery",
             "Musical",
             "Science Fiction",
             "Disaster",
             "Political",
             "Family",
             "Adventure",
             "Biography",
             "Suspense",
             "Animated"]
print(genrelist)
answer = input("what genre do you want to search?")
for i in range(0, len(data)):
    if data[i]["genres"] == answer:
        print(data[i]["title"])
        