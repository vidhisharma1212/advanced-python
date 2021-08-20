try:
    a= int(input("Enter a number : "))
    c= 1/a 
    print(c)
except ValueError as e:
    print("Exception1 occured.")
    print("Enter an integer please... ")
    print(e)
except ZeroDivisionError as e:
    print("Exception 2 occured.")
    print("Make sure you are not dividing by 0.")
    # print(e) What will user do by knowing this?

print("Thanks for using this code!")