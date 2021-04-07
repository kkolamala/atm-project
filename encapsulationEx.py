class User:
    def __init__(self,username=None,password=None):
        self.__username = username #private property
        self.__password = password #private property
        
    def login(self,username,password):
        if(self.__username.lower() == username.lower()):
            if(self.__password == password):
                return 'Valid user'
            else:
                return 'Invalid Password'
        else:
            return 'Invalid username'
        

#create a new User Object
Steve = User("Steve", "12345")

print(Steve.login('steve',"12345"))

Steve.__password  # compilation error will occur, since we made password as private variable and no one will have access to it
