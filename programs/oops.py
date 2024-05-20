# OOPs Concepts:
# Attributes : Variables
# behaviour : Methods/Functions
# Methods
# Class :---> Design & BluePrint of an object
# Object :---> Instance of a Class
#

class computer:
  def config(self):
    print("Lenovo","16gb","512GB","i7")

obj1 = computer()
obj2 = computer()
#  calling the function/method in class below both are same
obj1.config() # computer.config(obj1)

obj2.config() # computer.config(obj2)

# __init__ method (special methods)
# it will be called automatically

class initmethod:
  def __init__(self,name,age,number):
    self.name = name
    self.age = age
    self.number = number
    # print(name,age,number)
  def callMethod(self):
    print("The configurations are ",self.name,self.age,self.number)

obj1 = initmethod('peddireddy',24,2068)
obj1.callMethod()

# Constructor / Self method
# size of an object withh eb based on the no of variables used and size of a Variable
# who allocated the memroy to the variables --> construtor

class selfMethod:
  def __init__(self,name,age,number):
    self.name = name
    self.age = age
    self.number = number
  def update(self):
    self.age = 30

c1 = selfMethod('peddireddy',24,2048)
c1.update()
# print(c1.update())
print(c1.age)

class classMethods:
  def __init__(self,name,age,number,course):
    self.name = name
    self.age = age
    self.number = number
    self.course = course
  def method1(self,name,age,number,course):
    print(self.name,self.age,self.number,self.course)

  def method2(self):
    pass

object1 = classMethods('peddireddy',24,2048,'DevOps')
object1.method1('hari',25,2064,'python-dev')

# Compare method

class computer:
  def __init__(self,age,number):
    self.age = age
    self.number = number
  def compare(self,other):
    if self.age == other.age:
      return True
    else:
      return False
c1 = computer(24,56)
c1.age = 30
c2 = computer(30,67)
if c1.compare(c2):
  print('These Values are same')
else:
  print("Sorry the values are not same")

class methodsD:
  school = 'teluskoo'
  def __init__(self,m1,m2,m3):
    self.m1 = m1
    self.m2 = m2
    self.m3 = m3
  def avg(self):
    return (self.m1+self.m2+self.m3)/3
  @classmethod
  def infor(cls):
    return cls.school


c1 = methodsD(34,56,92)
c2 = methodsD(90,45,89)
print(c1.avg())
print(c2.avg())
print(methodsD.infor())


# Static methods
# Class methods
# Instnace methods
class methods:
  @staticmethod
  def staticMethod():
    print("Hello This is static method")
  @classmethod
  def classMethod(cls):
    print("This is class method")
  def mainMethod(self):
    print("This is main method")

c1 = methods()
c1.classMethod()
c1.mainMethod()
c1.staticMethod()


# Inner Class

class one:
  def __init__(self):
    print("Peddireddy")
  class two:
    def __init__(self):
      print("Hari Vardhan Reddy")

class student:
  def __init__(self,name,year,age):
    self.name = name
    self.year = year
    self.age = age
    self.lap = self.Laptop('MacBook',4,2022)
  def show(self):
    print(self.name,self.age,self.year,self.lap.brand)
  class Laptop:
    def __init__(self,brand,cpu,model):
      self.brand = brand
      self.cpu = cpu
      self.model = model

obj1 = student('peddiredy',24,2024)
obj1.show()
# Inheritance & Taking attributes and behaviours form parents

class a:
  def __init__(self):
    print("This is first class init method")
  def one(self):
    print("This is method 1")
  def two(self):
    print("This is method 2")

class b(a):
  def __init__(self):
    # super().__init__()
    print("This is second class init method")
  def three(self):
    print("This is method 3")
  def four(self):
    print("This is method 4")

# class c(a,b):
  def __init__(self):
    # super().__init__()
    print("This is third class init method")
  def fifth(self):
    print("This is method 5")
  def sixth(self):
    print("This is sixth method")

obj2 = c()
obj2.fifth()

obj1 = b()
obj1.one()
obj1.two()
obj1.three()
obj1.four()

# Polymorphisim poly many morph forms

# There are four type of Polymorhphism
# 1: Ducktyping
# 2: Method Overloading
# 3: Method Overloading
# 4: Operator Overloading

# Ducktyping means class dependent

# class myEditor:
#   def intro(self):
#     print("Compiling")
#     print("Running")
# class myInduction:
#   def implement(self,oldEditor):
#     oldEditor.myEditor()

# # obj2 =
# obj1 = myEditor()
# obj1.intro()

str.__add__('peddireddy','hari')

# Method Overloading
# Method OverRiding
