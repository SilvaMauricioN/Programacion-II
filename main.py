import Funciones as fc
import requests
import os

opcion=0
os.system("cls")
fc.Control_servidor()
while opcion!=9:
    opcion=fc.menu_inicial()
    #ingreso con usuario
    if opcion== 1:
        validacion=fc.ingreso_usuario()
        while True:
            if validacion==True:
                opcion=fc.menu_usuario()
                if opcion==1:
                    fc.Lista_Directores()
                elif opcion==2:
                    fc.Generos()
                elif opcion==3:
                    fc.Buscar_Director()
                elif opcion==4:
                    fc.Buscar_Pelicula_Portada()
                elif opcion==5:
                    fc.Cargar_Pelicula()
                elif opcion==6:
                    fc.Modificar_Pelicula()
                elif opcion==7:
                    fc.Cargar_Comentario()
                elif opcion==8:
                    fc.Eliminar_Pelicula()
                elif opcion==9:
                    break
            else:
                print("Algun dato esta mal")
                break
#ingreso en modo publico
    elif opcion== 2:
        
        fc.Ultimas_Peliculas()
    elif opcion == 3:
        print("Fin del programa.")
    else:
        print("\033[1;31m"+"Error, ingrese un numero que coincida con las opciones disponibles.\n"+'\033[0;m')