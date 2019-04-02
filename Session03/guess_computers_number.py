from random import *
num = randint(0,100) 
#another way":  import ramdom
#               n = random.randint ()
loop = True
while loop:
    guess = int(input("guess my number: "))
    if guess < num :
        print ("too small")
    elif guess > num :
        print ("so big")
    else: 
        print ("BINGO!")
        loop = False


