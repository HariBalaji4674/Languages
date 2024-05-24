### Bit Manupulation
#### AND OR XOR SHIFT NOT
- *AND* --> All True
  - 1 False --> False
- *OR* --> 1 True === True
  - all False == False
- *XOR* --> no of 1s ==> odd ==> 1
  - no of 1s ==> even ==> 0
- Shift Operator
  - Left Shift Shifting one bits left
  - Right Shift
- Largest Number

# Swap The numbers:


# Check if the ith bit set or not
  - First Write Binary Format
  - Do 1 left shift ith bit
  - then do and(&) operation
  - if (N & (1 << ith bit) != 0) print the number is set
  - else not set