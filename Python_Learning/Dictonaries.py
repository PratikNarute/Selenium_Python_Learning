
'''
Value is store in format of keys and values
It is mutable(changeable) in natute
'''
Dict = {"name":"pratik", "age":"26", "role":"QA", "expertise":"automation testing"}
print(Dict)
print("length of dict:", len(Dict))
print("Find value of keys:", Dict["name"])
print("Find value of keys:", Dict["expertise"])
Dict["goal"] = "full stack tester"
print("Add keys:",Dict)

'''
Methods in dictionary
get()  [Get the value of keys]
keys() [Return all keys from dict]
items()  [Get all keys and values pair in tupple formate]
values()   [Return all values from dict]
pop()   [Remove pair by argument as keys]
popitem() [Remove last one pair]
update()  [Add pair into dict]
copy() [copy dict]
clear() [clear all pairs from dict]
'''

print("Get the value of keys:", Dict.get("expertise"))
print("Get the all keys:", Dict.keys())
print("All Items in the formate of tupple:",Dict.items())
print("Get the all Values:", Dict.values())
Dict.pop("goal")
print("After pop out or removing key:", Dict)
Dict.popitem()
print("After popitems of last:", Dict)
Dict.update({"expertise":"automation testing"})
print("Update dict by adding pair:", Dict)
copyDict = Dict.copy()
print("Copy dict:",copyDict)
copyDict.clear()
print("Clear all dict:", copyDict)
