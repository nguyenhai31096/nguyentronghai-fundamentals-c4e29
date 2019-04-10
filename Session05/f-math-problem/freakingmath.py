from random import *
from calculate import calc
def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(2, 10)
    y = randint(1, 10)
    dau = ["+","-","*","/"]
    op = choice(dau)
    z = calc(x, y, op)
    
    result = choice([z-1, z+1])
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    z = calc(x, y, op)
    result = choice([z-1, z+1])
    if result == z:
        if user_choice == True:
            return True
        else:
            return False
    else :
        if user_choice == False:
            return True
        else:
            return False
    
