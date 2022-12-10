import Funciones as fc
import requests

opcion=0
while opcion!=3:
    opcion=fc.menu_inicial()
    #ingreso con usuario
    if opcion== 1:
        usuario,contraseña=fc.ingreso_usuario()
        if usuario==False and contraseña==False:
            print("Todo mal")
        else:
            print(usuario,contraseña)
# falta comprar si el usuario y la contraseña son correctos
#ingreso en modo publico
    elif opcion== 2:
        print("opcion 2")
    elif opcion == 3:
        print("Fin del programa.")
    else:
        print("\033[1;31m"+"Error, ingrese un numero que coincida con las opciones disponibles.\n"+'\033[0;m')

