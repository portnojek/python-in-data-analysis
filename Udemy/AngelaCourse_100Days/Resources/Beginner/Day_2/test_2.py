#print(len(111221)) TypeError: object of type 'int' has no len()
print(len(str(111221)))

#Data Tpes
#String
print("hello"[4]) #zaczynamy liczenie od 0
print(int("123") + int("456"))

street_name = "Abbey Road"
print(street_name[4] + street_name[5])

#Integer
print(123 + 345)

print(123_456_789) #python ignoruje podkreślenia

#Float
print(3.14159)
print(123_445.45)

#Boolean
True
False

# num_char = len(input("What is your name? "))
# new_num_char = str(num_char)

# # print("Your name has " + new_num_char + " characters")
# # print(type(num_char))
# # print(type(new_num_char))

a = 123
print(type(a))


#Zadanie od Angeli
a = str(input("Podaj pierwszą liczbę: "))
b = str(input("Podaj drugą liczbę: "))

print(a+b)
print(int(a)+int(b))

two_digit_number = input("Type a two digit number: ")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

print (int(first_digit) + int(second_digit))

'''kolejnosc dzialan, tzw. PEMDAS:
()
**
* /
+ -
'''
print(3 * 3 + 3 / 3 - 3) #wyik bedzie 7.0 (float)
print(3 * (3 + 3 )/ 3 - 3) #wyik bedzie 3.0 (float)