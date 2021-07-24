# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:31:38 2021

@author: 100431522
"""
# NOTES;
"""For variables and functions in Python use "Snake Case": 
where all lowercase letters are used with underscores between: like_this.
With classes, the convention is to use "Pascal Case", where no 
underscores are used between words, and the first letter of each 
word is capitalized: LikeThis."""

"""
An object is an entity that stores data.
An object's class defines specific properties objects of that class will have.
"""
"""
The calendar module
The time module
The datetime module
"""
"""
The datetime module contains a number of classes, including:
datetime.datetime: For working with date and time data.
datetime.time: For working with time data only.
datetime.timedelta: For representing time periods.
"""
"""
Internally Python will use one of three encodings to store strings in memory:
1 byte per character (Latin-1 encoding)
2 bytes per character (UCS-2 encoding)
4 bytes per character (UCS-4 encoding)
"""
"""
The overhead of variable-length encoding changes depending on the contents
 of the string but it will be a value between 49 and 80 bytes. 
"""
# To avoid space-taking characters in a text
""""
message = " text with characters we want to avoid like emoji"
message_latin_bytes = message.encode(encoding = 'Latin-1', errors = 'ignore')
cleaned_message = bytes.decode(message_latin_bytes, encoding = 'Latin-1')
"""
"""
A UTF-32 is a fixed-size 4-byte encoding whereas UTF-8 is a variable length
 encoding using from 1 to 4 bytes
"""

"""
The logarithmic time complexity is much faster than linear time algorithms 
but is not constant time algorithms. Its complexity lies between constant time
 complexity and linear time complexity.
"""
def binary_search(values, target):                     # First change
    range_start = 0
    range_end = len(values) - 1                        # Second change
    while range_start < range_end:
        range_middle = (range_end + range_start) // 2
        value = values[range_middle]                   # Third change
        if value == target:
            return range_middle
        elif value < target:
            range_start = range_middle + 1
        else:
            range_end = range_middle - 1
    # Add your code here
    if values[range_start] != target:
        return -1
    return range_start

values = [1, 2, 4, 5, 8, 10, 13, 15, 17, 20, 23, 24, 25, 26, 30, 31, 32, 36,
          37, 38, 41, 42, 43, 44, 45, 47, 50, 52, 54, 55, 56, 57, 58, 59, 61,
          62, 64, 66, 67, 69, 70, 73, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85,
          86, 87, 90, 91, 92, 94, 95, 96, 97, 98, 99, 100]

binary_search(values, 3)
"""
the number of times we need to divide N by 2 to reach 1.
 In mathematics, this value is called the base-2 logarithm of N and is denoted
 by log2(N). Base 2 because we are dividing by 2. We could ask the more general
 question of the number of times we need to divide N by b to reach 1.
 This is known as the base-b logarithm of N and is denoted by logb(N).
 That is, 2^k = N,  k = log_b(N)
 Adding these together, we conclude that the binary_search() function 
 has O(log(N)) time complexity. This is called logarithmic time complexity.
 When working with time complexities, we usually omit the base of the
 logarithms writing log instead of log2 , to lighten the notation.

Logarithmic time complexities usually arise form algorithms that are able to reduce the search space by some fraction at each iteration. In this example, we could eliminate half of it at each step. These algorithms are extremely fast and should be used whenever applicable.
"""
# Sorting Algorithm
"""
def swap(values, i, j):
    temp = values[i]
    values[i] = values[j]
    values[j] = temp

def select_minimum_index_in_range(values, range_start):
    minimum = None
    minimum_index = None
    N = len(values)
    for i in range(range_start, N):
        if minimum == None or values[i] < minimum:
            minimum = values[i]
            minimum_index = i
    return minimum_index

values = [5, 4, 6, 1, 3, 2]

def selection_sort(value_list):
    N = len(value_list)
    for range_start in range(N):
        index = select_minimum_index_in_range(value_list, range_start)
        swap(value_list, range_start, index)
    return value_list
# check sorting code
print(selection_sort(values))
"""
"""Python is able to sort list very quickly in O(N log(N))."""
# Space Complexity
"""
-Space Complexity is the way memory consumption changes as a function of the
 amount of data given as input to the algorithm.
- If an algorithm allocates N integers (of 32 or 64 bits), we say that it has
 space complexity O(N), ignoring the exact number of bits. we assume that a
 single numeric value uses a constant amount of memory, O(1).
 - The space complexity of a Python object amounts to counting the number of 
 values (numeric values, characters, and variable references) that it stores.
 In this sense, a string with N characters will contribute O(N) to the space
 complexity, as will a list with N integers.
 - A computer has two memory systems. The primary memory, also known as RAM 
 (random access memory), is a very fast memory used to store temporary values.
- The secondary memory is the hard drive. This memory is much slower than 
the RAM but has a lot more capacity. 
- Numeric values, characters, and references to variables are the three 
basic types of data that we store in a Python program.
 All of these have space complexity O(1).
 -When analyzing an algorithm, we do not include the space complexity of the
 input (arguments) in our model. We only account for the memory allocated 
 by the algorithm itself.
-Preprocessing some of the input of an algorithm into a more suitable data
 structure is often a solution to improve the time complexity of an algorithm.
e.g preprocess a list and transform it into a set for checking "belonging"   
"""