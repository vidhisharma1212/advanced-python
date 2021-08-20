try:
    i= int(input("Enter a number : "))
    c= 1/i
except Exception as e:
    print(e)
    exit()
# finally works always ... no matter if error is there, regardless if the program has exited exit()
finally:
    print("We were succesful! ")

print("Thanks for using this")