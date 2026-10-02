weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

bmi = weight // height ** 2

if bmi < 18.5:
    print("Your body mass index is:" + str(bmi) + " Underweight")
elif 18.5 <= bmi < 24.9:
    print("Your body mass index is:" + str(bmi) + " Normal weight")
elif 25 <= bmi < 29.9:
    print("Your body mass index is:" + str(bmi) + " Overweight")
