list = [30,60,40]

list1 = sum(list)
n = len(list)
print(n,list1, list1/n)
addition = 0
count = 0
for i in range(n):
    # print(list[i],end=" ")
    addition = addition + list[i]
    count = count + 1
    
print(addition,count,round(addition/count))

print(list1,n,list1/n)


'''
sum or even
'''

list = [40,37,77,44,12,67,88,90]
evenList = []
oddList = []

for i in list:
    if i%2 == 0:
        evenList.append(i)
        # print(i,end=" ")
    else:
        oddList.append(i)

print(evenList)
print(oddList)


'Joining lists'
'Extends List'
'Append List'

list1 = [10,20,30,40,50,60,70,80,90,100]
list2 = [11,21,31,41,51,61,71,81,91,101]

list1.extend(list2)
print(list1)
print()
print()

for i in range(10):
    print(i)

for i in range():
    print()
def mester





