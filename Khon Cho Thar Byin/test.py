def log_in(uName, pWD):
       if uName == "TEST" and pWD == "123":
          print("OK")
		else:
			print("Wrong")
			entry()

def entry():
	username = input("Enter NAME")
	password = input("Enter PWD")
    log_in( username,password )




print(" LOGIN .....")
#username = input("ENTER NAME")
#password = input("ENTER PWD")
entry()
