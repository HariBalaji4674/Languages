# Date: 11-May-2024

## Time and Space Complexities

### What is Time Complexity:
- Rate at which time taken increases with respect to the input size is called Time Complexities
- Time complexity is not equal to time taken
- Time complexity is not dependent on time taken

### Big O Notation O()
- Time Complexities should be measured always with respect to worst case scenario
- Avoid Constant Terms
- Avoid Lower Terms

### Space Complexity
- order of growth of memory or ram usage in terms of input

Auxiliary Space:
- Order of growth of extra space
- Space other than input and output
- Big O(n)- Auxiliary
- Theta 0(1)

Analysis of Recursion:
- Recursive Tree Method
  - We write Non-recursive
  - geometric progression
  - arithematic progression
  - lograthims

### What is recursion:
- repeatedly calling one function multiple times is called recusion function

### Space Complexity:

```
The term Space Complexity is misused for Auxiliary Space at many places. Following are the correct definitions of Auxiliary Space and Space Complexity.

Auxiliary Space is the extra space or temporary space used by an algorithm.

The space Complexity of an algorithm is the total space taken by the algorithm with respect to the input size. Space complexity includes both Auxiliary space and space used by input.

For example, if we want to compare standard sorting algorithms on the basis of space, then Auxiliary Space would be a better criterion than Space Complexity. Merge Sort uses O(n) auxiliary space, Insertion sort, and Heap Sort use O(1) auxiliary space. The space complexity of all these sorting algorithms is O(n) though.

Space complexity is a parallel concept to time complexity. If we need to create an array of size n, this will require O(n) space. If we create a two-dimensional array of size n*n, this will require O(n2) space.

In recursive calls stack space also counts. ```