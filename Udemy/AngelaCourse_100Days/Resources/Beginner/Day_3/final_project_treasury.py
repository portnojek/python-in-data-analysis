#to jest koncowy projekt z kursy Angeli

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

kierunek = input("Jesteś na skrzyżowaniu dróg, w którą stronę skręcasz, w lewo, czy prawo? ").lower()
if kierunek == "prawo":
    print("Wpadłeś w dziurę, gra skończona...")
elif kierunek == "lewo":
    co_robie = input("Jesteś nad brzegiem jeziora. Czekasz na łódź, czy zdecydowałeś się płynąć wpław? Napisz: czekam lub płynę ").lower()
    if co_robie == "płynę":
        print("Pożarł Cię rekin. Przegrałeś!")
    elif co_robie == "czekam":
         drzwi = input("Przybyłeś na wyspę. Przed sobą widzisz troje drzwi, czerwone, żółte oraz niebieskie. Przez które przechodzisz? ").lower()
         if drzwi == "żółte":
            print("Cudownie! Odkryłeś skarb!")
         else:
            print("Niestety, to była pułapka. Przegrałeś!") 