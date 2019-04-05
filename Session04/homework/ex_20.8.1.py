sentence_input = input("enter the sentence: ").lower()
list(sentence_input)
alpha = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
for i in alpha:
    n = sentence_input.count(i)
    if n!= 0:
        print(i, n)
    else:
        pass
    
        