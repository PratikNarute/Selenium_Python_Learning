"""
zip() [It is use for map the same index of first list to same index of another list]
range() [It generate the sequence of number, It takes three types of argument (start, end-1, step)]
max() [It find the max value from variables]
min() [It find the min value from variable]
iter() [It return the iterator values]
next() [Return the next value in iterable]
reversed() [Return the reverse value in iterable]
slice() [It is used to cut the specific values]
sorted() [sorting in ascending order]
sum() [It sum of all values from object]
input() [It take user input]
"""

# zip()
costItem = [100,200,300,500]
saleCostItem = [110,250,305,490]
for x,y in zip(costItem, saleCostItem):
    print("Find profit by zip function:", y-x)

# range()
for x in range(1,4,1):
    print("Range:",x)

# max()
tup = (30,55,19)
print("Find max value by max():",max(tup))

# min()
print("Find min value by min()", min(tup))

# iter()
i=iter(tup)
j=reversed(tup)
print("Next value from iterable:", next(i))
print("Next value from iterable:", next(i))
print("Next value from iterable:", next(i))
print("Reverse value from iterable:", next(j))
print("Reverse value from iterable:", next(j))
print("Reverse value from iterable:", next(j))

# slice()
name="Pratik Pandurang Narute"
Slice=slice(7,16)
print("slice:",name[Slice])

# sorted()
print("Sorted:", sorted(tup))

# sum()
print("Sum:",sum(tup))

# input()
Input = input("Enter your name: ")
print("Welcome:",Input)