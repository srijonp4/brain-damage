# Arrays are called lists in python

arr = [1, 2, 3]
print(arr)

# STACKS ??
# arrays are dynamic so they can be used as stacks

arr.append(4)  # push O(1)
print(arr)
print(arr.pop())  # pop O(1)
print(arr)
print(arr[-1])  # top functionality # O(1)

# Now some TC Analysis

""" 

1. Appending an element to the end of an array (push operation) using append() has an average time complexity of O(1). This is because Python's lists (arrays) are dynamic arrays, and appending an element to the end typically requires constant time, though occasionally it may require O(n) time if the underlying array needs to be resized.
2. Popping an element from the end of an array (pop operation) using pop() has an average time complexity of O(1) for the same reasons as above.
3. Accessing the top element of the stack (getting the last element of the array) using indexing (arr[-1]) also has a time complexity of O(1), as it directly accesses the last element of the array without needing to iterate through the entire array.

"""

# NOW TO SOME BASICS OF ARRAY
""" arr.insert(1, 7)
print(arr) """  # modifies the arr len pushes all remaining element by 1 position so O(n) TC

""" arr[1] = -7   """  # replaces the curr ele at index O(1) TC
""" print(arr) """

# READING AND RESIGNING A VALUE IS A CONSTANT TIME OPERATION , O(1)

# Initialize arr of size n with default val of 1

new_arr = [0] * 10
print(new_arr)

# indexing
new_arr[9] = -10
print(new_arr[-1])  # last elememt of the arr
print(new_arr[-2])  # second last elememt of the arr

# Now create a array using range

arr = list(range(1, 6))
print(arr)

# SUBLISTS/SUBARRAY or slices of the array
print(arr[2:-1])
# similar to range, the last index is non inclusive
print(arr[0:4])

# UNPACKING

arr = [1, 2, 3, 4, 5]

# Unpack the first element into 'a' and the rest into 'b' similar to spread(...) operator in js

a, *b = arr

print(a)  # Output: 1
print(b)  # Output: [2, 3, 4, 5]

# Now Lets Talk about Looping thorough the array

nums = list(range(1, 51))
print(nums)

# Using Index
""" for i in range(len(nums)):
  print(f"index : {i}\nvalue : {nums[i]}\n") """

# Without using index
""" for i in nums:
  print(f"value : {i}") """

# with index and value using the enumerate function

""" for index,value in enumerate(nums):
    print(f"index : {index}\nvalue : {value}\n")
print(f"index : {i}\nvalue : {nums[i]}\n") """

# Loop through multiple arrays simultneously with unpacking

""" nums1 = list(range(1, 4))
nums2 = list(range(4, 7))
print(nums1, nums2)

for n1, n2 in zip(nums1, nums2):
    print(n1, n2) """

# reverseing an array
""" nums.reverse()
print(nums)
nums.reverse()
print(nums) """


""" import random as r

r.shuffle(nums)
print(nums)


# Sort an array

nums.sort()
print(nums)

r.shuffle(nums)
print(nums)

nums.sort(reverse=True)
print(nums) """

""" names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen"]

# names.sort()
names.sort(key=lambda x:len(x), reverse=True)


print(names) """

# List Comprehension

arr = [i for i in range(0, 5)]
print(arr)
import math as m

arr_f = [m.sqrt(i) for i in range(0, 5)]
print(arr_f)

arr_f = [m.pow(i, i) for i in range(1, 6)]
print(arr_f)

import math as m

print(m.pow(0, 0))

# 2-D lists

arr = [[3] * 5 for _ in range(4)]

print(arr)

""" 


arr = [[3] * 5 ] * 3
print(arr)

arr[0][1] = -1

print(arr) # modify one of the rows and it will modify every row because of the reference

"""

# STRINGS

s = "I'm invincible"

print(s[4:])

# This creates a new string

s += " OmniMan"  # n time operation

print(s)

print(int("123") + int("123"))

print(str(123) + str(123))

# ASCII val of a char

print(ord("a"))
print(ord("A"))

strings = ["ab", "bc", "ef"]

print("+".join(strings))  # weird but works ig

# QUEUES (double ended queue)

from collections import deque

queue = deque()

queue.append(1)  # CONSTANT TIME
queue.append(2)

print(queue)

queue.appendleft(0)
print(queue)

queue.pop()  # CONSTANT TIME

queue.popleft()

print(queue)


# HASHSETS

mySet = set()

mySet.add(1)
mySet.add(2)

# no duplicates in set are allowed

print(1 in mySet)  # True
print(3 in mySet)  # False

mySet.remove(2)  # O(1)

# list to set

print(set(list(range(1, 6))))

# using list comprehensions
print(set([i for i in range(1, 6)]))


## HASHMAPS : cant have duplicate keys in hashmaps


myMap = {}

myMap["Hello"] = 0
myMap["World"] = 1

print(myMap)

print(myMap.get("Hello"))

print(len(myMap))

myMap["Hello"] = -1

print(myMap["Hello"])

print("Hello" in myMap)
myMap.pop("Hello")
print("Hello" in myMap)

myMap = {"Srijon": 100, "Kaberi": 150}

print(myMap)

# Dict Comprehention

myMap = {i: i**i for i in range(5)}

print(myMap)


# Loop Da Map vrmo

for key in myMap:
    print(key, " : ", myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, " : ", val)

for key in myMap.keys():
    print(key)

# Tuples are immutable

tup = (1, 2, 3)  # tuples are immutable so cant modify them

# tup[0] = 450 #BAD

print(tup)
print(tup[0])
print(tup[1])

# tuples can be used as a key to hashmap or in hashset

myMap = {(1, 2): "hello", (3, 4): "world"}

print(myMap)

mySet = ((1, 2), (3, 4))
print(mySet)

# NOTE : Lists or arrays cannot be used as a key


# HEAPS

import heapq

minheap = []

heapq.heappush(minheap, 3)
heapq.heappush(minheap, 2)
heapq.heappush(minheap, 34)

# Min ele is always at index 0 cuz by default its a min heap

print(minheap[0])

# NOTE : cuz its a minheap it will print in ascending order
while len(minheap):
    print(heapq.heappop(minheap))

# NOTE : there is no Max Heap in pyhton, then how do we implemement it ???

""" 
  1. Work Around is to use minheap and multiply by -1 when push or pop
"""

maxHeap = []
heapq.heappush(maxHeap, -1 * 6)
heapq.heappush(maxHeap, -1 * 34)
heapq.heappush(maxHeap, -1 * 56)
heapq.heappush(maxHeap, -1 * 2)

print(maxHeap[0] * -1)  # negate the negative by multiplying with -1

while len(maxHeap):
    print(heapq.heappop(maxHeap) * -1)

import random as r

arr = [i for i in range(5, 27)]

r.shuffle(arr)
print(arr)

import heapq

heapq.heapify(arr)

print(arr[0])

while arr:
    print(heapq.heappop(arr))

print("--------------------")

arr = [i for i in range(5, 27)]

r.shuffle(arr)
print(arr)

print("--------------------")


# Convert elements to negated values
arr = [-x for x in arr]
print(arr)
heapq.heapify(arr)

# Convert elements back to original values

print(-1 * arr[0])
print("--------------------")

while arr:
    print(heapq.heappop(arr) * -1)
