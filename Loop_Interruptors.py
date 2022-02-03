# we start with good praxis
def run():
    # # This code only will print even numbers
    # for i in range(1000):
    #     if i % 2 != 0:
    #         continue # This line skips each iteration 
    #                 # where the result is not Zero with Odd numbers
    #     print(i)
    # import random as rnd
    # for i in range(100):
    #     print(i)
    #     random_number= rnd.randint(1,100)
    #     if i == random_number:
    #         break # This line will stop the loop
    #                 #when the counter reaches a random number
    #                 #into the range
    # print(f'The stop number was: {random_number}')

    Palabra = input("Type a word or a phrase: ")
    Found = False
    position=0
    for i in Palabra:
        # We need to find a character called "@"
        position+=1
        if i == "@":
            Found = True
            break
    if Found == True:
        # we found the character
        print(f'We found the character "@" in the position: {position}')
    else:
        # we didn't found the character
        print('Character "@" not found')


# Entry point
if __name__ == '__main__':
    run()