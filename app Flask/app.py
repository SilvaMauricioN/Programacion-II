from flask import Flask,jsonify,json, Response,request
from http import HTTPStatus

#Creo objeto flask llamado app
app = Flask(__name__)
app.config['JSON_AS_ASCII']= False
#Cargo el json en un diccionario python
with open("Directores.json") as archivo:
    Directores=json.load(archivo)

#Cargo el json generos en un diccionarios
with open("Generos.json") as archivo:
    Generos=json.load(archivo)

#Cargo el json peliculas en un diccionario
with open("Peliculas.json", encoding='utf-8') as archivo:
    Peliculas=json.load(archivo)

#Cargo json Comentarios aa diccionario
with open("Comentarios.json", encoding='utf-8') as archivo:
    Comentarios=json.load(archivo)

#Lista de Directores
@app.route("/Directores")
def Devolver_Directores():
    
    return jsonify(Directores)

#Lista de Generos
@app.route("/Generos")
def Devolver_Generos():
    
    return jsonify(Generos)

#Peliculas de un mismo director
@app.route('/Peliculas/<string:Director>')
def Peliculas_Director(Director):
    Pelicula={
        "director":"",
        "peliculas":[]
    }

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