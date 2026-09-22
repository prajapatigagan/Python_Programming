# # Count positive number

# numbers=[1,-2,3,-4,5,6,-7,-8,9,10]
# positive_count=0
# for num in numbers:
#     if num>0:
#         positive_count+=1
#         num=positive_count
#         print(num)


# # Sum of Even no.

# n=10
# Even_sum=0

# for i in range(1,n+1):
#     if i%2==0:
#         print("Even",i)
#         Even_sum+=1
        
# print (Even_sum) 
  
# n=0
# number =[1,2,3,4,5,6,7,8,9]
# for i in number:
#     if i%2==0:
#         print(i)  
#         n+=1  

# print("Even no.",n)   

# # Multiplication Table print

# n=5
# for i in range(1,11):
#     if i==5:
#         continue
#     print(n*i)

# # Reverse A String..
# string="gagan"
# Reverse=""
# for i in string:
#     Reverse=i+Reverse

# print(Reverse)    

# # find non repetable character

# String="aammnnhhookddrr"
# Non_Repeting=""
# for nums in String:
#     if nums not in Non_Repeting:
#         Non_Repeting+=nums
          
# print(Non_Repeting)     

# # Fectorial calculator
# nums=5
# fectorial=1
# while nums>0:
#     fectorial=fectorial*nums
#     nums -=1
#     print(nums)
# print(fectorial)  

#   valid input
# nums=int(input("Enter Number :"))

# if 1 <= nums <= 10:
#     print("Input Valid")
# else:
#     print("Input nodes not valid")

# print duplicate in list
items=["apple","banana","orange","apple","mango"]
unique_item=set()
for item in items:
    if item in unique_item:
        print("Duplicate",item)
        break
    unique_item.add(item)