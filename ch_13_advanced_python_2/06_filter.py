def greater_than_5(n):
    if n>5:
        return True
    else:
        return False

w= lambda no : no>5
l= [1,2,3,4,5,6,7,8,9,18,19]
print(list(filter(greater_than_5, l)))
print(list(filter(w, l)))