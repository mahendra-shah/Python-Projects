import random
import json

lst1 = ["Abhimanyu", "Mahendra", "Raja", "Aniket", "Bhumesh", "Praveen", "Sajjad", "Akash Deshmukh", "Aadarsh"]
lst2 = [ "1", "2", "p12", "p26", "5", "6" ,"7" ,"8" ,"p10" ]

random.shuffle(lst1)
random.shuffle(lst2)

dict1 = {}
with open("LaptopShuffle.json", "w+") as f:
    for keys in lst1:
        for value in lst2:
            dict1[keys] = value
            lst2.remove(value)
            break
# print(dict1)
    json.dump(dict1, f, indent=4)
# print(dict1)

# f.close()


