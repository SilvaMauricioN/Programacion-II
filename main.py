import Funciones as fc
import requests

opcion=0
while opcion!=3:
    opcion=fc.menu_inicial()
    #ingreso con usuario
    if opcion== 1:
        validacion=fc.ingreso_usuario()
        if validacion==True:
            opcion=fc.menu_usuario()
            if opcion==1:
                print("hola")
        else:
            print("Algun dato esta mal")
# falta comprar si el usuario y la contraseña son correctos
#ingreso en modo publico
    elif opcion== 2:
        print("opcion 2")
    elif opcion == 3:
        print("Fin del programa.")
    else:
        print("\033[1;31m"+"Error, ingrese un numero que coincida con las opciones disponibles.\n"+'\033[0;m')

