# # Basic class and object

# class car: # this is class
#     def __init__(self,Brand,Modal):
#         self.brand=Brand
#         self.modal=Modal

# my_car=car("toyota","fortuner") # this is object
# print(my_car.brand,my_car.modal)  

# my_new_car=car("TATA","NANO")
# print(my_new_car.brand,my_new_car.modal)

# # class method and self

# class car:
#     def __init__(self,Brand,Modal):
#         self.brand=Brand
#         self.modal=Modal
        
#     def full_name(self): # this is method
#         return f"{self.brand},{self.modal}"        

# my_car=car("toyota","fortuner")
# print(my_car.full_name())


# # Inheritance
# class Car:
#     def __init__(self,Brand,Modal):
#         self.brand=Brand
#         self.modal=Modal
#     def full_Name(self):
#         return f"{self.brand},{self.modal}"    

# class Electric_Car(Car):    
#     def __init__(self,Brand,Modal,Battery_Size):
#             super().__init__(Brand,Modal)
#             self.battary_Size=Battery_Size

# my_Tesla=Electric_Car("tesla","85 S","85kwh")  
# print(my_Tesla.brand,my_Tesla.modal,my_Tesla.battary_Size) 

# # Encapsulation
# class Car:
#     def __init__(self,Brand,Modal):
#         self.__brand=Brand # private attribute
#         self.modal=Modal
#     def get_brand(self): # getter method
#         return self.__brand

#     def full_Name(self):
#         return f"{self.__brand},{self.modal}"

# my_car=Car("Toyota", "Fortuner") # Objects
# print(my_car.get_brand())
# print(my_car.full_Name())        

# polymorphism
# same method but different vihabiour
class Car:
    def __init__(self,Brand,Modal):
        self.__brand=Brand # private attribute
        self.modal=Modal
    def get_brand(self): # getter method
        return self.__brand

    def fuel_type(self):
         return "petrol or diesel"
    

class Electric_Car(Car):    
    def __init__(self,Brand,Modal,Battery_Size):
        super().__init__(Brand,Modal)
        self.battary_Size=Battery_Size
    def fuel_type(self):
        return "Electric charge"        

my_Tesla=Electric_Car("tesla","85 S","85kwh")  
print(my_Tesla.fuel_type())
my_Car=Car("TATA","Safari")
print(my_Car.fuel_type()) 

# class veriables
