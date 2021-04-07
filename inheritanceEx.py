class Vehicle:
    #Initializer
    def __init__(self,make,color,model):
        self.make = make
        self.color = color
        self.model = model
        
    def printDetails(self):
        print("Manufacturer: " , self.make) 
        print("Color: ", self.color)
        print("Model: ", self.model)

"""
Inheritance.
Parent class or super class is Vehicle
Child class or sub class or Derived class is Car
"""  
class Car(Vehicle):
    def __init__(self,make,color,model,doors):
        #calling the constructor from parent class
        Vehicle.__init__(self,make,color,model)
        self.doors = doors
        
    def printCarDetails(self):
        self.printDetails()
        print("Doors: ", self.doors)
        
        
carObject1 = Car("Ford","Grey","Edge Titanium",4)
carObject1.printCarDetails()
          
