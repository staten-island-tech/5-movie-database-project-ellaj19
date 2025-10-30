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


""" answer = input("what genre do you want to search? capitalize the first letter of your answer")
for i in range(0, len(data)):
    if answer in data[i]["genres"]:
        print(data[i]["title"]) """


    
answer = input("what genre do you want to search? capitalize the first letter of your answer")
for i in range(0, len(data)):
    if answer in data[i]["year"]:
        print(data[i]["title"])