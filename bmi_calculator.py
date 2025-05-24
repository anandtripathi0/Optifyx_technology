weight=float(input("Enter your weight(kg) : "))
height=float(input("Enter your height(m²) : "))
bmi=weight/height
if bmi<18.5:
    print("you are in underweight!")
elif 18.5<=bmi<=24.9:
    print("Normal weight!")
elif 24.9<=bmi<=29.9:
    print("Overweight!")
else:
    print("Your body is Obesity")
                