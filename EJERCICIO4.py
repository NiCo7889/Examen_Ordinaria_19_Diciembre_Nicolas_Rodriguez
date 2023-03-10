"""
Su tarea es escribir una función llamada do_math que reciba un solo argumento. Este argumento es una cadena que contiene varios números delimitados por espacios en blanco. Cada número tiene una sola letra del alfabeto en algún lugar dentro de él.

Ejemplo: "24z6 1x23 y369 89a 900b"

Como se muestra arriba, esta letra del alfabeto puede aparecer en cualquier lugar dentro del número. Tienes que extraer las letras y ordenar los números según sus letras correspondientes.

Ejemplo: "24z6 1x23 y369 89a 900b" se convertirá 89 900 123 369 246 (ordenados según la letra del alfabeto)

Aquí viene la parte difícil, ahora tienes que hacer una serie de cálculos sobre los números que has extraído.

La secuencia de cálculos es + - * /. Las reglas matemáticas básicas NO se aplican, debe hacer cada cálculo exactamente en este orden.
Esto tiene que funcionar para cualquier tamaño de números enviados (después de la división, volver a la suma, etc.).
En el caso de letras del alfabeto duplicadas, debe organizarlas de acuerdo con el número que apareció primero en la cadena de entrada.
Recuerde también redondear la respuesta final al entero más cercano.
Puedes escribir una función llamada do_math que realice los cálculos descritos en el enunciado del problema. La función debería tomar una sola cadena como argumento y devolver un número entero como resultado. Para resolver el problema, la función puede seguir los siguientes pasos:

Separe la cadena de entrada en una lista de números utilizando el espacio como separador.
Para cada número en la lista, extraiga la letra del alfabeto que se encuentra en el número y almacénela en un diccionario junto con el número entero correspondiente.
Ordenar el diccionario según las letras del alfabeto que se han extraído de los números.
Realizar los cálculos especificados en el enunciado utilizando los números ordenados del diccionario. Redondear el resultado final al entero más cercano y devolverlo como resultado de la función.
Ejemplos:

"24z6 1x23 y369 89a 900b" = 89 + 900 - 123 * 369 / 246 = 1299

"24z6 1z23 y369 89z 900b" = 900 + 369 - 246 * 123 / 89 = 1414

"10a 90x 14b 78u 45a 7b 34y" = 10 + 45 - 14 * 7 / 78 + 90 - 34 = 60

¡Buena suerte y que el CÓDIGO te acompañe!
"""

from ast import main 

def do_math(string):
    numeros = string.split(" ")
    numeros_1 = []
    letras = []
    for i in numeros:
        numeros_1.append(int(i[:-1]))
        letras.append(i[-1])
    numeros_1.sort()
    numeros = []
    for i in range(len(numeros_1)):
        numeros.append(numeros_1[i] + letras[i])
    
    cadena = ''
    for i in numeros:
        cadena += i + ' '
        return cadena

print(do_math("24z6 1x23 y369 89a 900b"))

if __name__ == '__main__':
    main()