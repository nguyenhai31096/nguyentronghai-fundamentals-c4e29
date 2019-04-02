fav = ["a", "b"]
print("hi, here is your favorite thing")
print (*fav, sep = ", ")
input_fav = input("What's fav? ")
fav.append(input_fav)
print(*fav, sep = ",")

