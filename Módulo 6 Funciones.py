##Bruno González, Ricardo Yadel Murillo Pérez y Plata Luna Iveth Vanessa
#Codificar de manera colaborativa mediante la plataforma replit.com:

# A)Codifica un programa que ejecute tres funciones:
# 	1. La función de fibonacci. Dado un número entero n, calcular los n-ésimo término de la cadena 
# 	2. La evaluacion del polinomio f(x) = x³ + 2x² - x + 5. Dado un valor de x devolver el valor de f(x) correspondiente.
# 	3. Crear una función que lea una cadena de caracteres y una subcadena. La función devolverá "Si" dado el caso que la 
# 	   subcadena esté en la cadena. "No" en caso contrario.
 
 #B)Sigue las buenas prácticas sugeridas para codificar funciones en python.
 
 #C)Elabora un menú inicial para elegir la función que se va a ejecutar.
import matplotlib.pyplot as plt
import numpy as np

#Fibonacci    
def fibonacci(n):
  if n == 0:
   return 0
  if n == 1:
    return 1
  return (fibonacci(n-1) + fibonacci(n-2))

#polinomio solo

def poli(x):
  #print ("el valor de x ",x)
    
  print ("el valor delpolinomio ")
  return (x**3)+2*(x**2)-x+5

#subcadena

def sub(cadena, subcadena):

  if (cadena.find(subcadena)!=-1):
    mensaje = "Se encontró la subcadena"
    return mensaje
  else:
    mensaje = "No se encontró"
    return mensaje


##Función menú. En esta función se muestra el menú del usuario y se recopila la elección. La función devuelve el valor elegido
def menu():
  print('Bienvenido')
  print('Elige alguna delas siguientes opciones: ')
  print('1.- Función de Fibonacci')
  print('2.- Evaluación de un polinomio')
  print('3.- Leer una cadena de caracteres')
  print('4.- Salir')
  eleccion = input()
  return eleccion

#Programa principal
while (True):
  select = int (menu())
  if select == 1:
    print('Elegiste Fibonacci')
    #if __name__ == '__main__':
    print("Favor de proporcionar un número:")
    n = int(input())
    resultado=fibonacci(n)
    print(resultado)
  
  if select == 2:
    print('Elegiste Polinomio')
    print("Favor de proporcionar el valor de x")
    x=int(input())
    resultado = poli(x)
    print(resultado)
    
  if select == 3:
    print('Elegiste búsqueda de subcadena')
    print("Dame la cadena:")
    cadena=input()
    print("Dame la subcadena:")
    subcadena = input()
    print(sub(cadena, subcadena))

    
  if select == 4:
    print('Adiós')
    break
    
  else:
    print('Opción inválida')
    continue
