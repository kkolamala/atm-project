#Python allows creating properties of an object outside the class
class Employee:
    """initializer is a special method because it does not have a return type
     The first parameter of __init__ is self, which is a way to refer to the object being initialized
     Initializing the values of properties inside the class is necessary otherwise code will not compile
     double underscores mean this is a special method that the Python interpreter will treat as a special case"""
    
    # defining the properties and assigning them None
    #The initializer is automatically called when an object of the class is created
    def __init__(self,id,salary,department):
        self.id = id
        self.salary = salary
        self.department = department
    
  
    

# creating an object of the Employee class with default parameters
Steve = Employee(3789, 2500, "Human Resources")

print(Steve.salary)