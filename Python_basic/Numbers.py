# number operations
import fractions
import numbers


a=6
b=5
c=6
print((a*b)+c)
print(2*2)
print(1000**1000)

# some function
# developer/debug representation of object
print(repr('gagan'))
# human-readable String Object
print(str('gagan'))
# show output in console
print('gagan')

x = "Gagan\nPrajapati"
print(str(x))
print(repr(x))

# Comparison of numbers

a=6
b=5
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a is b)
print(5<6 or 6>5)


# Number operations
print(0b1010) # binary number
print(0o20) # octal number
print(0x20) # hexadecimal number
print(0xFF) # hexadecimal number
print(bin(64))
print(oct(64))
print(hex(64))
print(int(0b1010))
print(int('10000',2))
print(int('64',8))
print(int('64',10))
print(int('64',16))
print(float(64))

# Bitwise Operators
print(5 & 6) # and
print(5 | 6) # or
print(5 ^ 6) # xor
print(~5) # not
print(5 << 2) # left shift
print(5 >> 2) # right shift

# some libraries

import math

print(math.sqrt(64))
print(math.ceil(3.14))
print(math.floor(3.14))
print(math.floor(-3.14))
print(math.pow(2,3))
print(math.factorial(5))
print(math.gcd(12,15))
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))
print(math.log(100,10))
print(math.trunc(3.14))
print(math.trunc(-3.14))
print(math.isqrt(64))


import random

print(random.randint(1,10))
print(random.randint(1,10))
print(random.choice([1,2,3,4,5]))
print(random.choices([1,2,3,4,5]))
l1=['king','queen','jack','ace']
random.shuffle(l1)
print(l1)
print(random.choice(l1))
print(random.choices(l1))
print(random.sample(l1,2))
print(random.uniform(1,10))

# From fractions import Fraction

from decimal import Decimal

d1 = Decimal(1.1)
d2 = Decimal(2.2)
print(d1 + d2)



# Sets...
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1 | set2) # union
print(set1 & set2) # intersection
print(set1 - set2) # difference
print(set1 ^ set2) # symmetric difference
print(set1-set1) # empty set