# for i in "Iterative_variable":
#     print(i)
import random as rnd
def run():
    for i in range(5,20):
        print(rnd.random()+i)


def run2():
    Name = input("Type your name: ")
    j = 0
    for i in Name:
        j += 1
        print(f'Letter {j}: {i}')

if __name__ == '__main__':
    run()
    run2()