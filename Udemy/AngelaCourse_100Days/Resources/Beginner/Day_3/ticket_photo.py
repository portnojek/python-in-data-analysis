#if_else_statement

print("Wlcome to the rollercoaster: ")

height = int(input("What is your height in cm?: "))
bill = 0

if height >= 120:
    #print("You may get on!")
    age = int(input("How old are you?: "))
    if age < 12:
        bill = 5
        print("5 dollars, please")
    elif age > 12 and age < 18:
        bill = 7
        print("7 dollars, please")
    else:
        bill = 12
        print("12 dollars, please ")

    wants_photo = input("Do you want a photo taken. Y or N. ")
    if wants_photo == 'Y':
        bill += 3
        print(f"{bill} dollars, please ")
    else:
        print("You can go!")
else:
    print("You can't to go!")