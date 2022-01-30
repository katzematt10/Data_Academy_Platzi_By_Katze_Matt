# Here, we're going to type some text methods 
# to learn how to use these type of fucntions.

# # # # # name = input("Please, type your name: ")
# # # # # name=name.upper()
# # # # # print(name)
# # # # # Capital_name = name.capitalize()
# # # # # print(Capital_name)

# name = input("Please, type your name: ")
# print(name)
# #If our name has useless spaces we can use strip
# name = name.strip()
# print(name)


# name = input("Please, type your name: ")
# print(name)
# print(name.replace('o','onsio'))
import random as rnd
name = input("Please, type your name: ")
print(name)
lenght= len(name)
Random_number = rnd.randrange(0,lenght-1)
Random_letter = name[Random_number]
print(f' the letter: "{Random_letter}" belongs to the position "{Random_number+1}"')