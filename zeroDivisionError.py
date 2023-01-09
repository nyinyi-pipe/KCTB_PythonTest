try:
    data1=int(input("please enter a number:"))

    if data1==10:
        raise ZeroDivisionError
    else:
        raise TypeError
except ZeroDivisionError:
    print("From ZeroDivisionError")
    print(type(data1))
except TypeError:
    print("This is TypeError")
    print(type(data1))