## Python DSA Notes
- Starting From The 11-May-2024 we are adding this Repository
- Second Chance to get it resolved this addition of repos

**Python OOPs Concepts:**
- Class
  - Group of Objects or Same kind of items storing in a single place is called Class
- Objects
  - Instance of a Class is called an Objects
- Inheritance
  - taking characteristics and attributes is called an Inheritance
- Abstraction
- Polymorphism
- Encapsulation

**What is DSA:**
- *Data Structures :*
  - Study of methods for storing and organizing the data in a formal structure is called Data Structuring
  - DS are the essential components that help organize and store data efficiently in computer memory

The run time can be dependent on multiple factors:
- Machine Dependent
- Language Specific
- Based on the operating system

- *Managing the DS :* `There are 4 types in Managing the data`
  - Insertion
  - Deletion
  - Updation
  - Accessing

- *Types of Data Strucures :*
  - Arrays
  - LinkedList
  - Stacks
  - Queues
  - Trees
  - Graphs
  - Hash
  - Graph
  - String

- **Algorithims:**
  - When we use some sequence of steps to organize and storing the data is called Algorithims
  - set of rules to obtain the expected output from the given input
  - managing the data structures with a sequene of Stepa is called the Algorithims

## Data Structures:

- **Arrays**
    - `Array is a Linear Data Structure stores a collection of elements of the same data type`
    - `Elements are allocated in a contiguous location`
    - `Each Element has unique index`
    - `Allowing for constant time access`
  - **Operations on Arrays**
    - Traversal: Iterating over all elements in an array
    - Insertion: Adding or Updating an element at specific index
    - Deletion: Removing an Element from an array by using an index
    - Searching: Finding an Element in an array by its value or index
  - **Types of Arrays**
    - One Dimensional Array
    - Multi-Dimensional Array
  - **Applications of Arrays**
    - Storing data in a Sequential Manner
    - Implementing queues,stacks and other data structures
    - Representing Matrices and tables
- **Strings**
    - `String is a sequence of characters, Typically used to represent text.`
    - `String is used for manipulating and processing of data in computer programs`
  - **Operations on String**
    - Concatenation: `Joining two strings together.`
    - Comparison: `Comparing two strings lexicographically.`
    - Substring extraction: `Extracting a substring from a string.`
    - Search: `Searching for a substring within a string.`
    - Modification: `Changing or replacing characters within a string.`
  - **Applications of String**
    - Text Processsing
    - Data Validation
    - Data Manipulation
    - Pattern Matching
    - Data Base Management

## What is Time Complexity:
*- A function that gives the relationship about time taken as the input grows.*

### Asymptotic Analysis
- No dependency in machine,programming language,CPU Cycles etc..
- We Do not have to implement all the ideas/algorithims
- Asymptotic Analysis is measusing the order of growth in the form of input sizes.
- Analysis of algorithms is the determination of the amount of time and space resources required to execute it.

## What is Space Complexity
- Extra space required or taken of an algorithim is taking

***Reverse String***
```
for i in range(10):
  for j in range(i):
    print(i,end=" ")
```

##### Day-01
**Greatest Common Divisors**
```
def gcd(a,b):
    if a == 0:
      return b
    return gcd(b%a,a)
```

### Big O Notation
1: What is meant by Big O notation
- The upper bound of the complexity of the program should not exceed the O(N^3)
### Big Omega Notation
1: What is Big Omega Notation
- It will require minimum n3 as lower bound for a program
### Theta Notation
1: What is theta notation
- Combining The both Omega and Big O Notations

Little Notation

Little Omega notation
- Loosely Bound of O(N^3)


Order of Growth:
Direct Way to find the order of growth:
- Ingore the Constant terms
- ignore lower order pf growth

How do compare the order of growth:
- c < log(logn) < log n < n^1/3 < n^1/2 < n < n^2 < n^3 < n^4 < 2^n < n^n
Time Taken --> Increasing order.      Order of Growth


