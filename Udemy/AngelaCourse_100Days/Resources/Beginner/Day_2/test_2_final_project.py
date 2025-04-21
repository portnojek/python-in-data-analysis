tip_10 = 10
tip_12 = 12
tip_15 = 15
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input(f"What percentage tip would yo like to give? {tip_10}, {tip_12}, or {tip_15}? "))
people_split = int(input("How many people to split the bill? "))
full_payment = total_bill * (1 + tip_percent/100)
pay_per_person = round((full_payment / people_split), 2)
print(f"Each person should pay: $ {pay_per_person}")
