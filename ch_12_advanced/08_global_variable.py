a= 34 #Global variable
def f():
    global a #work on a 
    print(f"statement 1 : {a}")
    a= 8 # Local variable
    print(f"statement 2 : {a}")

f()
print(f"statement 3 : {a}") 
# the above statement prints 8 as a bcz the value of a is changed at global level (means in code)