while (True):
    print("press q to quit")
    a= input("Enter a number: ")
    
    if a =='q':
        break
    try: 
        print("trying....")
        a= int(a)
        if a>6 :
            print("You entered a number which is greater than 6. ")
    except Exception as e:
        print(f"Your input resulted in an error : {e}")

print("Thank you ")