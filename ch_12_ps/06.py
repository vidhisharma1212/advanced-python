number= int(input("Enter a number here : \n"))
# m= True
mult=[f"{number}X{i}={number*i}" for i in range(1,11)]
with open ("tables.txt", "w") as f:
    for k in mult:
        f.write(f"{k} \n")  