x = int(input("enter x: "))
y = int(input("enter y: "))
n = input("enter the operator: ")
result = 0
if n == "+":
    result = x+y
elif n == "-":
    result  = x-y
elif n == "*":
    result = x*y
elif n == "/":
    result = x/y
print ("{0} {1} {2} = {3}".format(x, n, y, result))

