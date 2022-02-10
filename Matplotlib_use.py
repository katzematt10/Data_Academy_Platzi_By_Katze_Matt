# MatPlotLibe Usage
import matplotlib.pyplot as plt
import random as rnd
x = []
y = []
#Creo datos
for i in range(50):
    x.append(2014+i)
    y.append(10+ (50-10)*rnd.random())

plt.plot(x, y, marker='o', linestyle='--', color='g')
plt.xlabel('Years')
plt.ylabel('Revenue (Millions)')
plt.title('Revenue per year')
plt.show()

#############################################################
import matplotlib.pyplot as plt
import random as rnd
y=[]

for i in range(3):
    Valor=0
    ValorAcu=0
    for j in range(100):
        Valor= 200+(500-200)*rnd.random()
        ValorAcu += Valor
    ValorProm = ValorAcu/100
    y.append(ValorProm)

x = ['Data Science', 'Web Development', 'Mobile Development']
plt.ylabel('Revenue (Millions)')
plt.title('Revenue per year')

plt.bar(x, y)
plt.show()

###############################################################3
import matplotlib.pyplot as plt
import random as rnd
import numpy as np

prices =[]
bins =[]
Mu = 4
for i in range(3):
    
    Valor = (-Mu)*(np.log(1-rnd.random()))
    prices.append(Valor)
    bins.append(1000*(i+1))
print(prices)

plt.hist(prices, bins)
plt.show()

##########################################3
import matplotlib.pyplot as plt
import random as rnd
import numpy as np

x = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
y = [1, 2, 5, 10, 21, 40, 54]

plt.scatter(x, y)

plt.show()