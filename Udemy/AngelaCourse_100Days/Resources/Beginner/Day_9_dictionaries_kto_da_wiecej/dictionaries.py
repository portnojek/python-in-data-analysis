programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."}

#retrieve data from dictionary

print(programming_dictionary["Bug"])

#adding new item
programming_dictionary["Loop"] = "The action doing something over and over again"

#editing existing item

programming_dictionary["Bug"] = "A moth in you computer"

#create an empty dictionary

new_table = {}
print(new_table)
print(programming_dictionary)

#wipe
#programming_dictionary = {}

print(new_table)
print(programming_dictionary)

#Loop through a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])