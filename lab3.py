#Functions
def my_function():
    print("Hello from a function")

def my_function():
    print("Hello from a function")
my_function()

def my_function(fname,lname):
    print(fname)

def my_function(x):
    return x + 5

def my_fucntion(*kids):
    print("The youngest child is" + kids[2])

def my_function(**kid):
    print("His last name is " + kid["lname"])

#Lambda
    
x = lambda a : a

#Classes

class Myclass:
    x = 5

class Myclass:
    x = 5
p1=Myclass()

class Myclass:
    x = 5
p1=Myclass()
print(p1.x)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
#Inheritance
class Student(Person):
    
class Person:
    def __init__(self,fname):
        self.firstname=fname
    def printname(self):
        print(self.firstname)
    
class Student(Person):
    pass

x=Student("Mike")
x.printname()
        
