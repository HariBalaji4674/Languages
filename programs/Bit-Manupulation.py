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

# Swapping Two Numbers without third variable
a = 10
b = 9
10 == 1010
9 == 1001

print(a^b)

a = 4
print(a << 2)

b = 5
print( b >> 3)

# Check The ith bit

def decimalToBinary(num):
  if num > 1:
    decimalToBinary(num // 2)
  print(num%2,end=" ")

decimalToBinary(14)

print()

number = 14
i = 3
if number & (1 << i) != 0:
  print(f"This number is set at {i}th place")
else:
  print("This is not set")
