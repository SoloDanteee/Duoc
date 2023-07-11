import os
import numpy as np
import funcionesET as fn
departamento=np.empty([10,4], type(int))
fn.llenarMatriz(departamento)
os.system("cls")
op=0
dpto=0
while(op!=5):
    os.system("cls")
    print("                  Casa Feliz                                      ")
    print("        *********************                                     ")
    print("1.	Comprar Departamento 	                           ")
    print("2.	Mostrar Departamentos Disponibles                  ")
    print("3.	Ver listado de compradores                         ")
    print("4.	Mostrar ganancias totales                          ")
    print("5.	Salir                                              ")
    op=fn.ValiOp(op)
    if(op==1):
        fn.mostrarDisponibles(departamento)
        departamento=fn.ValiDpto
        os.system("pause")

    if(op==2):
        fn.mostrarDisponibles(departamento)
        os.system("pause")
    if(op==5):
        print("Gracias por utilizar mi programa:) / Dante Cannobbio 11/7/2023 ")
    