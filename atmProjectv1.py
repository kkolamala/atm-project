import re #re module provides support for regulae Expressions
import random #random module to generate random numbers
import json #module makes it easy to parse JSON strings and files containing JSON object

atmValidOptions = [1, 2, 3, 4, 5]

database = {} # stores Account and user details
userDetails = {} #stored user details
bankName = 'ABC Corp'

def init():
    print('Welcome to %s bank'% bankName)
    print('1. Login if you have account with %s'% bankName)
    print('2. If you don\'t have account, Register with %s'% bankName)
    
    userOption = int(input('Enter 1 to Login. 2 to Register? : '))
    
    while userOption in [1,2]:
        if userOption == 1:
            login()
            break
        else:
            register()
            break
    else:
        print('Invalid option selected.')
        init()
            
def register():
    print('****** Register ******')
    fName = input('Enter First Name: ')
    lName = input('Enter Last Name: ')
    userInputemail = input('enter Email: ')
    
    while not isEmailValid(userInputemail):
        print('Invalid email entered. Please enter valid email')
        userInputemail = input('enter Email: ')
    else:
        email = userInputemail
        
    password = input('enter password: ')
    
    accountNumber = generateAccountNumber()
    
    fullName = fName + lName
    print('welcome to %s bank %s \n'% (bankName,fullName))
    print('your Account Number is %d. Store this Account Number. You will need this to login to your Account'% accountNumber)
    
    userDetails = {
        'firstName': fName,
        'lastName': lName,
        'email': email,
        'password': password
    }
    
    database[accountNumber] = userDetails
    
    #write user details and Account details to json file
    saveAccountDetailsToFile(database)
    
    login()
        

def login():
    print('****** Login ******' )
    accountNumber = input('Account Number: ')
    password = input('password: ')
    
    message = verifyUser(accountNumber,password)
    
    if(message=='valid user'):
        bankingOptions(accountNumber)
    else:
        print(message)
        login()
    
def logout():
    print('logout')

def bankingOptions(accountNumber):
    #print('Welcome %s'% database[accountNumber]['firstName'])
    print('What would you like to do?')
    print('1. Withdrawl \n')
    print('2. Cash Deposit \n')
    print('3. Complaint \n')
    print('4. Exit/Logout \n')
    
    while int(accountNumber) > 0:# which means user is valid to perform bank operations
        selectedOption = int(input('Please select an option: '))

        if(selectedOption not in atmValidOptions):
            print('your selected option is %d, please choose valid option \n' %
                selectedOption)
            continue

        if(selectedOption == 1):
            withdraw(accountNumber)
            continue
            
        if(selectedOption == 2):
            deposit()
            
        if(selectedOption == 3):
            registerComplaint()
            
        if(selectedOption == 4):
            logout()
            break
    
def withdraw(accountNumber):
    amountToWithdraw = int(input('How much would you like to withdraw '))
    if(amountToWithdraw <= 0):
        print('Please enter valid amount to withdraw')
    else:
        print('take your cash $ %d' % amountToWithdraw)
    return
    

def deposit():
    amountToDeposit = int(input('How much would you like to Deposit '))
    if(amountToDeposit <= 0):
        print('Please enter valid amount to Deposit')
    else:
        print('$ %d is deposited to you account'% amountToDeposit)
    return

def registerComplaint():
    complaintInfo = input('What issue will you like to report? ')
    print('Thank you for contact us, we will soon resolve your issue')
    return

def logout():
    print('Thanks for visting us')
    
    
    
def generateAccountNumber():
    return random.randrange(1111111111,2222222222)

def saveAccountDetailsToFile(database):
    with open("database.json", "w") as outfile:
       json.dump(database, outfile)
    
def verifyUser(accountNumber,password):
    # Opening JSON file
    with open('database.json', 'r') as openfile:
        # Reading from json file
        userDictionary = json.load(openfile)
        
    if(accountNumber in userDictionary):
        if(userDictionary[accountNumber]['password'] == password):
            return 'valid user'
        else:
            return 'Invalid Password'
    else:
        return 'Invalid Account Number'
    

def isEmailValid(email):
    emailRegex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$' #email regular expression
    return re.search(emailRegex,email) 
    
init()