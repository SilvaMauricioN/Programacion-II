import Funciones as fc
import requests

opcion=0
while opcion!=3:
    opcion=fc.menu_inicial()
    #ingreso con usuario
    if opcion== 1:
        validacion=fc.ingreso_usuario()
        while True:
            if validacion==True:
                opcion=fc.menu_usuario()
                if opcion==1:
                    print("hola")
                elif opcion==2:
                    print("")
                elif opcion==3:
                    fc.modificar_peliculas()
                elif opcion==4:
                    fc.Eliminar_Pelicula()
                elif opcion==5:
                    break
            else:
                print("Algun dato esta mal")
#ingreso en modo publico
    elif opcion== 2:
        
        fc.Ultimas_Peliculas()
    elif opcion == 3:
        print("Fin del programa.")
    else:
        print("\033[1;31m"+"Error, ingrese un numero que coincida con las opciones disponibles.\n"+'\033[0;m')

