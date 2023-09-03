

str = "Pratik, Prajwal, Pranit"
value = 0
while value < len(str):
    if (str[value] == "P"):
        print(str[value])
    value=value+1
print("Out from the loop")

Dict = {"name":"pratik", "age":"26", "role":"QA", "expertise":"automation testing"}
for key,value in Dict.items():
    print(key, ":", value)

for key,value in Dict.items():
    print(key)

