import Funciones as fc

fc.Buscar_Director
fc.Buscar_Director
opcion=0
while opcion!=3:
    opcion=fc.menu_inicial()
    #ingreso con usuario
    if opcion== 1:
        usuario,contraseña=fc.ingreso_usuario()
        #falta comprar si el usuario y la contraseña son correctos
    
    #ingreso en modo publico
    elif opcion== 2:
        print("opcion 2")
    elif opcion == 3:
        print("Fin del programa.")
    else:
        print("\033[1;31m"+"Error, ingrese un numero que coincida con las opciones disponibles.\n"+'\033[0;m')
