#Password Generator Project
import random
from pygments.lexers import r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

rand_l = ""
letters_length = int(len(letters))
for l in range(1, nr_letters + 1):
    rand_l += letters[random.randint(0, letters_length - 1)]

rand_n = ""
number_length = int(len(numbers))
for n in range(1, nr_numbers + 1):
    rand_n += numbers[random.randint(0, number_length - 1)]

rand_s = ""
symbols_length = int(len(symbols))
for s in range(1, nr_symbols + 1):
    rand_s += symbols[random.randint(0, symbols_length - 1)]

print(rand_l+rand_n+rand_s)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

