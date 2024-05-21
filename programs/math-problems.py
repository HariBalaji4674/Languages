# Extraction of numbers
from cmath import log, log10
'''

n = 1234
print(type(n))
out = 0
while n > 0:
  rem = n%10
  print(rem)
  out = out+1
  n = n//10
print(out)

print(n/10)
print(n//10)

# print(log10(n))
'''
# Reverse a Given Number
number = 1234
out = 0
while number > 0:
  rem = number % 10
  out = out*10 + rem
  number = number//10

print(out)

# Palindrome or Not

number = int(input("Please enter your palindrome check number: "))

temp = number
out = 0
while number >0:
  rem = number % 10
  out = out*10 + rem
  number = number //10

if out == temp:
  print("This is Palindrome Number")
else:
  print("This is not palindrome number")

# Armstrong Number:
number = int(input("Please Enter Armstrong Number: "))
out = 0
temp = number
while number > 0:
  rem = number % 10
  out = out + rem * rem * rem
  number = number // 10

if out == temp:
  print(f"{out} is an armstrong number")
else:
  print(f"{out} is not an armstrong number")

  # No of Divisors

number  =  36
for i in range(1,number+1):
  if number % i == 0:
    print(i,end=" ")
  else:
    continue