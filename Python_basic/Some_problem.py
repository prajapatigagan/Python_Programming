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

# fruit Ripeness Checker

Banana={"Green":"Unripe","Yellow":"Ripe","Brown":"Overripe"}
Color=input("Enter Banana Color(Green/Yellow/Brown)")
print(Banana.get(Color))

# Weather
Weather=input("Enter Banana Color(Sunny/Rainey/Snowy)")

if Weather=="Sunny":
    activities="Go to walk"
elif Weather=="Rainey":
    activities="Read a book"
elif Weather=="Snowy":
    activities="Build a snowman"

print(activities)        


# Tranprotation Mode Selection
distance=int(input("Enter Distance :"))

if distance<3:
    choose_vehicle="walk"
elif 3<distance<15:
    choose_vehicle="Bike"
elif distance>15:
    choose_vehicle="Car"
else:
    print("Error 404 Page Does Not Found")

print(choose_vehicle)    
    
