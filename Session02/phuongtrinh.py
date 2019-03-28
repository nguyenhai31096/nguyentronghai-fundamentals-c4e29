a = int(input("nhap vao a "))
b = int(input("nhap vao b "))
c = int(input("nhap vao c "))
delta = b**2-4*a*c
if delta < 0:
    print("pt vo nghiem")
elif delta == 0:
    print ("pt co nghiem kep", (-b)/(2*a))
else:
    print ("x1 = ",  (-b - delta**(1/2))/(2*a))
    print ("x2 = ",  (-b + delta**(1/2))/(2*a))

