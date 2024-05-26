from ast import main
from numpy import swapaxes


array_def = [1,2,3,4,5]
rev_arr = array_def[::-1]
print(rev_arr)

# Array reversing using another array
def reve_arr(arr):
    rever_arr = arr[::-1]
    print("reverse order : ",end=" ")
    for i in rever_arr:
        print(i,end=" ")

reve_arr(rev_arr)

print("")

# Array Reversing using inbuild function
main_array = [3,4,6,7,9]
print(main_array[::-1])
n = len(main_array)
for i in range(n):
  # main_array[i] = main_array[n-i-1]
  # main_array = main_array.append(n-i-1)
  print(main_array[i])







