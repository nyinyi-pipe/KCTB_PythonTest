def log_in():
	if username=="xxsx" and password=="1231":
		print(username)
	else:
		print("Wrong")
		entry()

def entry():
	username = input("Enter NAME")
	password = input("Enter PWD")

print(" LOGIN .....")
#username = input("ENTER NAME")
#password = input("ENTER PWD")
entry()

log_in()