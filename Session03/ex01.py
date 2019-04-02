n = int(input("enter the number: "))
count = 0
loop = True
while loop:
    n = n//10
    count += 1
    if n == 0:
        loop = False

print (count)
