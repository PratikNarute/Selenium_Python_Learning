

"""
Variable scope in python
local scope [Scope of local var withing same function
global scope [scope global var within same file and class
global keyaword [Global keyword is use to declare lacal var as galobally
LEGB (Local Enclosing Global Build-in) rule
"""

# local scope
def local_scope():
    local=10
    print("Local:" ,local)

local_scope()

# global scope
Global=50
def global_scope1():
    print("Global:" ,Global)
def global_scope2():
    print("Global:" ,Global)

global_scope1()
global_scope2()

# Global keyword
def global_keyword1():
    global globalKeyword
    globalKeyword = 100
    print("Global keyword:" ,globalKeyword)
def global_keyword2():
    print("Global keyword:" ,globalKeyword)
global_keyword1()
global_keyword2()