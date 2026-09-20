
# refrence count
import sys

print(sys.getrefcount(24602))
# Ans-3
print(sys.getrefcount('gagan'))
# Ans-3221225472
print(sys.getrefcount('g'))
# Ans-3221225472
print(sys.getrefcount('p'))
# Ans-3221225472

# Integer value
a=3
a='chaiaurcode'
a=3.14
a=5
print(a)
b=2
print(b)
a=a+2
print(a)


# List..
mylistone=[1,2,3,4,5]
print(mylistone)
mylisttwo=mylistone
print(mylisttwo)
mylistone=[1,2,3,4,5]
print(mylistone)
print(mylisttwo)
mylistone[0]=10
print(mylistone)
print(mylisttwo)

# copy of list
l1=[1,2,3]
l2=l1[:]
print(l1)
print(l2)
l1[0]=10
print(l1)
print(l2)

import copy
h1=[1,2]
h2=copy.deepcopy(h1)
print(h1)
print(h2)