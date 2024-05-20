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

