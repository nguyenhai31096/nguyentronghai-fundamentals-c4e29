import random
while True:
    answer_list = ["champion", "nguyentronghai", "mylifeisfuckingawesome"]
    ranpick = random.choice(answer_list)
    loop = True
    while loop:
        words = list(ranpick)
        newwords = words[:] 
        random.shuffle(newwords)

        print(*newwords)
        answer_list = input("Your answer: ")
        if answer_list == ranpick:
            print("BINGO!")
            loop = False
        else :
            print("LET'S TRY IT AGAIN! ")
