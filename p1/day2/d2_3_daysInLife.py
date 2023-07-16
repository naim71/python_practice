age = input("What is your current age?\n")
age_left = 90 - int(age)
days = int(age_left)*365
months = int(age_left)*12
weeks = int(age_left)*52
print(f"You have {days} days, {months} months, {weeks} weeks left")
