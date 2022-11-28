import json 

#Creo diccionario apartir de un json
with open ('Peliculas.json', encoding='utf-8') as archivo:
    Peliculas = json.load(archivo)

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