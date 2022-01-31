# This is the way to create string slides in python

# Method 1 - Basic cut
# string[initial:final]
name = input("Type your name: ")
Slide = name[1:7]
print("Method 1")
print(Slide)

# Method 2 - Extracting slides ignoring one border
# String[:final] - This extracts all the string from the beggining
#                   to the "final" position
# String[initial:] - This extracts all the string from the "initial"
#                   position to the final.
print("Method 2")
Slide2 = name[:10]
print(Slide2)

print("Method 3")
Slide3 = name[5:]
print(Slide3)

# Method 4 - Extracting by steps
# String[initial:final:step] - Extracting from a position to another but
#                               not one by one, we can specify the steps

print("Method 4")
Slide4 = name[7:20:2]
print(Slide4)


# Method 5 - extracting upside down.
# String[initial:final:-1]
print("Method 5")
Slide5 = name[::-1]
print(Slide5)

