height = input("Enter you height in m: ")
weight = input("Enter you weight in kg: ")

result = float(weight)/(float(height)**2)
bmi = int(result)
print("Your BMI is = " + str(bmi))