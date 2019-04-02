sheepsize = [5, 7, 300, 90, 24, 50, 75]

#2.1
print("Hello, my name is Hai and there are my sheep size")
print(sheepsize)

#2.2
print("Hello, my name is Hai and there are my sheep size")
print(sheepsize)
print("Now my biggest sheep has size {} let's shear it ".format(max(sheepsize)))

#2.3
sheepsize[sheepsize.index(max(sheepsize))]= 8
print("After shearing, here is my flock ")
print(sheepsize)

#2.4
print("One month has passed, now here is my flock")
for i in range(len(sheepsize)):
    sheepsize[i] += 50
print(sheepsize)

#2.5 & 2.6
x = 0
loop = True
sheepsize = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hai and there are my sheep size")
print(sheepsize)
while loop:
    x +=1
    print("Month {} :".format(x))     ,   
    print("One month has passed, now here is my flock")
    for i in range(len(sheepsize)):
        sheepsize[i] += 50
    print(sheepsize)
    print("Now my biggest sheep has size {} let's shear it ".format(max(sheepsize)))
    sheepsize[sheepsize.index(max(sheepsize))]= 8
    print("After shearing, here is my flock ")
    print(sheepsize)
    print()
    if x == 4:
        loop = False
print ("my flock has size in total: ", sum(sheepsize))
print ("I would get {} * 2$ = {}$".format(sum(sheepsize),sum(sheepsize)*2))



   
