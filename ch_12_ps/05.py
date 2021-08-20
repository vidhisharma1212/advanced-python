number= int(input("Enter a number here : \n"))
# m= True
mult=[f"{number}X{i}={number*i}" for i in range(1,11)]
for k in mult:
    print(k)