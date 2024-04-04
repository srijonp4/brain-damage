""" name = input()
print(f"Hello {name}")
 """

# python is a dynamically typed lang
""" 
n, m = 0, "abc"

print("n : ", n, "\nm : ", m)
 """
# Increment decrement
""" n = n + 1  # Good
n += 1  # Good
# n++ Bad

print(n)

n = n - 1  # Good
n -= 1  # Good
# n++ Bad """

""" print(n) """

# None is null (absense of value)
""" n = 2
print(type(n)) """
# n = None
# print(type(n))

# conditionals statements
""" 
if n > 2:
    n -= 1
    print(f"n is greater than 2 and val of n after decrementing 1 is : {n}")
elif n < 2:
    n += 1
    print(f"n is less than 2 and val of n after incrementing 1 is : {n}")
else:
    print(f"n : {n}, typeof n is :" ,type(n))
 """
# Parenthesis needed for multiline conditionals
# and === &&
# or === ||
""" 
n, m = 1, 1

if ((n < m) and (n != m)) or (n == m):
    print(n + 1)
"""
# loops
n, m = 1, 10

""" while n <= m:
    print(n)
    n += 1
 """

""" for i in range(5):
    print(i)

for i in range(2, 6):
    print(i)

# reverse loop
for i in range(5, 0, -1):
    print(i)
"""

""" 
for i in range(5, 0, -2):
    print(i)
 """
""" for i in range(0, 21, 2):
    print(i) """

# Division
# decimal division by default
""" print(5 / 2) """
# to get integer division we have to use //
""" print(5 // 2) """

# CAREFUL : most langs round towards 0 by default so negative numbers will round down

""" print(-3 / 2)
print(-3 // 2) """  # but in python it doesn't round towards 0

# A workaround for rounding towards 0 is to use decimal division and then cast it to integer
""" print(int(-3/2)) """

# modulo
# similar to other langs
""" print(10 % 3) """
# except for negative numbers
""" print(-3 % 2) """  # except -1 but get 1
""" print(-10 % 3)   """  # expect -1 but get 2 weird right ?

# WORKAROUND: use fmod from math library

import math as m

""" print(m.fmod(-10, 3))   """  # but it gives in float though so

""" print(int(m.fmod(-10, 3)))  """  # but it gives in float though so


# few more helpful math functions

# floor round down to 0
""" print(m.floor(9 / 2)) """
# ceil -> opposite of floor
""" print(m.ceil(9 / 2)) """  # result 5
# squareroot
""" print(m.sqrt(2)) """
# power
""" print(m.pow(2, 3)) """
""" print(2**3)  """  # alt to pow function

# if ever need a maximum/minimum integer
""" print(float("inf"))
print(float("-inf")) """

# python numbers are infinite so they never overflow
""" print(m.pow(2, 200))
print(m.pow(2, 200) < float("inf")) # result in True """
