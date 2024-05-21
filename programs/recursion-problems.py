# Recursion Patterns
# DBMS, DSA, System Design, Design Patterns

# Summation of first n natural numbers
# Methods
# Parameterized way
# Functional Way

def main():
  recursive()
  print("This is main method")

def recursive():
  print("This is recursive method")

main()
num = 0
while num <= 10:
  print(f"Hello World {num}")
  num = num + 1

# Recursive Functions
# Sum of n numbers

# num = 10

def sum_Of_N_Numbers(num):
  if num == 0:
    return 0
  else:
    return num + sum_Of_N_Numbers(num-1)

print(sum_Of_N_Numbers(5))
print(sum_Of_N_Numbers(10))
print(sum_Of_N_Numbers(15))


# Multiplication of N numbers
def multiply(num):
  if num == 0:
    return 1
  else:
    return num * multiply(num-1)

print(multiply(5))
print(multiply(10))
print(multiply(15))

# Reverse an Array
list = [1,2,5,7,8,4,3]
print(list[1])
n = len(list)
for i in range(n-1,0,-1):
  print(list[i])


# print Gfg for 5 times

def function(n):
  if n <= 0:
    return
  print("GFG")
  function(n-1)
function(5)

#Factorial Number

def fact(n):
  if (n <= 0):
    return 1
  return n*fact(n-1)

print(fact(5))
print(fact(-5))

# Fibonacci Series
# 0 1 1 2 3 5 8 13 21 34 55

# Using Recursion
def fib(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fib(n-1)+fib(n-2)
print(fib(5))

def fibonacci(n):
  if n < 0:
    print("Please Enter correct Number")
  elif n == 0 :
    return 0
  elif n == 1 or n == 2:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))

# Native Approach

num1 = 0
num2 = 1

num3 = num2

count = 1
while count <= 10:
  print(num3,end = " ")
  count = count+1
  num1 = num2
  num2 = num3
  num3 = num1+num2
print()

