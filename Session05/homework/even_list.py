def get_even_list(l):
    listnumb =[]
    for i in l:
        if i % 2 == 0:
            listnumb.append(i)
        else:
            pass
    return listnumb
        

even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
