"""
Author: Bill Li
Date: 21/04/2019
Purpose: Testing
Topic: Sorted()
"""

# List
x = ['q', 'w', 'r', 'e', 't', 'y']
print("List:", sorted(x))

# Tuple
x = ('q', 'w', 'e', 'r', 't', 'y')
print("Tuple:", sorted(x))

# String (Sorted based on ASCII)
x = "python"
print("String:", sorted(x))

# Dictionary
x = {'q':1, 'w':2, 'e':3, 'r':4, 't':5, 'y':6}
print("Dictionary:",sorted(x))

# Set (Set content is immutable, Set is mutable)
x = {'q', 'w', 'e', 'r', 't', 'y'}
print("Set:", sorted(x))

# Frozen Set (Set content and Set are immutable)
x = frozenset(('q', 'w', 'e', 'r', 't', 'y'))
print("Frozen Set:", sorted(x))

# Problem 1030 LeetCode
cells = [[x, y] for x in range(10) for y in range(10)]
print("board:\n", cells)
print("", sorted(cells, key=lambda cell: abs(cell[0] - 0) + abs(cell[1] - 0)))