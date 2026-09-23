# Scope Example

username="Gagan"

def func():
    username="gagan"
    print(username)

print(username)
func()

# Example 2

x=99
def func2(y):
    z=x+y
    print(z)
func2(2)

# Example 3

x=99
def func3():
    global x
    x=90
func3()
print(x)

# Example 4
x=97
def f1():
    x=89
    def f2():
        print(x)
    f2()
f1()   

# Example 4
x=97
def f1():
    x=89
    def f2():
        print(x)
    return f2
my_result=f1()
my_result()

# Example 5
def chaiorcode(num):
    def actual(x):
        return x**num
    return actual

# x
f=chaiorcode(2)
g=chaiorcode(3)
# num
print(f(2))
print(g(5))