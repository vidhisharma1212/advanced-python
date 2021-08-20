from functools import reduce 
li= [1,2,3,4,8,3,5,2,4,6,3]
l= reduce(max, li)
print(l)