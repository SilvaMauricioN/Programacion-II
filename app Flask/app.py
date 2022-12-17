from flask import Flask,jsonify,json, Response,request
import json

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
    critica=[]
    for i in Comentarios['criticas']:
        if i['Nombre_pelicula'].upper() == Pelicula.upper():
            if i["comentarios"]==critica:
                Existe=False
            else:
                Existe=True    
    return Existe

def Existe_Director(nueva_pelicula):
    Directores=Abrir_Directores()
    director=[]
    #Verifico si el director existe en json directores, si no existe lo actualizo con el nuevo director  
    for i in Directores['directores']:        
        if i['nombre_director'].upper() == nueva_pelicula["director"].upper():
            director.append(i['nombre_director'])

    if len(director)>=1:
        Existe=True
    else:
        Existe=False    

    return Existe

def Existe_Genero(nueva_pelicula):
    Generos=Abrir_Generos()
    genero=[]
    for i in Generos['Generos']:

        if i['genero_pelicula'].upper() == nueva_pelicula["genero"].upper():
            genero.append(i['genero_pelicula'])
    if len(genero)>=1:
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
    Peliculas=Abrir_Peliculas()
    #Cargo el id de la nueva pelicula
    nueva_pelicula['id']=str(len(Peliculas['Movies']) + 1)

    with open ("Peliculas.json", "r+", encoding='utf-8') as archivo:
        data = json.load(archivo)
        data["Movies"].append(nueva_pelicula)
        archivo.seek(0)
        json.dump(data, archivo, indent=4, ensure_ascii= False, sort_keys = False )

def Agregar_Director(nueva_pelicula):

    Directores = Abrir_Directores()
    verifica = Existe_Director(nueva_pelicula)

    nuevo_director={
        "id_director":"",
        "nombre_director":""
        }
    #Verifico si el director existe en json directores, si no existe lo actualizo con el nuevo director
    
    if verifica != True:

        nuevo_director["id_director"]=str(len(Directores['directores']) + 1)
        nuevo_director["nombre_director"]=nueva_pelicula["director"]

        with open ("Directores.json", "r+", encoding='utf-8') as archivo:
            data = json.load(archivo)
            data["directores"].append(nuevo_director)
            archivo.seek(0)
            json.dump(data, archivo, indent=4, ensure_ascii = False, sort_keys=False)

def Agregar_Genero(nueva_pelicula):

    nuevo_genero={
        "genero_pelicula":""
        }    
    #Verifico si el genero existe en json genero, si no existe lo actualizo con el nuevo genero
    verifica=Existe_Genero(nueva_pelicula)
    
    if verifica != True:

        nuevo_genero['genero_pelicula']=nueva_pelicula['genero']

        with open ("Generos.json", "r+", encoding='utf-8') as archivo:
            data = json.load(archivo)
            data["Generos"].append(nuevo_genero)
            archivo.seek(0)
            json.dump(data,archivo, indent=4, ensure_ascii = False, sort_keys = False)

def Agregar_Comentario(Pelicula,Nuevo_Comentario):

    Comentarios=Abrir_Comentarios()

    for i in Comentarios['criticas']:
        if i['Nombre_pelicula'].upper() == Pelicula.upper():
            i['comentarios'].append(Nuevo_Comentario)

    with open ("Comentarios.json", "w+", encoding='utf-8') as archivo:
        data=Comentarios
        archivo.seek(0)
        json.dump(data,archivo, indent=4, ensure_ascii = False, sort_keys = False)

def Borrar_Pelicula(Pelicula):

    Peliculas = Abrir_Peliculas()

    for i in Peliculas['Movies']:
        
        if i['titulo'].upper() == Pelicula.upper():

            Peliculas['Movies'].remove(i)
        
        with open ("Peliculas.json", "w", encoding='utf-8') as archivo:
            json.dump(Peliculas,archivo, indent=4, ensure_ascii=False, sort_keys=False)

def Borrar_Comentario(pelicula):

    comentarios= Abrir_Comentarios()
    
    for i in comentarios["criticas"]:
        
        if i["Nombre_pelicula"].upper() == pelicula.upper():
            comentarios["criticas"].remove(i)
    
    with open ("Comentarios.json", "w", encoding='utf-8') as archivo:
            json.dump(comentarios,archivo, indent=4, ensure_ascii=False, sort_keys=False)

#Agregar diccionaro de comentarios de la nueva pelicula
def Agregar_Objeto_Comentario(nueva_pelicula):
    Comentarios=Abrir_Comentarios()
    Nuevo_Pelicula_Comentario={
            "Nombre_pelicula":"",
            "id_pelicula":"",            
            "comentarios":[]
            }
       
    Nuevo_Pelicula_Comentario['Nombre_pelicula']=nueva_pelicula
    Nuevo_Pelicula_Comentario['id_pelicula']=str(len(Comentarios['criticas']) + 1)
    Comentarios['criticas'].append(Nuevo_Pelicula_Comentario)

    with open ("Comentarios.json", "w+", encoding='utf-8') as archivo:
        data=Comentarios
        archivo.seek(0)
        json.dump(data,archivo, indent=4, ensure_ascii = False, sort_keys = False)

#RUTAS/ENDPOINTS
#Lista de Usuarios
@app.route("/Usuarios")
def Devolver_Usuarios():
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

#Devolver Comentarios
@app.route("/Comentarios")
def Devolver_Comentarios():
    Comentarios=Abrir_Comentarios()
    return jsonify(Comentarios)
    
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
    Peliculas = Abrir_Peliculas()
    for i in Peliculas['Movies']:
        if i['director'].upper() == Director.upper():    
            Pelicula['director']= Director
            Pelicula['peliculas'].append(i['titulo'])
    
    if len(Pelicula['peliculas'])==0:
        return jsonify("{Director, No Encontrado}")   
    else:
        return jsonify(Pelicula)

#Peliculas con imagen de portada
@app.route("/Portadas/Peliculas")
def Portadas():

    ImgPortada=[
    ]
    Peliculas = Abrir_Peliculas()
    for i in Peliculas['Movies']:
        if len(i['img'])  >= 1:

            ImgPortada.append({
                "titulo":i['titulo'],
                "img":i['img']
            })           
    
    if len(ImgPortada[0]['titulo'])==0:
        return jsonify("No Encontrado")     
    else:
        return jsonify(ImgPortada)

#Agregar Nueva  Pelicula
@app.route("/Agregar/Pelicula", methods=["POST"])
def Nueva_Pelicula():

    nueva_pelicula=request.get_json()
    
    if "titulo" in nueva_pelicula and "año" in nueva_pelicula and "director" in nueva_pelicula  and "reparto" in nueva_pelicula \
        and "genero" in nueva_pelicula and "sinopsis" in nueva_pelicula and "img" in nueva_pelicula and "duracion" in nueva_pelicula:

        Verificar = Existe_Pelicula(nueva_pelicula['titulo'])
        
        if Verificar == True:
            return jsonify("La Pelicula Ya Existe")
        else:
            Agregar_Pelicula(nueva_pelicula)
            Agregar_Director(nueva_pelicula)
            Agregar_Genero(nueva_pelicula)
            Agregar_Objeto_Comentario(nueva_pelicula['titulo'])
            return jsonify("Pelicula Cargada Existosamente")
    else:
        return jsonify("Falta un Campo")

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
            Borrar_Comentario(Pelicula)
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
                                
                if "titulo" in Pelicula_A_Modificar and "año" in Pelicula_A_Modificar and \
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

#modificar pelicula desde programa python
@app.route("/Modificar/Peliculas", methods=['PUT'])
def Cargar_Modificaciones():    
    
    pelicula_A_Modificar = request.get_json()

    if 'Movies' in pelicula_A_Modificar:

        with open ("Peliculas.json", "w+", encoding='utf-8') as archivo:
            data=pelicula_A_Modificar
            archivo.seek(0)
            json.dump(data,archivo, indent=4, ensure_ascii = False, sort_keys = False)

        return jsonify("Pelicula Modificada Exitosamente")
    else:
        return jsonify("La ruta seleccionada no corresponde con el formato de json enviado")    


@app.route("/Comentarios/<string:Pelicula>", methods=["POST"])
def Nuevo_Comentario(Pelicula):
    verificar=Existe_Pelicula(Pelicula)
    Nuevo_Comentario=request.get_json()

    if verificar:
        if "id_usuario" in Nuevo_Comentario and "nombre" in Nuevo_Comentario and "opinion" in Nuevo_Comentario or Nuevo_Comentario==[]:

            Agregar_Comentario(Pelicula,Nuevo_Comentario)
            return jsonify("Comentario Cargado")
        else:
            return jsonify("Falta un campo")
    else:
        return jsonify('La pelicula NO Existe')