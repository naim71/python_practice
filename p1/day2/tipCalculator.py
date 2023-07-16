print("Welcome to the tip calculator")
bill = input('What was the total bill? $')

tip = input('What percentage of bill would you like to give: 12, 15 or 10? ')
tip_given = int(tip)/100
percentage_bill = float(bill)*tip_given
total_bill = float(bill)+percentage_bill
numOfPep = input('How many people to split the bill: ')
each_bill = total_bill/int(numOfPep)
rounded_bill = round(each_bill,2)
each_person = print(f'Each person should pay: ${rounded_bill}')