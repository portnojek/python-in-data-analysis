# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

if position[0] == '1' and position[1] == '1':
    row1[0] = 'X'
elif position[0] == '2' and position[1] == '1':
    row1[1] = 'X'
elif position[0] == '3' and position[1] == '1':
    row1[2] = 'X'
elif position[0] == '1' and position[1] == '2':
    row2[0] = 'X'
elif position[0] == '2' and position[1] == '2':
    row2[1] = 'X'
elif position[0] == '3' and position[1] == '2':
    row2[2] = 'X'
elif position[0] == '1' and position[1] == '3':
    row3[0] = 'X'
elif position[0] == '2' and position[1] == '3':
    row3[1] = 'X'
elif position[0] == '3' and position[1] == '3':
    row3[2] = 'X'
    
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")