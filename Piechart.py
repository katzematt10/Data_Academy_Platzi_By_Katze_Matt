import matplotlib.pyplot as plt
import random as rnd
x= [rnd.random(),rnd.random(),rnd.random(),rnd.random()]
labeks=["Python","Java","C", "C++"]
plt.pie(x,labels=labeks)
plt.show()

