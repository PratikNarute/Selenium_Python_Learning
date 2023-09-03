'''
Operators
    Arthimatical
    Assignament
    Comparision
    Logical
    Identity
    Membership
    Bitwise
'''

# Arthimatical operator
x=5
y=10

print("addition: ",x+y)
print("Substraction: ",x-y)
print("Multiplication: ",x*y)
print("Divider: ",x/y)
print("Round divider:",x//y)
print("remider: ",x%y)
print("Exponetial:",x**y)


# Assignament Operator (=)
x=10
y=x
print("Assignment operator:",y)

# Comparision operator
x=10
y=20
print("Equal to:",x==y)
print("Not equal to:",x!=y)
print("Less than:",x<y)
print("Greater than:",x>y)
print("Less than or equal to:",x<=y)
print("Greater than or equal to:",x>=y)

# Logical operator
x=10
y=20

print("And operator:",x==y and x<y)
print("Or operator:",x==y or x<y)

# Identity operator (it show the assigned memory by objects
x=["Number","10"]
y=["Number","10"]
p=10
q=10
print("Identity:", x is y)  # x and y object take seperate memory
print("Identity:", p is q)  # p and q variable take same memory because the values are same


# Membership operator
p = "Pratik Pandurang Narute"
print("Membership operater:", "Pratik " in p)
print("Membership operater:", "Pratik " not in p)