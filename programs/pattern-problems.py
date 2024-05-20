#Pattern problems
#1  Square Pattern
# Outer Loop Represents the rows || no of lines == no of rows
# Inner Loop Represents the Columns

# Improve Thought process


for i in range(4):
  for j in range(4):
    print(i,end=" ")
  print()

#2
'''
* * * * *
* * * *
* * *
* *
*
'''

n =5
for i in range(n):
  for j in range(i+1):
    print(i,end=" ")
  print()

'''
* * * * *
* * * *
* * *
* *
*
'''

print("This is reverse array")

n = 5
for i in range(n,0,-1):
  for j in range(i):
    print(i,end=" ")
  print()

#1 Increasing Traingle
#2 Decreasing Traingle
#3 Right Sided Traingle

for i in range(n):
  for j in range(i):
    print('*',end=" ")
  print()

for i in range(n):
  for j in range(i,n):
    print("*",end=" ")
  print()

for i in range(n):
  for j in range(i,n):
    print(" ",end=" ")
  for j in range(i+1):
    print("*",end=" ")
  print()

for i in range(n):
  for j in range(i+1):
    print(" ",end=" ")
  for j in range(i,n):
    print("*",end=" ")
  print()

# Increasing means = i+1
# Decreasing Means = i,n

for i in range(n-1):
  for j in range(i,n):
    print(" ",end=" ")
  for j in range(i+1):
    print("*",end=" ")
  for j in range(i):
    print("*",end=" ")
  print()
for i in range(n):
  for j in range(i+1):
    print(" ",end=" ")
  for j in range(i,n):
    print("*",end=" ")
  for j in range(i,n-1):
    print("*",end=" ")
  print()

k=0
for i in range(n):
  for j in range(i+1):
    print(k,end=" ")
    k+=1
  print()
for i in range(n):
  for j in range(i,n-1):
    print(k,end=" ")
  print()

for i in range(n):
  if i%2 == 0:
    start = 1
  else:
    start = 0
  for j in range(i+1):
    print(start,end=" ")
    start = 1-start
  print()

n = 10
m = 0
for i in range(n):
  for j in range(i):
    print(format(m,">3"),end=" ")
    m = m+1
  print()

name = "Peddireddy Hari {:<10} Reddy"
print(name.format("vardhan"))

for i in range(n):
  for j in range(i+1):
    print(j,end=" ")
  print()

for i in range(n):
  for j in range(i+1):
    print(m,end=" ")
  print()


def pattern(n):
  for i in range(n):
    for j in range(i,n):
      print(j,end=" ")
    print()
def pattern(n):
  for i in range(n):
    print(i,end=" ")

pattern(5)

print("*********************")


for i in range(5):
  for j in range(i,n):
    print(" ",end=" ")
  for j in range(i+1):
    print("*",end=" ")
  for j in range(i):
    print(i,end= " ")
  print()

for i in range(n):
  for j in range(n-i-1):
    print("*",end=" ")
  print()
for i in range(n):
  for j in range(i,n-1):
    print("*",end=" ")
  print()

n = 5
for i in range(n):
  for j in range(i,n):
    print(" ",end=" ")
  for j in range(i+1):
    print("*",end=" ")
  for j in range(i+1):
    print(i,end=" ")
  print()
m = 0
for i in range(n):
  for j in range(i+1):
    print(" ",end=" ")
  for j in range(n,0,-1):
    print(j,end=" ")
  for j in range(i,n):
    print(m,end=" ")
    m = m+1
  print()


# for i in range(start,end,increment)

for i in range(5,0,-1):
  print(i,end=" ")


# Pattern Problems Conditions are :
# n-i-1  for no of linto be filled with spaces
# i+1 to increase the count
# i,n to decrease the count

# Python String Formatting

print()
price = 20
txt = f"The price is {95:.2f}"
txt = f"I am adding {20+40}"
print(txt)

name = 'peddireddy hari vardhan reddy'
print(f"i love my name {(name.upper())}")

def even(number):
  return number*20.4

answer = f"I am collecting the value of list{even(200)}"
print(answer)
print(even(10))


# String Formatting Problems
name = 'peddireddy'
age = 24
year = 2024

deatils = "My Name is {0} and my age is {1} the year is {2}"
print(deatils.format(name,age,year))