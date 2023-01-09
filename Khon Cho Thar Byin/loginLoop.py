

def inputAccount():
    userName = input('Enter Login user name : ')
    userPwd = input('Enter Login user password : ')
    login(userName,userPwd)


def login(userName,userPwd):
    if userName == "testName" and userPwd == "123456":
        print("Log in successful")
    else:
        print("WRONG")
        inputAccount()

#print("HERE 1st ENTRY point ")
inputAccount()




