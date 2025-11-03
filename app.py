import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

""" for i in range(len(data)):
    print(data[i]["title"])  


answer2 = input("after what year do you want to see the movies of? start at 1961")
for i in range(0,len(data)):
    if answer2 < str(data[i]["year"]):
        print(data[i]["title"])

answer3 = input("after what year do you want to see the movies of? start at 1961")
answer4 = input("before what year do you want to see the movies of?")
for i in range(0,len(data)):
    if answer3 <= str(data[i]["year"]) and answer4 >= str(data[i]["year"]):
        print(f"the results include: {data[i]["title"]}")

answer5 = input("during what year would you want to see the movies of? start at 1961 and end at 2023.")
for i in range(0,len(data)):
    if answer5 == str(data[i]["year"]):
        print(data[i]["title"])
 """
answer6 = input("search for a movie: input title, year, cast, genres, etc.")
for i in range(0,len(data)):
    if answer6 == str(data[i]["title"]) or answer6 == str(data[i]["year"]) or answer6 == str(data[i]["cast"]) or answer6 == str(data[i]["genres"]):
        print(data[i]["title"])
""" 
answer = input("what genre do you want to search? capitalize the first letter of your answer")
for i in range(0, len(data)):
    if answer in data[i]["genres"]:
        print(data[i]["title"]) 

 """
   
        
