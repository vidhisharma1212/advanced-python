try:
    i= int(input("Enter a number : "))
    c= 1/i
except Exception as e:
    print(e)
# else works only if try is worked.
else:
    print("We were succesful! ")