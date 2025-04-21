print(int(8/3)) #zawsze występje odcięcie w dół, w tym przypadku będzie to 2
print(round(8/3, 2)) #zaokrągleie do dwóch miejsc po przecinku - two decimal places
print(8 // 3) # floor division - zaokrąglenie w dół

result = 4 / 2
result /= 2
print(result) #będzie 1.0


'''
czyli mamy dodatkowe operatory jak +=, -= itp
'''

score = 0
height = 1.8
isWinning = True
#f-String
print(f"your score is {score}", f"your heigth is {height}", f"your place is {isWinning}" )

#challenge z miesiącami życia które nam pozostały

age = input("What is your curret age? ")
age = int(age)

days = 90 * 365
month = 90 * 12
week = 90 * 52

days_left = days - (age * 365)
months_left = month - (age * 12)
week_left = week - (age * 52)

print(f"Pozostało Ci {days_left} dni, {months_left} miesięcy, {week_left} tygodni życia...")

# ale można jeszcze metodą Ageli
age = input("What is your curret age? ")
age_int = int(age)

years_remaining = 90 - age_int
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

message = f"zostało Ci {years_remaining} lat, {months_remaining} miesięcy, {weeks_remaining} tygodni, {days_remaining} dni życia..."
print(message)