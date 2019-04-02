import random

answer = "champion"
words = list(answer)
newwords = words[:] 
random.shuffle(newwords)

print(*newwords)
loop = True
while loop:
    answer = input("Your answer: ")
    if answer == "champion":
        print("BINGO!")
        loop = False
    else :
        print("LET'S TRY IT AGAIN! ")

