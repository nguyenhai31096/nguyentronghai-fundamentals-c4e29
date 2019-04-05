from random import *

while True: 
    a = randint(1, 10)
    b = randint(1, 10)
    x = randint(1, 10)
    y = a * ( x + b )
    print((("if x = {}, then what is the value of {}(x + {})".format(x, a, b))))
    answer = {}
    answer_list = ["1", "2" ,"3" ,"4"]
    answer_list02 = [randint(1, 100), randint(1, 100), randint(1, 100), y ]
    for i in answer_list: 
        pick = choice(answer_list02)
        answer[i] = pick
        answer_list02.remove(pick)
    for key, value in answer.items():
        print(key, value)
    loop = True
    while loop:
        enter = (input("Your choice: "))
        
        if enter in answer.keys(): 
            if answer[enter]==y:
                print("bingo!, next question!")
                loop = False
            else:
                print("Wrong!, Do it again!")
                loop = True
        else:
            print("Plz enter the correct answer!")
            loop = True





    



    



