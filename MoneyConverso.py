#In this program, we'll convert COP into USD
COP = input("How many colombian pesos do you have? ")
COP_Val=float(COP) #We need to convert the string into a number, in this case a float
Conversion= (1/3977) # 1 USD/3977 COP
USD_Val = COP_Val * Conversion
URS_Val = round(USD_Val,2)
print(f'You have {COP_Val} COP = {USD_Val} USD.')