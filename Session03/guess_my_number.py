print('''all you need is answer my guess
S is smaller
C is correct
b is bigger ''')
low = 0
high = 101
loop = True
while loop:
    mid = (low + high)//2
    answer = input("is {} your number".format(mid))

    if answer == "c" :
        print ("bingo")
        loop = False
    elif answer == "b" :
        high = mid
    elif answer == "s" :
        low = mid

    
     



