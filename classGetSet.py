class User:
    def __init__(self,username=None): #initializer
        self.__username = username
        
    def setUsername(self,value):
        self.__username = value
        
    def getUsername(self):
        return self.__username
    
user = User('Krishna')
user.setUsername('Mohan')

print(user.getUsername())



# str = 'str1'
# number = 10
# isValid = False
# print('str1', number,isValid)