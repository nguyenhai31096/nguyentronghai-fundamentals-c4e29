def calc(x, y, op):
    z = 0    
    if op == "+":
        z = x + y
    elif op == "-":
        z = x - y
    elif op == "*":
        z = x * y
    elif op == "/":
        z = x / y
    return z


#cach import
# from foldername.function import calc (if your function file inside another folder)