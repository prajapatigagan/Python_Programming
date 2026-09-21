# Age group categraization

age=int(input("Enter Your age :"))
if 0<age<13:
    print("child")
elif 13<age<19:
    print("teenger")
elif 19<age<59:
    print("adult")
elif age>60:
    print("senior")
else:
    print("This is not human")


# movie ticket price distribution

age=22
day="Wednesday"

price=12 if age>=18 else 8
if day=="Wednesday":
    price=price-2
print(price)

# Gread calculator

marks=int(input("Enter Your subject marks :"))
if marks>=90:
    print("A")
elif 80<=marks<90:
    print("B")
elif 70<=marks<80:
    print("C")
elif 60<=marks<70:
    print("D")
elif 50<=marks<60:
    print("E")
elif marks<=40:
    print("F")
else:
    print("Error 404")

