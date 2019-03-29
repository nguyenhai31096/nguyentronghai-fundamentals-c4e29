from turtle import *

speed(0)
shape("turtle")
color("red")
left (30)
def diamond():
    forward(100)
    right(60)
    forward(100)
    right(120)
    forward(100)
    right(60)
    forward(100)
for i in range (4): 
    diamond()
    right (30)
    
mainloop()