# Basic class and object

class car: # this is class
    def __init__(self,Brand,Modal):
        self.brand=Brand
        self.modal=Modal

my_car=car("toyota","fortuner") # this is object
print(my_car.brand,my_car.modal)  

my_new_car=car("TATA","NANO")
print(my_new_car.brand,my_new_car.modal)

# class method and self

class car:
    def __init__(self,Brand,Modal):
        self.brand=Brand
        self.modal=Modal
        
    def full_name(self): # this is method
        return f"{self.brand},{self.modal}"        

my_car=car("toyota","fortuner")
print(my_car.full_name())


# Inheritance
class Car:
    def __init__(self,Brand,Modal):
        self.brand=Brand
        self.modal=Modal
    def full_Name(self):
        return f"{self.brand},{self.modal}"    

class Electric_Car(Car):    
    def __init__(self,Brand,Modal,Battery_Size):
            super().__init__(Brand,Modal)
            self.battary_Size=Battery_Size

my_Tesla=Electric_Car("tesla","85 S","85kwh")  
print(my_Tesla.brand,my_Tesla.modal,my_Tesla.battary_Size) 

# Encapsulation
class Car:
    def __init__(self,Brand,Modal):
        self.__brand=Brand # private attribute
        self.modal=Modal
    def get_brand(self): # getter method
        return self.__brand

    def full_Name(self):
        return f"{self.__brand},{self.modal}"

my_car=Car("Toyota", "Fortuner") # Objects
print(my_car.get_brand())
print(my_car.full_Name())        

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
class car: # this is class
    car_count=0
    def __init__(self,Brand,Modal):
        self.brand=Brand
        self.modal=Modal
        car.car_count+=1

car("toyota","fortuner") 
car("TATA","NANO")
car("tata","nexon")
car("maruti","Swift")
print(car.car_count)


# Static method
class car:
    def __init__(self,Brand,Modal):
        self.brand=Brand
        self.modal=Modal
    def full_name(self):
        return f"{self.brand},{self.modal}" 

    @staticmethod   
    def genral_description():
        return "car are means of Transport"
    
my_Car=car("TATA","Safari")
print(my_Car.genral_description())

# properties Decorators

class Car:
    def __init__(self,Brand,Modal):
        self.brand=Brand
        self.__modal=Modal

    @property    #only_read properties ye getter hota hai setter nhi
    def modal(self):
        return self.__modal 

my_car=Car("Tata","Nexon")
print(my_car.modal)        

# class inheritance and isinstance() function

class Car:
    def __init__(self,Brand,Modal):
        self.brand=Brand
        self.modal=Modal
    def full_Name(self):
        return f"{self.brand},{self.modal}"    

class Electric_Car(Car):    
    def __init__(self,Brand,Modal,Battery_Size):
            super().__init__(Brand,Modal)
            self.battary_Size=Battery_Size

my_Tesla=Electric_Car("tesla","85 S","85kwh")  

print(isinstance(my_Tesla,Car))  #isinstance() Finction
print(isinstance(my_Tesla,Electric_Car))

# multiple inheritance

class Car:
    def __init__(self,Brand,Modal):
        self.brand=Brand
        self.modal=Modal
    def full_Name(self):
        return f"{self.brand},{self.modal}"   

class Battery:
    def batter_info(self):
        return "this is battery"

class Engine:
    def Engine_info(self):
        return "this is Engine"

class Electric_Car(Battery,Engine):
    pass

my_tesla=Electric_Car("tesla","85 S","85kwh")
print(my_tesla.batter_info)
print(my_tesla.Engine_info)
