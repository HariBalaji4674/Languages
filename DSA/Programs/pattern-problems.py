#Pattern problems
#1  Square Pattern
# Outer Loop Represents the rows
# Inner Loop Represents the Columns

# Improve Though process

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


# Tricks
# 1: How to Appproach
# Every rows(outer loop) and columns(inner loop)
'''
no of lines == no of rows
no of columns == no of elements added

'''
n =5
for i in range(n):
  for j in range(i+1):
    print(i,end=" ")
  print()

