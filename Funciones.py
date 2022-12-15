import requests
from requests import Timeout

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
    Datos = requests.get("http://127.0.0.1:5000/Portadas/Peliculas")
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
    validacion=comprobar_usuario(usuario,contraseña)
    if validacion==True:
        return True
    else:
        return False

def comprobar_usuario(usuario,contraseña):
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

def Verificar_ID(pelicula):

    Datos = requests.get("http://127.0.0.1:5000/Peliculas")
    Peliculas = Datos.json()

    for i in Peliculas['Movies']:
        if i['titulo'].upper() == pelicula.upper():
            ID = i['id']

    return ID

def Modificar_Pelicula():

    pelicula = input("Ingrese el Nombre de la Pelicula a Modificar: ")
    Verificar = Existe_Pelicula(pelicula)

    if Verificar:
        Datos = requests.get("http://127.0.0.1:5000/Peliculas")
        Peliculas = Datos.json()
        opcion=0
        ID=Verificar_ID(pelicula)
        while opcion != 9:
            print()
            print ('1) Modificar Titulo pelicula ' )
            print ('2) Modificar Año')
            print ('3) Modificar Director')
            print ('4) Modificar genero')
            print ('5) Modificar Sinopsis')
            print ('6) Modificar Portada de la pelicula')
            print ('7) Modificar Duracion de pelicula')
            print ('8) Modificar Reparto')
            print ('9) Salir')
            opcion = input ('Ingrese una opcion:  ')
                
            if opcion == '1':
                nuevo_titulo=input("Nombre de la pelicula:")
                for i in Peliculas['Movies']:
                    if i['id'] == ID:
                        i['titulo'] = nuevo_titulo
                 
            elif opcion == '2':

                nuevo_año=input("Año de la pelicula:")
                for i in Peliculas['Movies']:
                    if i['id'] == ID:
                        i['año'] = nuevo_año

            elif opcion =='3':

                nuevo_director=input("director de la pelicula:")
                for i in Peliculas['Movies']:
                    if i['id'] == ID:
                        i['director'] = nuevo_director
            
            
            elif opcion =='4':

                nuevo_genero=input("genero de la pelicula:")
                for i in Peliculas['Movies']:
                    if i['id'] == ID:
                        i['genero'] = nuevo_genero

            
            elif opcion =='5':

                nuevo_sinopsis=input("Sinopsis de la pelicula:")
                for i in Peliculas['Movies']:
                    if i['id'] == ID:
                        i['sinopsis'] = nuevo_sinopsis

            
            elif opcion =='6':

                nuevo_img=input("Url de imagen de pelicula:")
                for i in Peliculas['Movies']:
                    if i['id'] == ID:
                        i['img'] = nuevo_img
            
            
            elif opcion =='7':

                nuevo_duracion=input("Tiempo de duracion de la pelicula:")
                for i in Peliculas['Movies']:
                    if i['id'] == ID:
                        i['duracion'] = nuevo_duracion

            
            elif opcion =='8':


                reparto= []
                op=0

                while op != 2:

                    print("1) Nuevo actor y personaje")
                    print("2) Salir")
                    op=input("Ingrese opcion: ")

                    if op == '1':

                        actor=input("Nombre del Actor: ")
                        personaje=input("Nombre del Personaje: ")

                        reparto.append({

                            "actor":actor,
                            "personaje":personaje
                            })
                    
                    elif op =='2':
                        break
              
                for i in Peliculas['Movies']:
                    if i['id'] == ID:
                        i['reparto'] = reparto

            elif opcion == '9':
                break
        

        Datos = requests.put("http://127.0.0.1:5000/Modificar/Peliculas", json=Peliculas)
       
        mensaje=Datos.json()
        print(mensaje)
    else:
        print("La pelicula no existe")

def Cargar_Comentario():
    pelicula=input("Nombre de la Pelicula: ")
    Verificar=Existe_Pelicula(pelicula)

    if Verificar == True:

        comentario={
            "id_usuario":"",
            "nombre":"",
            "opinion":""
            }

        usuario=input("Ingrese ID de Usuario:")
        nombre=input("Ingrese Nombre: ")
        opinion=input("Ingrese su opinion: ")

        comentario['id_usuario']=usuario
        comentario['nombre']=nombre
        comentario['opinion']=opinion

        Datos_Comentarios = requests.post('http://127.0.0.1:5000/Comentarios/'+pelicula, json=comentario)
        mensaje=Datos_Comentarios.json()
        print(mensaje)
    else:
        print("La Pelicula No existe")

def Cargar_Pelicula():

    titulo= input("Ingrese el nombre de la pelicula: ")
    año= input("Ingrese el año: ")
    print()
    Lista_Directores()
    print()
    director= input("Ingrese el Director: ")
    print()
    Generos()
    print()
    genero= input("Ingrese el genero: ")
    print()
    sinopsis= input("Ingrese la sinopsis: ")
    img= input("Ingrese la ur de la portada: ")
    duracion= input("Ingrese el tiempo de duracion:")

    comentario={
        "id_usuario":"",
        "nombre":"",
        "opinion":""
        }
    
    reparto=[]
    op=0

    while op !=3:
        print()
        print("Menu Carga Actores")
        print("1) Cargar Actor y su personaje:")
        print("2) Ingrese Comentario")
        print("3) Salir")
        
        op=input("Ingrese su opcion: ")
        print()
        if op == '1':

            actor=input("Nombre del Actor: ")
            personaje=input("Nombre del Personaje: ")

            reparto.append({

                "actor":actor,
                "personaje":personaje
                })
        elif op == '2':
            usuario=input("Ingrese ID de Usuario:")
            nombre=input("Ingrese Nombre: ")
            opinion=input("Ingrese su opinion: ")

            comentario['id_usuario']=usuario
            comentario['nombre']=nombre
            comentario['opinion']=opinion


        elif op =='3':
            break
           

    nueva_pelicula={
        "titulo":"",
        "año":"",
        "director":"",
        "reparto":"",
        "genero":"",
        "sinopsis":"",
        "img":"",
        "duracion":""
    }

    nueva_pelicula['titulo']=titulo
    nueva_pelicula['año']=año
    nueva_pelicula['director']=director
    nueva_pelicula['genero']=genero
    nueva_pelicula['sinopsis']=sinopsis
    nueva_pelicula['img']=img
    nueva_pelicula['duracion']=duracion  
    nueva_pelicula['reparto']=reparto
    #CArgo pelicula a api
    Datos = requests.post('http://127.0.0.1:5000/Agregar/Pelicula', json=nueva_pelicula)
    mensaje1 = Datos.json()
    print(mensaje1)
    #Cargo comentario a api        
    Datos_Comentarios = requests.post('http://127.0.0.1:5000/Comentarios/'+titulo, json=comentario)
    mensaje=Datos_Comentarios.json()
    print(mensaje)


Cargar_Pelicula()
# url = "http://127.0.0.1:5000/Usuarios"
# try:
#     r = requests.get(url, timeout=1)
#     print('Response Code:', r.status_code)
#     servidor_apagado=False
#     print(servidor_apagado)
# except Timeout as ex:
#     servidor_apagado=True
#     print("ok",ex)
#     print(servidor_apagado)