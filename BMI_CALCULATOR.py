# BMI CALCULATOR
name = input("What is your name?: ")
height_m = float(input("How tall are you in meters?: "))
weight_kg = float(input("How much do you weight in KG?: "))


def bmi_calculator():
    bmi = weight_kg / (height_m ** 2)
    if bmi < 25:
        print("Your BMI: " + str(bmi))
        return name + ", you are not overweight."
    else:
        print("Your BMI: " + str(bmi))
        return name + ", you are overweight."


print(u'\u2500' * 50)
p1 = bmi_calculator()
print(p1)
