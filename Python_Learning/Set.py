Set = {1,2,"3",4,4}
print(type(Set))
print("Eliminate duplicate value from set:", Set)
print("Length of set:", len(Set))
Set.add(5)
print("After add:",Set)
Set.remove(5)
print("After remove:",Set)

Set1 = {"Pratik", "Shubham"}
Set2 = {"Prajwal", "Shubham"}
print("Different values from set:", Set1.difference(Set2))
print("Different values from set:", Set2.difference(Set1))
Set3 = Set1.union(Set2) # Need to create another variable
print("Join two set:", Set3)

Set1.update(Set2)  # No-Need to create another variable
print("Update set:", Set1)