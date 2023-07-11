import os
def llenarMatriz(mat):
    p=1
    for i in range(10):
        for j in range(4):
            mat[i,j]=p
            p+=1
def ValiOp(op):
    while(True):
        try:
            op=int(input("   Elija Opción   "))
            if(op>=1 and op<=5):
                break
            else:
                print("Debe ingresar una opción entre 1 y 5")
        except ValueError:
                print("Debe ser un número entero")
    return op
def mostrarDisponibles(numPiso):
    os.system("cls")
    for i in range(10):
        print("\n") #salto de linea
        for j in range(4):
            if(j==1):
                print("\t",numPiso[i,j], end="        ")
            else:
                print("\t",numPiso[i,j], end="    ")
    print("\n\n")
def ValiDpto():
    numDpto=0
    while True:
        try:
            numDpto=int(input(" Ingrese departamento que desea comprar 1-4 "))
            if(numDpto>=1 and numDpto<=4):
                break
            else:
                print("Error, el número de piso debe ser entre 1 y 4!!!")
        except ValueError:
            print("Error... Ingrese piso entre 1 y 4")
            return numDpto
def buscarDisponible(numPiso,numDpto):
    for x in range(10):
        for i in range(4):
            if (numDpto==numPiso[x,i]):
                return True
    return False 
def comprarDpto(numPiso,numDpto):
    for x in range(10):
        for i in range(4):
            if (numPiso[x,i]==numPiso):
                numPiso[x,i]="X"      #el departamento esta vendido
                if i=="A":
                    pago=3.800
                elif i=="B":
                    pago=3.000
                if i=="C":
                    pago==2.800
                elif i=="D":
                    pago=3.500
    return pago 
def Compradores(numPiso,numDpto):
              

