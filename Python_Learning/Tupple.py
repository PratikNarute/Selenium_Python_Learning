Tupple = (1,2,3,2)
print("Type of class:",type(Tupple))

'''
It has indexes
It allow duplicate values
It is immutable(not-changable) in nature [we cannot use append and remove methods here]
'''

# Methods use in tupple
print("Length of tuple:",len(Tupple))
print("count of values:", Tupple.count(2))
print("index of value:", Tupple.index(1))

for x in Tupple:
    print(x)

Tupple1 = ("Pratik", "Shubham", "Prajwal")
Tupple2 = ("Narute", "Savne", "Narute")

Tupple3 = Tupple1+Tupple2
print("Join two tupple:",Tupple3)
