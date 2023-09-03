"""
types of arguments
Positional
Keyword
required
positional

"""

def Positional(x,y):
    print("Positional:",x+y)

def Keyword(x,y):
    print("Keyword:",x+y)

def required(x,y):
    print("required:",x+y)

def optional(x=0,y=0):
    print("optional:",x+y)

# Positional argument
Positional(10,10)

# Keyword argument
Keyword(x=10,y=20)

# Required argument
required(10,10)

# optional argument
optional()

