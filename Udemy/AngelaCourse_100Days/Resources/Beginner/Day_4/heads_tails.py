#Remember to use the random module 👇
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

coin_rand = random.randint(0, 1)
print(coin_rand)
if coin_rand == 0:
  print("Heads")
else:
  print("Tails")
  