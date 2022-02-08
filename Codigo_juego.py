import random as rnd
# Inicia ejercicio

def run():
  Intentar = True
  Costo = 100
  Premio=0
  while Intentar == True:
    # Se dicen los numeros 
    Num1 = 0
    Num2 = 0
    while Num1 == Num2:
      Num1 = rnd.randint(2,8)
      Num2 = rnd.randint(2,8)
      if Num1  == Num2:
        print("Los números son iguales, por favor vuelve a intentarlo.")
    #Acá los números son diferentes, vamos a mirar los aleatorios:
    Num3 = 0
    Num4 = 0
    while Num3 ==  Num4:
      Num3 = rnd.randint(2,8)
      Num4 = rnd.randint(2,8)
    
    #Acá los numeros aleatorios no son iguales, se mira si premia o no:
    #premio 1
    if ((Num1 == Num3) or (Num1 == Num4)) and ((Num2 == Num3) or (Num2 == Num4)):
      #gana premio 1
      Premio = 100000
      Intentar = False
    elif (Num1 == Num3) or (Num1 == Num4) or (Num2 == Num3) or (Num2 == Num4):
      if (Num1 == Num3)  or (Num1 == Num4):
        NumGana = Num1
      elif (Num2 == Num3) or (Num2 == Num4):
        NumGana = Num2
      else:
        print("NA")
      #Gana el premio 2
      Premio = NumGana * 100
      Intentar = False
    else:
      Suma1 = Num1 + Num2
      Suma2 = Num3 + Num4
      if Suma1 == Suma2:
        #Gana premio 3
        Premio =0
        Intentar = True

    Utilidad = Premio - Costo

    return Utilidad   




if __name__ == "__main__":
  Intentos = int(input("Digita los intentos: "))
  Ganancia = 0
  GananciaAcu=0
  for i in range(Intentos):
    Ganancia = run()
    GananciaAcu += Ganancia
  
  GananciaProm = GananciaAcu/Intentos
  print("La ganacia promedio es: " + str(GananciaProm) + "$")