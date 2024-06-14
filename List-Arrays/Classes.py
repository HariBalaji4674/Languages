class Objects:
    def main(self):
        print("Peddireddy")

obj1 = Objects()
obj1.main()

class StarCookie: # Pascal Case Class Name
    def __init__(self):
        print("This is a cookie class")

star_cookies = StarCookie()
star_cookies.name = "Hari Vardhan Reddy"
star_cookies.age  = 24
star_cookies.sleep = True

print(star_cookies.name,star_cookies.age,star_cookies.sleep)
star_cookies1 = StarCookie()
star_cookies1.name = "Aliens"
star_cookies1.age  = 28
star_cookies1.sleep = False

print(star_cookies1.name,star_cookies1.age,star_cookies1.sleep)

class SecClass:
    def __init__(self,color,shape,area):
        self.color = color
        self.shape = shape
        self.area = area
        print(color,shape,area)
    def main(self):
        print("Calling Main Method")

secObect = SecClass('red','circle','high')
secObect.main()
        
class oops:
    science = 45
    social = 48
    history = 47
    def marks(self,science,social,history):
        self.science = science
        self.social = social
        self.history = history
        # science = oops.science
        # social = oops.social
        # history = oops.history
# obj = oops(45,89,98)
print(oops.science)
print(obj.marks())

    



"""

Without class we cannot create a Objects
Class Components: Name,Attributes, Behaviour

Method : 

Class Name
Attributes
Methods/Behaviours

Instantiation

Objects: Instances
Creating Objects: Instantiation

Our Own Class: 

Init funtion will call automatically without calling

"""