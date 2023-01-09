

def login(userName,userPwd):
    if userName == 'testName' and userPwd == '123456':
        print("Log in successful")
    else:
        print("Log in UNSUCCESSFUL")

uName = input('Enter Login user name : ')
uPwd = input('Enter Login user password : ')

login(uName,uPwd)
