import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("Drogi Szymonie, zagrajmy w grę... Wybierz 0 - kamień, 1 - papier, 2 - nożyce "))
if choice >= 3 or choice < 0: 
  print("You typed an invalid number, you lose!") 

else:
    choice_list = [rock, paper, scissors]
    comp_choice_len = int(len(choice_list))
    comp_choice = choice_list[random.randint(0, comp_choice_len - 1)]
    my_choice = [rock, paper, scissors][choice]
    print(my_choice) 
    print("komputer wybrał\n" + comp_choice)

    if my_choice == comp_choice:
        print("Draw, try again")
    elif my_choice == rock and comp_choice == paper:  
        print("you lost")
    elif my_choice == rock and comp_choice == scissors:
        print("you won")
    elif my_choice == paper and comp_choice == rock:
        print("you won")
    elif my_choice == paper and comp_choice == scissors:
        print("you lost")
    elif my_choice == scissors and comp_choice == rock:
        print("you lost")
    elif my_choice == scissors and comp_choice == paper:
        print("you won")