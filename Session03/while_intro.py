#Sample
while False:
    print("hi")

#way1 :
count = 0
while True:
    print("hi")
    count += 1
    if count == 2: #kiem soat so lan vong while
        break # pha vong lap gan nhat
        print("done")

#way2:(best way) 
count = 0
loop = True
while loop:
    print("hi")
    count += 1
    if count == 3 :
        loop = False
        print("done")
#way3 :
count = 0
while count < 3:
    print("hi")
    count += 1

