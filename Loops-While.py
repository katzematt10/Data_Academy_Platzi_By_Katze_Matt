def run():
    Limit = input("Define the maximun number: ")
    Limit = int(Limit)
    Power = 0
    i = 0
    while (Power < Limit):
        i += 1
        Power = 2 ** (i)
        print(f'2^{i}: {Power}') 


if __name__ == "__main__": # Activation code
    run()


