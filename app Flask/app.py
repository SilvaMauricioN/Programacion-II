from flask import Flask,jsonify,json, Response,request
import json
from http import HTTPStatus

#Creo objeto flask llamado app
app = Flask(__name__)
app.config['JSON_AS_ASCII']= False

#Funciones para comprobar
def Existe_Pelicula(Pelicula):
    Peliculas = Abrir_Peliculas()
    movie=[]
    for i in Peliculas["Movies"]:
        if i['titulo'].upper() == Pelicula.upper():      
            
            movie.append(i['titulo'])
    
    if len(movie)==1:
        return(True)
    else:
        return(False)

def Existen_Comentarios(Pelicula):

    Comentarios = Abrir_Comentarios()
    
    for i in Comentarios['criticas']:
       
        if i['Nombre_pelicula'].upper() == Pelicula.upper():           

            if len(i['comentarios']) >= 1:
                Existe=True
            else:
                Existe=False    
    return Existe

#Funciones Para Abrir los archivos json

def Abrir_Usuarios():
    with open("Usuarios.json", encoding='utf-8') as archivo:
        Usuarios=json.load(archivo)
    return Usuarios

def Abrir_Directores():

    with open("Directores.json", encoding='utf-8') as archivo:
        Directores=json.load(archivo)
    return Directores

def Abrir_Generos():

    with open("Generos.json", encoding='utf-8') as archivo:
        Generos=json.load(archivo)
    
    return Generos

def Abrir_Peliculas():

    with open("Peliculas.json", encoding='utf-8') as archivo:
        Peliculas=json.load(archivo)

    return Peliculas

def Abrir_Comentarios():
    
    with open("Comentarios.json", encoding='utf-8') as archivo:
        Comentarios=json.load(archivo)
    
    return Comentarios
#Funciones para modificar peliculas
def Agregar_Pelicula(nueva_pelicula):

    with open ("Peliculas.json", "r+", encoding='utf-8') as archivo:
        data = json.load(archivo)
        data["Movies"].append(nueva_pelicula)
        archivo.seek(0)
        json.dump(data, archivo, indent=4, ensure_ascii= False, sort_keys = False )

def Agregar_Director(nueva_pelicula):

    Directores = Abrir_Directores()

    nuevo_director={
        "id_director":"",
        "nombre_director":""
        }
    #Verifico si el director existe en json directores, si no existe lo actualizo con el nuevo director
    for i in Directores:

        if i["id_director"].upper() == nueva_pelicula["director"].upper():
            Existe=True
        else:
            Existe=False
    if Existe != True:

        nuevo_director["id_director"]=str(len(Directores['directores']) + 1)
        nuevo_director["nombre_director"]=nueva_pelicula["director"]

        with open ("Directores.json", "r+", encoding='utf-8') as archivo:
            data = json.load(archivo)
            data["directores"].append(nuevo_director)
            archivo.seek(0)
            json.dump(data, archivo, indent=4, ensure_ascii = False, sort_keys=False)

def Agregar_Genero(nueva_pelicula):

    Generos = Abrir_Generos()
    nuevo_genero={
        "genero_pelicula":""
        }
    
    #Verifico si el genero existe en json genero, si no existe lo actualizo con el nuevo genero
    for i in Generos['Generos']:
        if nueva_pelicula["genero"] in i.values():
            Existe=True
        else:
            Existe=False
    
    if Existe != True:

        nuevo_genero['genero_pelicula']=nueva_pelicula['genero']

        with open ("Generos.json", "r+", encoding='utf-8') as archivo:
            data = json.load(archivo)
            data["Generos"].append(nuevo_genero)
            archivo.seek(0)
            json.dump(data,archivo, indent=4, ensure_ascii = False, sort_keys = False)

def Borrar_Pelicula(Pelicula):

    Peliculas = Abrir_Peliculas()

    for i in Peliculas['Movies']:
        
        if i['titulo'].upper() == Pelicula.upper():

            Peliculas['Movies'].remove(i)
        
        with open ("Peliculas.json", "w", encoding='utf-8') as archivo:
            json.dump(Peliculas,archivo, indent=4, ensure_ascii=False, sort_keys=False)

#RUTAS/ENDPOINTS        

#Lista de Usuarios
@app.route("/Usuarios")
def Devolver_Usiarios():
    Usuarios=Abrir_Usuarios()
    return jsonify(Usuarios)

#Lista de Directores
@app.route("/Directores")
def Devolver_Directores():
    Directores=Abrir_Directores()
    return jsonify(Directores)

#Lista de Generos
@app.route("/Generos")
def Devolver_Generos():
    Generos=Abrir_Generos()
    return jsonify(Generos)

#Todas las Peliculas
@app.route("/Peliculas")
def Devolver_Peliculas():
    Peliculas=Abrir_Peliculas()
    return jsonify(Peliculas)
    
#Peliculas de un mismo director
@app.route('/Peliculas/<string:Director>')
def Peliculas_Director(Director):
    Pelicula={
        "director":"",
        "peliculas":[]
    }
    Peliculas = Agregar_Pelicula()
    for i in Peliculas['Movies']:
        if i['director'].upper() == Director.upper():    
            Pelicula['director']= Director
            Pelicula['peliculas'].append(i['titulo'])
    
    if len(Pelicula['peliculas'])==0:
        return Response("{Director, No Encontrado}", str(HTTPStatus.BAD_REQUEST))    
    else:
        return jsonify(Pelicula)

#Peliculas con imagen de portada
@app.route("/Portada/Peliculas")
def genero():

    ImgPortada=[
    ]
    Peliculas = Agregar_Pelicula()
    for i in Peliculas['Movies']:
        if len(i['img'])  >= 1:

            ImgPortada.append({
                "titulo":i['titulo'],
                "img":i['img']
            })           
    
    if len(ImgPortada[0]['titulo'])==0:
        return Response("{No Encontrado}", str(HTTPStatus.BAD_REQUEST))     
    else:
        return jsonify(ImgPortada)

#Agregar Nueva  Pelicula
def Nueva_Pelicula():

    nueva_pelicula=request.get_json()
    
    if "id" in nueva_pelicula and "titulo" in nueva_pelicula and "año" in nueva_pelicula and "director" in nueva_pelicula  and "reparto" in nueva_pelicula \
        and "genero" in nueva_pelicula and "sinopsis" in nueva_pelicula and "img" in nueva_pelicula and "duracion" in nueva_pelicula:

        Verificar = Existe_Pelicula(nueva_pelicula['titulo'])

        Abrir_Generos(nueva_pelicula)
        Agregar_Genero(nueva_pelicula)

        if Verificar == True:
            return Response("La Pelicula Ya Existe", status=HTTPStatus.OK)
        else:
            Agregar_Pelicula(nueva_pelicula)
            return Response("Pelicula Cargada Existosamente", status=HTTPStatus.OK)
    else:
        return Response("Falta un Campo", str(HTTPStatus.BAD_REQUEST))

#Eliminar Pelicula
@app.route("/Eliminar/<string:Pelicula>", methods=["DELETE"])
def Eliminar_Pelicula(Pelicula):
    Existe=Existe_Pelicula(Pelicula)

    if Existe:
        verificar = Existen_Comentarios(Pelicula)

        if verificar == True:
            return jsonify("No se puede eliminar tiene comentarios")
        else:
            Borrar_Pelicula(Pelicula)
            return jsonify("Pelicula Eliminada")
    else:
        return jsonify("La Pelicula No Existe")

#Modificar Pelicula
@app.route("/Modificar/<string:Pelicula>", methods=["PUT"])
def Modificar_Pelicula(Pelicula):

    Peliculas = Abrir_Peliculas()
    Pelicula_A_Modificar = request.get_json()
    Verificar=Existe_Pelicula(Pelicula)

    if Verificar:

         for i in Peliculas["Movies"]:

            if Pelicula in i.values():
                                
                if "id" in Pelicula_A_Modificar and "titulo" in Pelicula_A_Modificar and "año" in Pelicula_A_Modificar and \
                "director" in Pelicula_A_Modificar  and "reparto" in Pelicula_A_Modificar \
                    and "genero" in Pelicula_A_Modificar and "sinopsis" in Pelicula_A_Modificar and "img" in Pelicula_A_Modificar and \
                    "duracion" in Pelicula_A_Modificar:
                        
                    i['titulo'] = request.json['titulo']
                    i['año'] = request.json['año']
                    i['director'] = request.json['director']
                    i['genero'] = request.json['genero']
                    i['sinopsis'] = request.json['sinopsis']
                    i['img'] = request.json['img']
                    i['duracion'] = request.json['duracion']
                    i['reparto'] = request.json['reparto']

                    with open ("Peliculas.json", "w+", encoding='utf-8') as archivo:
                        data=Peliculas
                        archivo.seek(0)
                        json.dump(data,archivo, indent=4, ensure_ascii = False, sort_keys = False)        
                    
                    
                    return jsonify('Pelicula Modificada')

                else:    
                    return jsonify('ERROR, Falta un Campo')

    else:
        return jsonify("La Pelicula No Existe")