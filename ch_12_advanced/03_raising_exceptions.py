def increment(n):
    try: 
        return int(n)+1
    except:
        raise ValueError("You have added a string, not an integer. Pleaase type some integer. ")
x= increment(34)
print(x)
a= increment('e34')
print(a)