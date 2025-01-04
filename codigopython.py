## este nuevo tablero de trabajo vamos a practicar mas bucles. vamos a intentar hacer ejercicios mas retadores e ir 
## subiendo el nivel hasta llegar a ser cracks en esto. SIIIU

#Ejercicio: Adivina el número mágico con pistas
#Escribe un programa donde el usuario debe adivinar un número mágico entre 1 y 100. 
# El programa debe proporcionar pistas para ayudar al usuario a acercarse al número mágico. Las reglas son:
#1 vamos a generar un numero entre 0 y 100 aleatoriamente 

import random     #importamos la libreria random
numeroMagic=random.randint(0,100)   #definimos el numero aleatorio entre 0 y 100
intentos=0   ## el usuario tiene  intentos, empezamos con el intento 0
MaxIntentos=7
numeroParticipante=int(input('por favor ingresa un numero entre 0 y 100: '))
while intentos <MaxIntentos : 
    intentos+=1
    if numeroParticipante==numeroMagic:
        print(f'Felicidades! Has encontrado el número mágico en  {intentos}')
        break
    elif numeroParticipante<numeroMagic:
        print('el numero magico es mayor')
    else:
        print('el numero magico es menor')
    if intentos < MaxIntentos:
        numeroParticipante = int(input('Por favor, ingresa un nuevo número: '))
    else:
        print(f'Lo siento, se acabaron tus intentos. El número mágico era {numeroMagic}.')
       
    