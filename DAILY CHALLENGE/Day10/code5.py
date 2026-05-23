W = float(input("Enter weight(kg): "))
H = float(input("Enter height(m): "))
bmi = W / ((H / 100) ** 2)
print("BMI = ", round(bmi, 2))
