list = [1,2,3,4]
print(type(list))

# Methods in list
list.append(5)  # add at the end index
print("After Append:",list)
list.insert(5, 6)  # Add at the particular index
list.insert(0, 0)
print("Insert:",list)
list.remove(0)  # It will remove first and only one value from list
print("After removing:", list)
list.pop(5)  # It will remove value from particular index
print("After pop:", list)
print("Get index of value:", list.index(5))
list.reverse()
print("After reverse", list)

list = [3,5,1]
list.sort()
print("After sorting:", list)
listCopy = list.copy()
print("After copy:", list)
listCopy.clear()
print("Clear list:", listCopy)  # Clear all values from list