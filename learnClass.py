#Python allows creating properties of an object outside the class
class Player:
    """initializer is a special method because it does not have a return type
     The first parameter of __init__ is self, which is a way to refer to the object being initialized
     Initializing the values of properties inside the class is necessary otherwise code will not compile
     double underscores mean this is a special method that the Python interpreter will treat as a special case"""
     
     #class variable are shared by all instances of the class
    teamName = 'Sun Risers' 
    teamMembers = []
    
    # defining the properties and assigning them None
    #The initializer is automatically called when an object of the class is created
    def __init__(self,name):
         #instance variables : these are specific to the Instance 
        self.name = name
        self.formerTeams = []
        self.teamMembers.append(self.name)
        
    #methods in calss   
    def tax(self):
        return self.salary*.2
    
    def salaryPerDay(self):
        return self.sarary/30
    
    @staticmethod
    def myStaticMethod():
        print('this is a static method')
        
    @classmethod    
    def myClassMethod(cls):
        print(cls.teamName)
    
  
    

# creating an object of the Employee class with default parameters
Steve = Player('Steve')
Steve.formerTeams.append('Mumbai Indians')
Mark = Player('Mark')
Mark.formerTeams.append('Chennai Super Kings')

print("team members = %s"% Steve.teamMembers)

#calling static method from class and object 
Player.myStaticMethod()
Steve.myStaticMethod()

Steve.myClassMethod()