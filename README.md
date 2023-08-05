En este repositorio se mostrará una aplicación de Radar en Python.

■ Nombre del proyecto: Radar

■ Objetivos:

El presente proyecto es un radar, rastrea objetos a través de un sensor ultrasónico en un rango de 360 grados y 20 centímetros. Los datos obtenidos se envían por medio del puerto serial y son codificados y almacenados en listas para que posteriormente la computadora represente de manera gráfica y en formato texto la ubicación en coordenadas polares y cartesianas los objetos con respecto al sensor ultrasónico. La computadora también calculará las distancias entre los objetos rastreados. El alcance de este proyecto no involucra el diseño del radar y la programación en Arduino. Solamente se ven aspectos de la programación en Python.

■ Problema que resuelve: Una de las grandes problemáticas en la enseñanza aprendizaje es incentivar a los alumnos. Algunas estrategias que podemos usar es el trabajo a través de proyectos; pero para esto, el docente tiene que ser ejemplo, esto quiere decir que el docente tiene que involucrarse en proyectos o diseñar estos. Al presentarle al alumno un proyecto desarrollado por el profesor pudiera generar cierta curiosidad al alumno por saber más. Por tal motivo, una de las estrategias utilizadas es mostrar una aplicación práctica en donde se utilicen los aprendizajes a ver en la sesión, con el fin de que el en el alumno o la alumna se le despierte la motivación por conocer más. Se ejemplificará el uso estructuras de datos en una aplicación en diferentes lenguajes de programación (arreglos unidimensionales en Java y de listas en Python) a través de un proyecto titulado Radar. El presente proyecto es un radar, rastrea objetos a través de un sensor ultrasónico en un rango de 360 grados y 20 centímetros. Los datos obtenidos se envían por medio del puerto serial y son codificados y almacenados en listas para que posteriormente la computadora represente de manera gráfica y en formato texto la ubicación en coordenadas polares y cartesianas los objetos con respecto al sensor ultrasónico. La computadora también calculará las distancias entre los objetos rastreados. El alcance de este proyecto no involucra el diseño del radar y la programación en Arduino. Solamente se ven aspectos de la programación en Python.

■ Mención sobre el (los) lenguaje(s) utilizado(s) y argumentación sobre la elección de este lenguaje: Las estructuras de datos como los arreglos y listas se utilizan con frecuencia para optimizar la manipulación y almacenamiento de datos en todos los lenguajes de programación. En la enseñanza aprendizaje es un tema complejo, porque involucra conocimientos previos como el concepto de variables, tipos de datos, estructura de repetición for, variables de acumulación e incremento, en algunos casos los operadores unarios. Sin embargo, el programa de Python puede ayudar a ejemplificar de una manera mucho más fácil las listas y dar un paso en la comprensión de los índices dentro de los arreglos.

■ Descripción de lo que está simulando, analizando o demostrando.

El presente proyecto es un radar, rastrea objetos a través de un sensor ultrasónico en un rango de 360 grados y 20 centímetros. Los datos obtenidos se envían por medio del puerto serial y son codificados y almacenados en listas para que posteriormente la computadora represente de manera gráfica y en formato texto la ubicación en coordenadas polares y cartesianas los objetos con respecto al sensor ultrasónico. La computadora también calculará las distancias entre los objetos rastreados. El alcance de este proyecto no involucra el diseño del radar y la programación en Arduino. Solamente se ven aspectos de la programación en Python. Ver imagen 1 Radar ultrasónico (sensor ultrasónico, motor a pasos, placa Arduino).

■ Ejemplo básico de funcionamiento general, instrucciones de ejecución y uso.

Funcionamiento general:

El programa decodifica por medio de funciones para el manejo de cadenas de caracteres (búsqueda de caracteres y extracción de subcadenas). Al finalizar la decodificación se almacena los grados y la distancia de los objetos en listas.
De los datos obtenidos y almacenados (grados, distancia y objetos) se calcula las coordenadas cartesianas, para que posteriormente se represente un plano de manera gráfica.
Para graficar utilizamos la librería numpy y matplotlib. Utilizamos las listas de los objetos, grados, distancia y coordenadas para graficar.
También el programa en Python muestra los resultados de las coordenadas de cada objeto, la distancia con respecto al radar, los grados y el objeto.
Para continuar con el cálculo de las distancias entre los objetos, primero el programa hace todas las posibles combinaciones que puede tener cada objeto. Para esto creamos algunas listas que ayudaran a la generación de todas las posibilidades.
En el antepenúltimo paso, el programa calcula todas las distancias que puede existir entre los objetos.
Por último, el programa vuelve a graficar los objetos en el plano cartesiano.
Instrucciones de ejecución: El código que se presenta en la sección correspondiente se ejecuta en un solo bloque con el interprete de Jupyter Notebook, pero para su funcionamiento es necesario contar con el prototipo implementado en Arduino. Este anteproyecto incluye una placa Arduino, un motor a pasos que gire 360 grados, un sensor ultrasónico que gire 360 grados a través del motor a pasos y el código para identificar objetos en un rango de 360 grados a través de un sensor ultrasónico. El resultado final del anteproyect es una secuencia de caracteres que envía por medio del puerto serial de acuerdo en el siguiente orden y delimitado por caracteres: objeto, distancia, grados. El número de objeto identificado está delimitado por al inicio por una "O" (en mayúscula) y al final "o" (en minúscula). La distancia del objeto con respecto al sensor está delimitado por al inicio por una "D" (en mayúscula) y al final "d" (en minúscula). Los grados que guarda el objeto con respecto está delimitado por al inicio por una "G" (en mayúscula) y al final "g" (en minúscula). Si se desea implementar el código, es necesario tomar en consideración esta secuencia de caracteres por cada objeto encontrado. Veamos un ejemplo. Esta cadena "O1oD15dG45g" especifica las siguientes características: es el primer objeto localizado, se encuentra a 15 centímetros del sensor ultrasónico y 45 grados ha girado el motor. Cada uno de estos números se delimita con los caracteres correspondientes.

Uso: El radar se puede emplear en diversas asignaturas, Matemática, Estadística, Informática o Cibernética para ejemplificar alguno de los siguientes conceptos y procesos: coordenadas polares, coordenadas cartesianas (Matemáticas), distancia entre dos puntos (Matemáticas), combinaciones (Probabilidad), comprensión de estructuras de datos definida por el usuario entre ellas listas y arreglos (Informática o Cibernética).

Código: ################################################################################ ##Autor Plata Luna Iveth Vanessa ##Importamos la librería para el uso del puerto serial y time par el menejo del tiempo. import serial import time

##El programa se conecta al puerto serial COM6 a 9600 baudios dando tiempos de demora para recibir datos. serialArduino= serial.Serial("COM6", 9600 ) time.sleep(1)

#La variable cad almacenará de manera temporal los datos obtenidos del puerto serial. cad =""

#Definimos una lista para almacenar los datos del puerto serial. La variable i es de control. lista=[] i = 0

#Segmento de código que obtiene datos desde el puerto serial y lo transforma a ASCII. El bucle termina hasta que se obtene una 'f' while not(cad[0:1] == 'f') : cad = serialArduino.readline().decode('ascii') print(cad) if not(cad[0:1] == 'f'): lista.append(cad) i=i+1

print(cad)

print(lista)

print(i)

#La definición de estas listas es para almacenar los datos obtenidos del puerto serial, previamente se decodifican. objeto=[] distancia=[] grados=[]

#Definimos listas que servirán a decodificar la información del puerto serial. indexO = [] indexo= [] indexD = [] indexd = [] indexG = [] indexg = [] numDigO = [] numDigD = [] numDigG = [] objetoS=[] distanciaS=[] gradosS=[]

#Segmento de código que decodifica las cadenas de caracter obtenidas desde el puerto serial. #Se utiliza funciones para la manipulación de cadenas, como buscar un caracter y extraer subcadenas. #Los resultados obtenidos se almacenan en listas. for n in range(0, len(lista), 1): print(lista[n]) cadena=lista[n]

indexO.append(cadena.find('R'))
indexo.append(cadena.find('r'))
indexD.append( cadena.find('D'))
indexd.append(cadena.find('d'))
indexG.append(cadena.find('G'))
indexg.append(cadena.find('g'))

numDigO.append (indexo[n] - indexO[n] - 1)
numDigD.append (indexd[n] - indexD[n] - 1)
numDigG.append (indexg[n] - indexG[n] - 1)

objetoS.append(cadena[(indexO[n]+1):(indexO[n]+1+numDigO[n])])
distanciaS.append(cadena[(indexD[n]+1):(indexD[n]+1+numDigD[n])])
gradosS.append(cadena[(indexG[n]+1):(indexG[n]+1+numDigG[n])])
print("índice de caracteres") print(indexO) print(indexo) print(indexD) print(indexd) print(indexG) print(indexg) print("Número de dígitos") print(numDigO) print(numDigD) print(numDigG) print("Resultados") print(objetoS) print(distanciaS) print(gradosS)

#En este segmento de código se convierten las coordenadas polares a coordenadas cartesianas. #Para esta función utilizamos la libreria math. import math objeto = [] distancia = [] grados = []

for n in range(0, len(lista), 1):

objeto.append (int (objetoS[n]))
distancia.append (int (distanciaS[n]))
grados.append(int (gradosS[n]))
x=[] y=[] for n in range(0, len(lista), 1): x.append(distancia[n] * math.cos(math.radians(grados[n]))); y.append(distancia[n] * math.sin(math.radians(grados[n]))); print(objeto) print(distancia) print(grados) print(x) print(y)

#Para graficar utilizamos las librerias mumpy y matplotlib. import numpy as np import matplotlib.pyplot as plt

#Es importante convertir la lista a un tipo arreglo para poder graficar. xnp = np.array(x) ynp = np.array(y) print(xnp) print(ynp)

#Configuración del gráfico

fig, ax = plt.subplots(figsize = (20,20))

plt.xlabel("x") plt.ylabel("y") plt.xlim(-20,20) plt.ylim(-20,20) plt.title("Radar")

plt.hlines(0,-20,20, color="blue") plt.vlines(0,-20,20, color="blue")

for n in range(0, len(lista), 1): plt.plot([0,x[n]],[0,y[n]])

#Configuración del color color = np.where((xnp<= 0) , "red", "blue") color = np.where((ynp <= 0) , "green", "purple")

plt.scatter(xnp, ynp, c=color, label=color, s=500, marker=r'$\heartsuit$', alpha=0.4 ) plt.plot(xnp, ynp, linestyle="dotted") plt.plot(xnp, ynp, linestyle="dashdot") plt.plot(xnp, ynp, linestyle="dashed") plt.show()

#En este segmento de código se despliegan los datos obtenidos desde el puerto serial, objeto, grados, distancia. #También se imprime las coordenadas cartesianas. for n in range(0, len(lista), 1): print("Objeto: " , objeto[n]) print("Distancia en la que se encuentra el objeto: ", distancia[n]) print("Grados en la que se encuentra el objeto: " , grados[n]) print("Coordenadas en el plano cartesiano: [ " , x[n] , " , " , y[n] , " ]") print("\n")

#Para calcular la distancia entre dos objetos es importante crear todas las posibles combinaciones entre los objetos. #Generamos algunas listas para las posibles combinaciones. objetos=[] combinaciones=[] serieObjetos=[]

for n in range(1, len(lista)+1, 1): objetos.append(n)

for m in range(1, len(objetos)+1, 1): for n in range(1, len(objetos)+1, 1): serieObjetos.append(m)

for m in range(1, len(lista)+1, 1): for n in range(1, len(lista)+1, 1): combinaciones.append(n)

print("objetos: ",objetos) print("Serie objetos: ", serieObjetos) print("combinaciones: ",combinaciones)

#Para continuar con las posibles combinaciones, llenamos las listas con todas las posibilidades. posObjetosXY1=[] posObjetosXY2=[] combObjetosXY1=[] combObjetosXY2=[] combX1=[] combX2=[] combY1=[] combY2=[]

combDistanciaObjetos=[]

for n in range(0, len(serieObjetos), 1):
print("Objeto: ",serieObjetos[n],"Posición objeto: ", objeto.index(serieObjetos[n]),"Coordenada x: ",x[objeto.index(serieObjetos[n])],"Coordenada y:",y[objeto.index(serieObjetos[n])]) posObjetosXY1.append(objeto.index(serieObjetos[n])) combX1.append(x[objeto.index(serieObjetos[n])])
combY1.append(y[objeto.index(serieObjetos[n])]) combObjetosXY1.append(serieObjetos)

print("\n") for m in range(0, len(combinaciones), 1): print("Objeto: ", combinaciones[m],"Posición objeto: ", objeto.index(combinaciones[m]),"Coordenada x: ",x[objeto.index(combinaciones[m])],"Coordenada y:",y[objeto.index(combinaciones[m])]) posObjetosXY2.append(objeto.index(combinaciones[m])) combX2.append(x[objeto.index(combinaciones[m])]) combY2.append(y[objeto.index(combinaciones[m])]) combObjetosXY2.append(combinaciones)

print("\n")

print("Combinación objetosXY1 : ",combObjetosXY1) print("Posición objetosXY1 : ",posObjetosXY1) print("x1:", combX1) print("y1:", combY1) print("\n")

print("Combinación objetosXY2 : ",combObjetosXY2) print("Posición ObjetosXY2: ",posObjetosXY2) print("x2:", combX2) print("y2:", combY2)

#En este segmento de código se calcula la distancia de todas las posibles combinaciones entre los objetos y #se despliegan los resultados. print(objetos) print(x) print(y) print("\n") print("\n") for m in range(0, len(combinaciones), 1): print("\n") print("\n") combDistanciaObjetos.append(float(math.sqrt((combX1[m]-combX2[m])**2+(combY1[m]-combY2[m])**2))) print("Distancia: ", float(math.sqrt((combX1[m]-combX2[m])**2+(combY1[m]-combY2[m])**2)) ) print("x1: ",combX1[m]," x2:", combX2[m], ) print("y1: ",combY1[m]," y2:",combY2[m]) print("\n") print("Objeto: ",serieObjetos[m]) print("Posición objeto: ", objeto.index(serieObjetos[m])) print("Coordenada x: ",x[objeto.index(serieObjetos[m])]) print("Coordenada y: ",y[objeto.index(serieObjetos[m])]) print("\n") print("Objeto: ", combinaciones[m]) print("Posición objeto: ", objeto.index(combinaciones[m])) print("Coordenada x: ",x[objeto.index(combinaciones[m])]) print("Coordenada y:",y[objeto.index(combinaciones[m])])

print(combDistanciaObjetos) print("\n")

#Volvemos a graficar.

fig, ax = plt.subplots(figsize = (20,20))

plt.xlabel("x") plt.ylabel("y") plt.xlim(-30,30) plt.ylim(-30,30) plt.title("Radar")

plt.hlines(0,-30,30, color="blue") plt.vlines(0,-30,30, color="blue")

for n in range(0, len(lista), 1): plt.plot([0,x[n]],[0,y[n]])

#Configuración del color color = np.where((xnp<= 0) , "red", "blue") color = np.where((ynp <= 0) , "green", "purple")

plt.scatter(xnp, ynp, c=color, label=color, s=500, marker=r'$\heartsuit$', alpha=0.4 ) ax.plot(combX1,combY1, marker='') ax.plot(combX2,combY2, marker='')

ax.plot(combX1,combY1, marker='') ax.plot(combX2,combY2, marker='') plt.show() ################################################################################

■ Tema que ayuda a comprender Resuelve problemas que involucren el uso de los arreglos unidimensionales en los métodos de una Clase. El proyecto se puede implementar en diversas asignaturas me Matemática, Estadística, Informática o Cibernética para ejemplificar alguno de los siguientes conceptos y procesos: coordenadas polares, coordenadas cartesianas (Matemáticas), distancia entre dos puntos (Matemáticas), combinaciones (Probabilidad), listas (Informática o Cibernética).

■ Justificación de cómo ayuda al alumno a comprender el tema El docente al mostrar algunos ejemplos en donde se usan lista podría ayudar al alumno a reflexionar sobre la utilidad de esta estructura de datos definida por el usuario. También a través de la comparación entre ambos lenguajes con respecto a los arreglos (en Java) y listas (en Python) los alumnos pueden reflexionar sobre el manejo de estas estructuras por medio de sus índices (listas y arreglos).
