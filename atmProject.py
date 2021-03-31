import datetime
allowedUsers = ['KRIS', 'MIKE', 'JOHN']
allowedPasswords = ['krispassword', 'mikepassword', 'johnpassword']
validOptions = [1, 2, 3, 4]
isValidUser = False
#balance in Account
currentBalanace = 1000

userName = input('Enter User Name: \n')

userNameInUpperCase = userName.upper()

userID = -1
# If the user exists in system, get the Index of the User
if userNameInUpperCase in allowedUsers:
    userID = allowedUsers.index(userNameInUpperCase)
    password = input('Enter Password \n')
    isValidUser = userID>=0 and password == allowedPasswords[userID]
    if(userID>=0 and password == allowedPasswords[userID]):
        isValidUser = True
    else:
        print('Incorrect password, please try again...')
else:
    print("User doesn't exist in system")

# If the User is valid , print welcome message and login date and time
if isValidUser:
    print('Welcome %s \n' % userName.title())
    dateObject = datetime.datetime.now()
    print('Current Date and time is : \n')
    print(dateObject.strftime("%c"))

# If user is valid then provide him with options to select
while isValidUser:
    print('These are the available options \n')
    print('1. Withdrawl \n')
    print('2. Cash Deposit \n')
    print('3. Complaint \n')
    print('4. Exit \n')

    selectedOption = int(input('Please select an option: '))

    if(selectedOption not in validOptions):
        print('your selected option is %d, please choose valid option \n' %
              selectedOption)
        continue

    if(selectedOption == 1):
        amountToWithdraw = int(input('How much would you like to withdraw '))
        if(amountToWithdraw <= 0):
            print('Please enter valid amount to withdraw')
            continue
        if(amountToWithdraw > currentBalanace):
            print(f"your amount to withdraw : {amountToWithdraw} exceeded available balance : {currentBalanace}")
        else:
            currentBalanace -= amountToWithdraw
            print('take your cash %d' % amountToWithdraw)

    if(selectedOption == 2):
        amountToDeposit = int(input('How much would you like to deposit '))
        if amountToDeposit > 0:
           currentBalanace += amountToDeposit
           print('current balance is %d' % currentBalanace)
        else:
            print('Please enter valid amount to deposit')

    if(selectedOption == 3):
        complaintInfo = input('What issue will you like to report? ')
        print('Thank you for contact us')

    if(selectedOption == 4):
        print('Thank you for visiting us')
        break
