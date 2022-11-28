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


def menu():
    print("1.Ver peliculas")

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