import json, os


def startInsert():
    l = []
    if os.path.exists("json.json"):
        
        with open("json.json", "r") as f:
            l = json.load(f)
            id = l[-1]["id"]

        insert(l, id)
    else:
        id=0
        insert(l, id)

def insert(l, id, update=False, delete=False):
    if update:
        id = id
    else:
        max_id = l[0]["id"]
        for data in l:
            if data["id"] > max_id:
                max_id = data["id"]
        id = max_id+1
        
    with open("json.json", "w") as f:
        if(delete != True):
            a = {
                "id":id,
                "name":input("name:"),
                "age":int(input("age:")),
                "gender":input("gender:")
            }
            l.append(a)
        json.dump(l, f, indent=4)



def updateDetail(id, delete = False):
    if os.path.exists("json.json"):
        with open("json.json", "r") as f:
            allData = json.load(f)
            for data in allData:
                if data["id"] == id:
                    allData.remove(data)
                    if(delete):
                        insert(allData, id, False, True)
                        return
                    insert(allData, id, True)
                    return

    print("user not available")


def showDetail(id):
    if os.path.exists("json.json"):

        with open("json.json", "r") as f:
            allData = json.load(f)
            for data in allData:
                if data["id"] == id:
                    print(data)
                    return
    print("data not found")

def deleteDetail(id):
    updateDetail(id, True)

def add(a, b):
    return a+b

if __name__ == "__main__":
    inp = input('input something')

