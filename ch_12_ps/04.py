a= int(input("Enter value of a : "))
b= int(input("Enter value of b : "))
try:
    c=a/b
    print(f"The value of 'a/b' is {c}")

except ZeroDivisionError:
    print("Infinite")