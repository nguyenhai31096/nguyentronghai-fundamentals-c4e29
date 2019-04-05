from random import *

while True: 
    #question 1
    print("Question 1: ")
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
                print("Wrong!")
                loop = False
        else:
            print("Wrong!, Do it again!")
            loop = True
    #question 2
    print("Question 2:")
    print ("Estimate this answer (exact calculation not needed): ")
    score1 = randint(1, 100)
    score2 = randint(1, 100)
    score3 = randint(1, 100)
    score4 = randint(1, 100)
    score5 = randint(1, 100)
    about = (score1 + score2 + score3 + score4 + score5)/5
    about_answer = {}
    about_answer_list = ["1", "2" ,"3" ,"4"]
    about_answer_list02 = [randint(1, 100), randint(1, 100), randint(1, 100), about]
    print("Jack scored these marks in 5 math tests: {}, {}, {}, {} and {}. What is the mean?".format(score1,score2,score3,score4,score5))
    for f in about_answer_list: 
        pick02 = choice(about_answer_list02)
        about_answer[f] = pick02
        about_answer_list02.remove(pick02)
    for key2, value2 in about_answer.items():
        print(key2, value2)
    loop2 = True
    while loop2:
        enter2 = (input("Your choice: "))
        
        if enter2 in about_answer.keys(): 
            if about_answer[enter2]==about:
                print("bingo!, next question!")
                loop2 = False
            else:
                print("Wrong!")
                loop2 = False
        else:
            print("Wrong!, Do it again!")
            loop2 = True


    

