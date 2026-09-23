import math

# Square of Number

def Square(nums):
    return nums**3
print(Square(5))

# mulitiple parameters

def Square(nums,exp):
    return nums*exp
print(Square(5,5))

# polymorphism in function

def Square(p1,p2):
    return p1*p2
print(Square(5,5))
print(Square("H",6))
print(Square(2,5))

# function return multiple values

def circle_State(R):
    area= math.pi*R**2
    circumference=2*math.pi*R
    return area,circumference
print(circle_State(3))

# Default parameter values

def greet(nums,exp=2):
    return nums+exp
print(greet(5))
print(greet(5,5))
print(greet("Gagan","Prajapati"))

# lemda function

cube=lambda x:x**3
print(cube(5))

# function with args
def total(*args):
    print(args)
    return sum(args)
print(total(1,2,3,4,5))
print(total(9,8,7,6,5,4))

# function with **kwargs

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="gagan",power="Engineer") 

print_kwargs(name="gagan",power="Engineer",Enemt="Dr.v jhatka")      

# Genrator function with yield..

def Even_no(limit):
    for key in range(2,limit+1,2):
        yield key

for num in Even_no(10):
    print(num)        

# recursive Fuunction

def fectorial(n):
    if n==0:
        return 1
    else:
        return n*fectorial(n-1)

print(fectorial(5))    