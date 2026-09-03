"""
- sort() method is generally faster since it sorts in place, but sorted() should
be used if you need a new list

- sort() and sorted() both have O(n log n) time complexity (logarithmic time)
"""

# Initializing a list
a = [5, 1, 5, 6]

# Sort modifies the given list
a.sort()
print(a)

b = [5, 2, 9, 6]

# Sorted does not modify the given list
# and returns a different sorted list
bs = sorted(b)
print(b)
print(bs)

# Initializing a list
a = [5, 2, 9, 1, 5, 6]

# Sorting the list in ascending order
a.sort()
print("Sorted list (ascending):", a)

a.sort(reverse=True)
print("Sorted list (descending):", a)

# Initializing a list
a = [5, 2, 9, 1, 5, 6]

# Sorting the list in descending order
sa = sorted(a)
print("Sorted list (ascending):", sa)

sa = sorted(a, reverse=True)
print("Sorted list (descending):", sa)

"""
Python sorted() function returns a sorted list. It is not only defined for the list and it accepts any iterable (list, tuple, string, etc.). It does not modify the given container and returns a sorted version of it.

We can sort other containers:
tuple: sorted() function converts tuple into sorted list of elements

Sorting a set: Since sets are unordered, sorted() converts the set into a sorted list of its elements.

Sorting a string: This will sort the characters in the string and return a list of the sorted characters.

Sorting a dictionary: When a dictionary is passed to sorted(), it sorts the dictionary by its keys and returns a list of the keys in sorted order.

Sorting a list of tuples: The list of tuples is sorted primarily by the first element of each tuple, and secondarily by the second element if the first ones are identical.
"""

# Sorting a tuple
a = (10, 12, 5, 1)
print(sorted(a))
# > [1, 5, 10, 12]

# Sorting a set
s = {'gfg', 'course', 'python'}
print(sorted(s))
# > ['course', 'gfg', 'python']

# Sorting a string
st = 'gfg'
print(sorted(st))
# > ['f', 'g', 'g']

# Attempting to sort a dictionary (it will sort the keys)
d = {10: 'gfg', 15: 'ide', 5: 'course'}
print(sorted(d))
# > [5, 10, 15]

# Sorting a list of tuples
l = [(10, 15), (1, 8), (2, 3)]
print(sorted(l))
# > [(1, 8), (2, 3), (10, 15)]

"""
Sorting User Defined Objects
"""
# Example 1: Using a Separate Method

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def myFun(p):
    return p.x

l = [Point(1, 15), Point(10, 5), Point(3, 8)]
l.sort(key=myFun)

for i in l:
    print(i.x, i.y)

# Example 2: Using a __lt__ Method
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x

l = [Point(1, 15), Point(10, 5), Point(3, 8)]
l.sort()

for i in l:
    print(i.x, i.y)

# Example 3: Sorting with Custom Criteria
a = [1, -5, 10, 6, 3, -4, -9]

# Sorting by absolute values in descending order
sa = sorted(a, key=abs, reverse=True)
print("Sorted by absolute values:", sa)

# Example 4: Custom Sorting with Lambda Functions
# List of tuples
a = [(1, 'one'), (3, 'three'), (2, 'two')]

# Sorting by the second element of each tuple
sa = sorted(a, key=lambda x: x[1])
print("Sorted by second element:", sa)

