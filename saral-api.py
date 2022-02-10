import requests
import json
import os

#### saral api

if os.path.exists("courses.json"):
    with open("courses.json", "r") as f:
        
        data = json.load(f)
        print("from file")
else:
    data = requests.get("https://saral.navgurprint(cuntr)ukul.org/api/courses")
    with open("courses.json", "w") as f:
        
        data = json.loads(data.text)
        out_file = json.dump(data, f, indent=4)
# print(data["availableCourses"])


##### Starts here meraki(api-again)
# More updated (print course id by indexig given by user)


if os.path.exists("courses.json"):
    with open("courses.json", "r") as f:
        
        data = json.load(f)
        print("from file")
else:
    data = requests.get("https://saral.navgurukul.org/api/courses")
    with open("courses.json", "w") as f:
        
        data = json.loads(data.text)
        out_file = json.dump(data, f, indent=4)

corsList = data["availableCourses"]   # all courses stored in this array

######list of courses y indexing
cuntr = 1
for courses in corsList:
    print(cuntr, '→', courses["name"])
    cuntr+=1

usrInput = int(input("Give Index: "))   # user input

cuntr = 1                                # counter for counting index
for corseId in range(len(corsList)):        # running loop on legth of corsList
    if cuntr == usrInput:
        # print("when matched")
        courseMatch = corsList[corseId]          # course id will be stored here
        print("Course Name:", courseMatch["name"])   # here we get the desired output
        break
    else:
        cuntr+=1

with open("exercises.json", "w") as file:
    url = ("http://saral.navgurukul.org/api/courses/"+courseMatch["id"]+"/exercises")
    print(url)
    data = requests.get(url)
    data1 = json.loads(data.text)
    out_file = json.dump(data1, file, indent=4)
    exerciseList = (data1["data"])              #all exercises will be stored here
    # print(exerciseList)                

#######For exercise from the courseyou selected
cuntr2 = 1
for courses2 in exerciseList:
    print(cuntr2, '→', courses2["name"])    
    cuntr2+=1

cuntr2 = 0
exerciseInput = int(input("Give name serial no. "))
for exerciseId in range(len(exerciseList)):
    if cuntr2 == exerciseInput:
        exerciseMatch = exerciseList[exerciseId]
        print(exerciseMatch)
        print("Child exercise name", '→', exerciseMatch["name"])
        # print(exerciseMatch)
        break
    else:
        cuntr2+=1
with open("child-exercise.json", "w") as fle:
    out_file = json.dump(exerciseMatch, fle, indent=4)
    
