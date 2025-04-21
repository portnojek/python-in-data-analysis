#moje metoda - pewnie kiepska :) - po sprawdzeniu okazalo sie z nie ma tragedii

name1 = input("What is your name?: ")
name2 = input("What is her name?: ")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

t = (lower_case_name1.count("t"))
r = (lower_case_name1.count("r"))
u = (lower_case_name1.count("u"))
e = (lower_case_name1.count("e"))
t2 = (lower_case_name2.count("t"))
r2 = (lower_case_name2.count("r"))
u2 = (lower_case_name2.count("u"))
e2 = (lower_case_name2.count("e"))

l3 = (lower_case_name1.count("l"))
o3 = (lower_case_name1.count("o"))
v3 = (lower_case_name1.count("v"))
e3 = (lower_case_name1.count("e"))
l4 = (lower_case_name2.count("l"))
o4 = (lower_case_name2.count("o"))
v4 = (lower_case_name2.count("v"))
e4 = (lower_case_name2.count("e"))

prawda = (t + r + u + e + t2 + r2 + u2 + e2)
milosc = (l3 + o3 + v3 + e3 + l4 + o4 + v4 + e4)

pisane = int(str(prawda) + str(milosc))

if 10 > pisane or pisane > 90:
    print (f"Your score is {pisane}, you go together like coke and mentos")
elif 40 <= pisane <= 50:
    print (f"Your score is {pisane}, you are alright together")
else:
    print (f"Your score is {pisane}")