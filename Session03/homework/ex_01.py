clothes = ["T-Shirt", "Sweater"]


while True:
    def printsrc():
        print("Our items: ", end = '')
        print(*clothes,sep=', ')
        
    shop = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if shop == "R":
        printsrc()
        
    elif shop == "C" :
        new = input("enter new item: ")
        clothes.append(new)
        printsrc()
        
    elif shop == "U":
        update = int(input("update position?: ")) - 1
        if update < 0 :
            print("Please enter the correct position !")
        elif update > len(clothes):
            print ("Please enter the correct position !")
        else:
            shop_update = input("New item: ")
            clothes.insert(update, shop_update)
            printsrc()
    elif shop == "D":
        delete = int(input("Delete position: ")) - 1
        if delete <0:
            print("Please enter the correct position !")
        elif delete > len(clothes):
            print("Please enter the correct position !")
        else:
            del clothes[delete]
            printsrc()






