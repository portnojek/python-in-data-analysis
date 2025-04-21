from os import name
from replit import clear
from art import logo

print(logo)

auctioners = {}



should_end = False
while not should_end:
    key = str(input("What's your name? "))
    value = float(input("What's your bid?: $"))
    auctioners[key] = value
    
    def auction(key, value):

        biders_list = {}
        biders_list["name"] = key
        biders_list["bid"] = value
        auctioners.append(biders_list)
    ans = input("Is the another player? ")
    if ans == "no":
        should_end = True
        print(auctioners)
    else:
        clear()
        auction(key, value)

auction(key, value)
