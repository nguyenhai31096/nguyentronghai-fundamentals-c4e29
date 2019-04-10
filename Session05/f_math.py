from random import *
from calculate import calc
while True:
    a = randint(2, 10)
    b = randint(1, 10)
    op = ["+","-","*","/"]
    pick_op = choice(op)
    z = calc(a, b, pick_op)
    error = choice([-1, 0, 1])
    ans = z + error
    
    print("{} {} {} = {}".format(a, pick_op, b, ans))
    answer = input("(Y/N)?").lower()
    if error == 0:
        if answer == "y":
            print("bingo!")
        elif answer == "n":
            print("idiot!")
    else:
        if answer == "n":
            print("bingo!")
        elif answer == "y":
            print("idiot!")

    

