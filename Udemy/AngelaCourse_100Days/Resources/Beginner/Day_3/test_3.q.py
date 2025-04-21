# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = float(round(weight / (height**2), 2))
# print(bmi)
# if bmi < 18.5:
#  print(f"Your bmi is {bmi}, and you are underweight")
# elif bmi > 18.5:
#     if bmi < 25:
#      print(f"Your bmi is {bmi}, and you are a normal")
#     elif bmi > 25:
#      if bmi < 30:
#       print(f"Your bmi is {bmi}, and you are overweighted")
#      elif bmi > 30:
#       if bmi < 35:
#        print(f"Your bmi is {bmi}, and you are obese")
#       else:
#        print(f"Your BMI is {bmi}, and you are clinicaly obese")

if bmi < 18.5:
    print(f"Your bmi is {bmi}, and you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, and you are a normal")
elif bmi < 30:
    print(f"Your bmi is {bmi}, and you are overweighted")
elif bmi < 35:
    print(f"Your bmi is {bmi}, and you are obese")
else:
    print(f"Your BMI is {bmi}, and you are clinicaly obese")