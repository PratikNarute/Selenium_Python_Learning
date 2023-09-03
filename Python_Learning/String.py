

"""
# Fuctions in String
len() [It return length of string]
str() [It convert into string]
upper() [It convert all letter in upper case]
lower() [It convert all letter in lower case]
count()  [It return count of particualr letter from string]
isUpper() [It return boolean]
isLower()  [It return boolean]
split() [It split the string, and separate white spaces by default and return the index of string array]
lstrip() [It remove first perticualr string from left and by default remove spaces] 
rstrip() [It remove first perticualr string from right and by default remove spaces] 
replace() [It replace old string into new string]
find() [It same to find method but it return -1 exit code when particular char is not available in string]
index() [It return index of string]

"""

fuction = "I start to learn about python"
mobNumber = 8625812214
print("length of string:", len(fuction))
convertedString = str(mobNumber)
print("Convert into string:",type(convertedString))
print("find index of string:",convertedString.find("8"))
print("find Index of string:",convertedString.find("0"))
print("Index of string:",convertedString.index("8"))
print("find char of string:", convertedString[0])
print("Convert into upper case:",fuction.upper())
print("Convert into lower case:",fuction.lower())
print("Convert into capatilize case:",fuction.capitalize())
print("count of string:",convertedString.count("2"))
print("Split white spaces by default:", fuction.split())
print("Split spaces:", fuction.split(" "))
print("replace string:", fuction.replace("I", "We"))

Strip = "       ;''86I start to learn about python"
R_Strip = "I start to learn about python        ;''86"
print("Remove first strings from left by strip method:",Strip.strip())
print("Remove first strings from left by strip method:",Strip.strip(" ;''86"))
print("Remove first strings from right by strip method:",R_Strip.rstrip(" ;''86"))


# Slicing of string
mobNo= "8625812214"
print("Slicing of string:", mobNo[0:10])    # In mobNo[0:10] 0 show index and 10 show size of string
print("Slicing of string:", mobNo[0: len(mobNo): 2])    # In mobNo[0:len(mobNo):2] 0 show index and len(mobNo) show size of string and 2 show interval steps
print("Reverse string by slicing:", mobNo[::-1])

# String formating (concating string)
name = "My name is pratik."
location = " I am from India"

print(name+location)
print("My name is pratik."+location)
print("Hellow, %s %s" %(name, location))
print("Hellow, {} {}".format(name, location))
print("Hellow, {name} {location}".format(name=name, location = " I am from India"))
