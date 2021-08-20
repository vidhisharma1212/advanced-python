# list= [1,2,3,4,5,6,7,8,9,10]
# list2=[list[i] for i in [2,4,6]]
# print(list2) #done.!

# See the following code-
li= [1,2,3,4,5,6,7,8,9,10]
for index,item in enumerate(li):
    if index==2 or index==4 or index==6:
        print(f"The {index+1}th element is {item}")