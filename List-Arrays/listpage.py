import math

list = ["peddireddy",23,24,True,45.6,98.100]
print(list)

list = [10,70,30,80,40,60]
# print(list)
# print(math.sqrt(4))
# print(math.pow(3,10))
# print(math.log(10))

list.reverse()
print(list)

list.sort()
print(list)

n = list.count(10)
print(n)

list1 = list
list.append(list1)
print(list)
list.extend(list1)
print(list)

list.clear
print("removed list",list)

list.copy
print(list)

del list[6:]
print(list)

print(max(list))
print(min(list))




# List Methods

# list.append(list)
# list.sort
# list.reverse
# list.remove(30)
# print(list)
# n = list.count
# print(n)




"""
list is collection of items
Dynamic size
Array Based 
can have same type or different types also
pre allocated some space also in list in python

Array/List in Python : 
- Random Access
- cache friendliness
- linked list / double linked list

How does Dynamic size works?
- the pre allocates some extar space
- it becomes full do teh following
  - allocates a new space of a larger size
  - copy old spce to  new
  -  free old space

Time Complexity of list operations:

- Constant time for Append and pop operations
- Insertion/searching/deletion is costly in list python
- there is a set where used to do acid operations

"""