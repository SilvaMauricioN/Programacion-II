import requests
#funciones de Control

def Existe_Pelicula(Pelicula):
    Datos = requests.get("http://127.0.0.1:5000/Peliculas")
    Peliculas = Datos.json()

    movie=[]
    for i in Peliculas["Movies"]:
        if i['titulo'].upper() == Pelicula.upper():      
            
            movie.append(i['titulo'])
    
    if len(movie)==1:
        return(True)
    else:
        return(False)


#Modo Publico
#funcion para ver las ultimas 10 pelicuas subidas
def Ultimas_Peliculas():

    Datos = requests.get("http://127.0.0.1:5000/Peliculas")
    Peliculas = Datos.json()
    
    print("Ultimas Peliculas")
    print()
    #calulo en que posicion empezar
    indice=len(Peliculas['Movies'])-10
    for i in Peliculas['Movies'][indice:]:
        print()
        print(i['titulo'])
        print()
        print(i['sinopsis'])

#funcion para buscar peliculas por nombre de director
def Buscar_Director():

    director =input("Ingrese el Nombre del Director: ")
    Datos = requests.get("http://127.0.0.1:5000/Peliculas/"+director)
    print (Datos.url)
    
    Peliculas= Datos.json()
    print(director)

    if type(Peliculas) == dict:

        for i in Peliculas['peliculas']:
            print(i)
    else:
        print(Peliculas)

def Buscar_Pelicula_Portada():
    Datos = requests.get("http://127.0.0.1:5000/Portada/Peliculas")
    Portada = Datos.json()
    for i in Portada:
        print(i["titulo"])
        print(i["img"])

def Lista_Directores():
    print("Estos son los directores presentes en la plataforma.\n")
    datos=requests.get("http://127.0.0.1:5000/Directores")
    directores=datos.json()
    for i in directores["directores"]:
        print(i["nombre_director"])
    
#Funcion generos

def Generos():
    print("Estos son los generos presentes en la plataforma.\n")
    datos=requests.get("http://127.0.0.1:5000/Generos")
    generos=datos.json()
    for i in generos["Generos"]:
        print(i["genero_pelicula"])
#Modificar pelicula existente
def modificar_peliculas():
    
    peliculas = input("Ingrese el Nombre de la Pelicula a Modificar: ")

    Verificar = Existe_Pelicula(peliculas)

    if Verificar:
        pelicula=input("Ingrese nuevo nombre: ")
        año = input("Ingrese el año de la pelicula: ")
        director = input("Ingrese nombre del Director: ")
        genero = input("Ingrese genero de la pelicula: ")
        sinopsis = input ("Ingrese la sinopsis: ")
        img = input("Url de la imagen de la pelicula: ")
        duracion = input("Ingrese duracion de la pelicula: ")
        reparto = input("Ingrese reparto de la pelicula: ")

        pelicula_a_modificar ={
            "id":"",
            "titulo":"",
            'año' :"",
            'director':"",
            'genero':"",
            'sinopsis':"",
            'img':"",
            'duracion':"",
            'reparto':""
                }
        pelicula_a_modificar['titulo']=pelicula
        pelicula_a_modificar['año']=año
        pelicula_a_modificar['director']=director
        pelicula_a_modificar['genero']=genero
        pelicula_a_modificar['sinopsis']=sinopsis
        pelicula_a_modificar['img']=img
        pelicula_a_modificar['duracion']=duracion
        pelicula_a_modificar['reparto']=reparto
        
        Datos = requests.put("http://127.0.0.1:5000/Modificar/"+peliculas, json=pelicula_a_modificar)
        print(Datos.url)
        print(pelicula_a_modificar)
        mensaje=Datos.json()
        print(mensaje)
    else:
        print("La Pelicula No Existe")

# Todos los Menus
def menu_inicial():
    print("------ Menu de Inicio ------\n"
    "1- Ingresar como usuario registrado.\n"
    "2- Ingresar en modo publico.\n"
    "3- Salir del programa.")
    opcion=control_de_entrada_usuario()
    return opcion

def menu_usuario():
    print()
    print("------ Menu Usuario ------\n"
    "1- Lista de Directores.\n"
    "2- Lista de Generos.\n"
    "3- Peliculas del director. \n"
    "4- Pelicualas con Portada.\n"
    "5- Cargar Peliculas \n"
    "6- Modificar pelicula.\n"
    "7- Eliminar una pelicula.\n"
    "8- Volver al menu inicial.\n")
    opcion= control_de_entrada_usuario()
    return opcion


# Usuarios
def ingreso_usuario():
    usuario=input("Ingrese usuario: ")
    contraseña=input ('Ingrese contaseña: ')
    validacion=comprovar_usuario(usuario,contraseña)
    if validacion==True:
        return True
    else:
        return False

def comprovar_usuario(usuario,contraseña):
    respuesta=requests.get("http://127.0.0.1:5000/Usuarios")
    diccionario=respuesta.json()
    for i in diccionario["Usuarios"]:
        if i["User name"] == usuario and i["Contraseña"] == contraseña:
            return True
    return False
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
    
    Datos = requests.delete("http://127.0.0.1:5000/Eliminar/"+titulo)
    mensaje=Datos.json()
    print(mensaje)
    
#modificar_peliculas()

def Portada():

    #director =input("Ingrese el Nombre del Director: ")
    Datos = requests.get("http://127.0.0.1:5000/Portadas/Peliculas")
    print (Datos.url)
    
    Peliculas= Datos.json()

    for i in Peliculas:
        print(i['titulo'])
        print(i['img'])

Portada()
#Buscar_Director()
