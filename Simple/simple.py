import random

amount = 10

def generateList(amount):
    list = []
    i = 1
    while i <= amount:
        dictionary = {"id": i, "edad": random.randint(1, 100)}
        list.append(dictionary)
        i += 1
    return list

def orderList(list):
    list.sort(reverse=True, key = lambda dict: dict["edad"])
    print("Youngest person's id: ", list[0]["id"])
    print("Oldest person's id: ", list[len(list) - 1]["id"])
    return list

newList = generateList(amount)
orderedList = orderList(newList)
