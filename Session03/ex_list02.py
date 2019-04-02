print("hi, here is your list")
print(20*"*")
fav = ["a","b","c"]
for index, item in enumerate(fav):
    #print(index+1, item, sep=". ")
    print("{}. {}".format(index+1, item))
print(20*"*")