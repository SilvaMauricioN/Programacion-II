import json 

#Creo diccionario apartir de un json
# with open ('Peliculas.json', encoding='utf-8') as archivo:
#     Peliculas = json.load(archivo)

#Modo Publico

#funcion para ver las ultimas 10 pelicuas subidas
def Ultimas_Peliculas():

    print("Ultimas Peliculas")
    print()
#calulo en que posicion empezar
    indice=len(Peliculas['Movies'])-10

    for i in Peliculas['Movies'][indice:]:
        print(i['titulo'])

#funcion para buscar peliculas por nombre de director
def Buscar_Director():

    director =input("Ingrese Nombre de Director: ")
    encontrado=False

    for i in Peliculas['Movies']:
        if director.upper() == i["director"].upper():
            print()
            print("Pelicula Dirigida: ",i["titulo"])
            print()
            print("Sinopsis: ",i["sinopsis"])
            encontrado=True
    if (encontrado==False):
        print("No se encontro director",director)


def modificar_peliculas():
    #en proceso
    return None

# Todos los Menus
def menu_inicial():
    print("------ Menu de Inicio ------\n"
    "1- Ingresar como usuario registrado.\n"
    "2- Ingresar en modo publico.\n"
    "3- Salir del programa.")
    opcion=control_de_entrada_usuario()
    return opcion

def menu_usuario():
    print("------ Menu Usuario ------\n"
    "1- Cargar pelicula.\n"
    "2- Editar una pelicula.\n"
    "3- Eliminar una pelicula.\n"
    "4- Volver al menu inicial.\n")
    opcion= control_de_entrada_usuario()
    return opcion


# Usuarios
def ingreso_usuario():
    usuario=input("Ingrese usuario: ")
    while True:
        contraseña=input ('Ingrese contaseña: ')
        try:
            contraseña=int(contraseña)
            break
        except ValueError:
            print("\033[1;31m"+"Error, ingrese un numero.\n"+'\033[0;m')

    return usuario, contraseña

def comprovar_usuario():
    print("en espera")

#Control de errores y verificación

def control_de_entrada_usuario():
    while True:
        entero=input ('Ingrese una opcion: ')
        try:
            entero=int(entero)
            return entero
        except ValueError:
            print("\033[1;31m"+"Error, ingrese un numero.\n"+'\033[0;m')

def Eliminar_Pelicula():

    titulo = input("Nombre de pelicula a eliminar: ")
    #Variable de Control
    encontrado=False

    with open ('Peliculas.json','r',encoding='utf-8') as archivo:
        Peliculas = json.load(archivo)

    for i in Peliculas['Movies']:

        if titulo.upper() == i['titulo'].upper():
            encontrado=True
            if len(i['criticas']) == 0:

                Peliculas['Movies'].remove(i)
                print(titulo, 'eliminada del registro')               

                with open ('peliculas.json', 'w', encoding='utf-8')as archivo:
                    json.dump(Peliculas, archivo, indent=4, ensure_ascii = False)

            else:    
                print('No se puede eliminar ', titulo,' incluye comentarios')
                
    if (encontrado==False):
        print('La pelicula no existe')
    