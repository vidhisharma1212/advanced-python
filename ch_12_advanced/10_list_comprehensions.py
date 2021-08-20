a= [1,3,5,8,9,0,3,3,19,10,19,39,26,49,27,10,28,48,27,32]
# b=[]
# for item in a :
#     if item%2==0:
#         b.append(item)

# print(b)

# short cut to write the same-
b= [i for i in a if i%2==0]
print(b)

t= [1,2,2,2,5,6,4,3,5,3,2,4,5,3,4,3,7,23,4,3,3,]

s= {i for i in t}
# print(t)
print(s) #does not print repeated value..