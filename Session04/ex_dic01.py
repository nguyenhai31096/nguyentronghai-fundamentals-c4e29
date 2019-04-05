print(20*" *")
dic = {
    "vc": "vãi chưởng",
    "clgt": "cậu làm gì thế",
    "dcm": "đập con muỗi",
}
for key in dic.keys():
    print(key, end = ' ')
print() 
loop = True
while loop:
    ask = input("your code?: ")
    if ask in dic:
            print(dic[ask])
    else:
        yes_or_no = input("Add word? (Y/N)").lower()
        if yes_or_no == "y":
            dic_input = input("meaning: ")
            dic[ask] = dic_input
        else:
            loop = False
    