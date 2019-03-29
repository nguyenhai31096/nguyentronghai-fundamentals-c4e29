height = int(input("enter your height (cm): "))
weight = int(input("enter your weight (kg): "))
heightm = height/100

bmi = weight / heightm*heightm
if bmi < 16:
    print("Severely underweight !")
elif 16 <= bmi < 18.5:
    print("Underweight !")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese!!!")



