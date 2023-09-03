# =================================Class and object==============================
class EmployeeDetails:
    def __init__(self, FirstName, LastName, Role):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Role = Role
    def details(self):
        print("Details:", self.FirstName, self.LastName, self.Role)

class AreaCalculate:
    width=10   # Class variabble
    def __init__(self,length, width):
        self.length=length
        self.width = width   #instace variable
    def Rectangle(self):
        print("Calculate area:", self.length * self.width)
    def perimeter_Ractangle(self):
        print("Perimeter:",(self.length*2)+(self.width * 2))


employeeDetails = EmployeeDetails("Pratik", "Narute", "QA")  # Create object of class
employeeDetails.details()

areaCalculate = AreaCalculate(5,5)  # Create object of class
areaCalculate.Rectangle()
areaCalculate.perimeter_Ractangle()

# =====================================Single Inheritance================================================

class parentClass:
    def __init__(self):
        pass
    def parentMethod(self):
        print("Single: parentMethod")

class childClass(parentClass):
    def __int__(self):
        pass
    def childMethod(self):
        print("Single: childMethod")

child = childClass()
child.parentMethod()
child.childMethod()

# =====================================Multiple Inheritance================================================

class ParentClass1:
    def __int__(self):
        pass
    def paarentMethod1(self):
        print("Multiple: parentMethod1")

class ParentClass2:
    def __int__(self):
        pass
    def parentMethod2(self):
        print("Multiple: ParentMethod2")

class ChildClass(ParentClass1, ParentClass2):
    def __int__(self):
        pass
    def childMethod(self):
        print("Multiple: ChildMethod")

child = ChildClass()
child.paarentMethod1()
child.parentMethod2()
child.childMethod()

# =====================================Multilevel Inheritance================================================

class ParentClass:
    def __int__(self):
        pass
    def parentMethod1(self):
        print("Multilevel Inheritance: parentMethod")

class ChildClass1(ParentClass):
    def __int__(self):
        pass
    def childMethod1(self):
        print("Multilevel Inheritance: childMethod1")

class ChildClass2(ChildClass1):
    def __int__(self):
        pass
    def childMethod2(self):
        print("Multilevel Inheritance: childMethod2")

obj = ChildClass2()
obj.parentMethod1()
obj.childMethod1()
obj.childMethod2()





