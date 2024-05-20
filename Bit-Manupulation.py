# Lambda Function in Python
a = lambda a,b:a+b
print(a(4,5))

def add(x,y):
  return x+y
print(add(4,5))

x = lambda x,y : x+y
print(x(10,20))

def firstMethod(sum,diff):
  print("This is main progarm to be called to develop")
  print(sum,diff)
  secondMethod(25,46)


def secondMethod(high,low):
  print("This is second method")
  print(high+low)

firstMethod(67,33)