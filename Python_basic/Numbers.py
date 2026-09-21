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


# Strings..
s1 = "Gagan deep"
print(s1[0])
slice1 = s1[0:5]
print(slice1)
num_list="0123456789"
print(num_list[:])
print(num_list[3:])
print(num_list[:7])
print(num_list[::7])
print(num_list[0:7:2])
print(s1.lower())
print(s1.upper())
s2="     gagan deep       "
print(s2.strip())
print(s1.replace("deep","prajapati"))
chai="Leman,gingar,Masala,Mint"
print(chai.split(","))
print(s1.find("deep"))

# String to list
chai_types="Masala"
quantity="2"
order="I ordered {} cups of {} chai"
print(order.format(quantity,chai_types))
# list to String
chai_list=["Masala","Leman","Ginger"]
print(",".join(chai_list))
# print letter in string
chai="Masala"
for letter in chai:print(letter)
# String ke sath
chai="he said,\"I Love you\""
print(chai)
chai="gagan\ndeep"
print(chai)
chai=r"c:\Users\gagan\Desktop"
print(chai)


# List in python

chai=["Masala","Leman","Ginger","Harbal"]
print(chai[1])
chai[2]="Mint"
print (chai)
print(chai[1:1])
chai[1:1]=["white","black"]
print(chai)
chai[1:3]=[]
print(chai)

# for loop in list
for tea in chai:
    print(tea)

for tea in chai:
    print(tea, end=" ")


chai.append("Tulsi")
print(chai)

# question putup
if "Tulsi" in chai:
    print("Tulsi is available")

# remove and pop
chai.pop()
print(chai)
chai.remove("Leman")
print(chai)

# adding list to list
chai_one=["Tulsi","Mint","Masala"]
print(chai_one)
chai.insert(1,"Leman")
print(chai)
chai_one_copy=chai_one.copy()
print(chai_one_copy)
chai_one_copy.append("Ginger")
print(chai_one_copy)

# squre and cube of number
squared_num=[x**2 for x in range(1,10)]
print(squared_num)
cube_num=[x**3 for x in range(1,10)]
print(cube_num)

# Dictionay in python
chai_types={"Masala":10,"Leman":5,"Ginger":7,"Mint":8}
print(chai_types)
print(chai_types["Masala"])
print(chai_types.get("Leman"))

# change of value in dictionary
chai_types["Mint"]=9
print(chai_types)

# use for loop in dictionary
for chai in chai_types:
    print(chai)
for chai in chai_types:
    print(chai,":",chai_types[chai])
for key,value in chai_types.items():
    print(key,":",value)  

# question putup
if "Masala" in chai_types:
    print("it is here") 
else:
    print("it is not here")  

# length of dictionary , key added in dictionary,delete
print(len(chai_types))

chai_types["tulsi"]=12
print(chai_types)

chai_types.pop("tulsi")
print(chai_types)

del chai_types["Mint"]
print(chai_types)

tea_shop={"chai":{"Masala":10,"Leman":5,"Ginger":7,"Mint":8},
           "coffee":{"Black":15,"White":20,"Cold":25}}
print(tea_shop)

# squre and cube of number using dictionary
squared_num={x:x**2 for x in range(1,10)}
print (squared_num)
squared_num.clear()
print(squared_num)
cube_num={x:x**3 for x in range(1,10)}
print(cube_num)