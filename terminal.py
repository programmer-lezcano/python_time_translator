import os
import logic

option = ''

def getToken():
    global option
    token = 0
    while option[0].isdigit():
        token = token * 10 + int(option[0])
        option = option[1:]
    return token

print("Ingrese la hora correctamente en minúscula y sin dejar espacios,")
print("por ejemplo; 2:15am , 12:1pm , 5:5am ...")
print("O ingrese exit para salir")

while option != 'exit':    
    
    option = input(">> ")

    if option == 'exit':
        break
    
    hour = getToken()
    option = option[1:]
    minute=getToken()

    print(logic.getTime(hour, minute, option))
