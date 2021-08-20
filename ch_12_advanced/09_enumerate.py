list1= [3,53,2,None, 5.09, "Jimmy", "Songs"]
# index= 1
# for item in list1:
#     print(index, item)
#     index+=1

# The following code starts index from 0
for index, item in enumerate(list1):
    print(index, item)


# The following code starts index from 1
for index, item in enumerate(list1):
    print(index+1, item)