# -*- coding: utf-8 -*-
"""
Created on Thu May  8 13:16:18 2025

@author: andhe
"""

"""Alumno: Eduardo Hernández Hernández
   Fundamentos de python 2025"""
   
   
###################### Funciones ######################

####### EJERCICIO 1: CENSURAR PALABRAS PROHIBIDAS #######


"""Crea una función censurar(texto, prohibidas)
que reemplace cada palabra en la lista prohibidas dentro del 
texto por asteriscos (***), manteniendo las demás palabras intactas."""


def censurar(texto, prohibidas):
    lista = texto.split()
    for i in range(len(lista)):
        if lista[i].lower() in prohibidas:
            lista[i] = "***"
    print(" ".join(lista))

# ejemplo
censurar("Ayer él me dijo ignorante y gordo", ["ignorante", "gordo"])

#%%
####### EJERCICIO 2: FORMATO DE TÍTULO LIMPIO #######

"""Crea una función formato_titulo(titulo)
que reciba una cadena de texto y devuelva el mismo texto con las siguientes reglas:
    * Todas las palabras con la primera letra en mayúscula.
    * Espacios extra eliminados."""
    
def formato_titulo(titulo):
    lista = titulo.split()
    for k in range(len(lista)):
        lista[k] = lista[k].capitalize()
    return " ".join(lista)
       
# ejemplo
formato_titulo("    Me hicieron    Trampa en     el   examen")


#%%
####### EJERCICIO 3: PALABRAS UNICAS #######

"""Escribe una función palabras_unicas(texto)
que reciba un texto y devuelva una lista con todas las 
palabras únicas que contiene, en minúsculas."""


def palabras_unicas(texto):
    # convertimos el texto en una lista y eliminando espacios con el método split
    lista = texto.split()
    lista_palabras_unicas = [] # lista donde agregaremos las palabras unicas
    # contamos cuantas palabras aparecen sólo una vez
    for palabra in lista:
        cantidad = lista.count(palabra)
        if cantidad == 1:
            # si la palabra aparece solo una vez, la agregamos a la lista de palabras unicas
            """pudiera pasar que la palabra sea la misma a excepción de que 
            una palabra comience con mayúscula y la otra con minuscula, por eso 
            agregamos la palabra en minusculas a la lista de palabras unicas"""
            lista_palabras_unicas.append(palabra.lower())
            """pedimos que nos devuelva la lista formada por aquellas palabras 
            que aparecen en la lista de palabras unicas sólo una vez"""
    return [palabra.lower() for palabra in lista_palabras_unicas if lista_palabras_unicas.count(palabra.lower()) == 1]

texto = input("Ingrese un texto: ")
            
palabras_unicas(texto)

#%%
####### EJERCICIO 4: BUSCAR USUARIO POR CORREO #######

"""Crea una función buscar_usuario(usuarios, correo)
que reciba una lista de diccionarios con claves 
"nombre" y "email",  y un correo a buscar.
La función debe devolver el nombre del usuario si se encuentra, 
o None si no."""

# ejemplos de usuarios 
usuarios = [{"nombre":"Eduardo Hernández","email":"eduher2002@gmail.com"},
            {"nombre":"Denisse Hernández","email":"desher2022@gmail.com"},
            {"nombre":"Rigoberto Tlapale","email":"rigoberto1980@gmail.com"}]

correo = input("Ingrese el correo que desea buscar: ")

def buscar_usuario(usuarios,correo):
    for diccionario in usuarios:
        # accedemos a la clave email con el método get de diccionarios
        if diccionario.get("email") == correo:
            return diccionario.get("nombre")
        else:
            return None
# ejemplo
buscar_usuario(usuarios,correo)


#%%
####### EJERCICIO 5: DIVIDIR LISTA EN BLOQUES #######

"""Crea una función dividir_en_bloques(lista, tam)
que divida una lista en sublistas de longitud
tam. La última sublista puede tener menos elementos 
si no alcanza el tamaño indicado."""


def dividir_en_bloques(lista, tam):
    # verificamos que el tamaño de cada sublista no sea mayor al tamaño de la lista original
    if tam <= len(lista):
        sublista = [] # lisa donde ingresaremos cada sublista de tamaño tam
        varias_sublistas = [] # lista donde ingresaremos todas las sublistas
        x = len(lista) // tam # número de listas de tamaño tam que se pueden formar a partir de la lista original
        l = 0 # inicializamos índice en 0
        while l < x:
            # calculamos los limites superior e inferior de cada sublista que se irá generando 
            m = l * tam
            n = (l + 1) * tam
            sublista = [lista[k] for k in range(m,n)]
            varias_sublistas.append(sublista) # agregamos la sublista formada a "varias_sublistas"
            l += 1 # modificamos el indice 
        """verificamos que el limite superior n sea distinto del tamaño de la lista original, 
        pues si son iguales, en la siguiente parte del código me agregaría una lista vacía para el caso 
        en que tam = len(lista). """
        if n != len(lista):
            varias_sublistas.append([lista[i] for i in range(n,len(lista))])
        return varias_sublistas
    else:
        print("El tamaño se las sublistas excede el tamaño de la lista original.")
        return None 

dividir_en_bloques([42, "hola", 3.14, True, None, 100, "Adiós"],1)

#%%
####### EJERCICIO 6: NORMALIZAR NOMBRES #######

"""Crea una función normalizar_nombres(lista_nombres)
que reciba una lista de nombres desordenados (con mayúsculas mal
colocadas, espacios extras, etc.) y devuelva una lista con nombres corregidos, en el formato: "Nombre Apellido". """


def normalizar_nombres(lista_nombres):
    # eliminamos espacios extras
    for i in range(len(lista_nombres)):
        lista_nombres[i] = lista_nombres[i].split()
    # Escribimos nombre y apellido en minúsculas y despues escribimos su primera letra en mayúscula
    for i in range(len(lista_nombres)):
        for k in range(len(lista_nombres[i])):
            lista_nombres[i][k] = lista_nombres[i][k].lower().capitalize()
    # pegamos nombre y apellido usando el método join
    for i in range(len(lista_nombres)):
        lista_nombres[i] = " ".join(lista_nombres[i])
    return lista_nombres

# ejemplo
normalizar_nombres(["eduardo HernANDEZ  ", "   DenissE   HERNÁndez", "Mónica    ibARRA "])



#%%
####### EJERCICIO 7: EXTRAER HASHTAGS #######

"""Crea una función extraer_hashtags(texto)
que reciba una cadena de texto y devuelva una lista con todas las palabras que
comienzan con el símbolo #, sin incluir el símbolo en el resultado."""



def extraer_hashtags(texto):
    lista_palabras_hashtag = [] # lista donde pondremos las palabras que tienen hashtags
    # convertimos en una lista al texto ingresado 
    lista_texto = texto.split() 
    for palabra in lista_texto:
        # verificamos que la palabra en la lista anterior comience con un hashtag
        if palabra.startswith("#"):
            lista_palabras_hashtag.append(palabra) # si la palabra comienza con hashtag, la agregamos a la lista de palabras con hashtag
    # modificamos la lista de palabras con hashtag 
    for i in range(len(lista_palabras_hashtag)):
        # quitamos el hashtag de las palabras que comienzan con #
        # primero separamos la palabra de su hashtag usando el metodo split
        # despues unimos los elementos con el metodo join 
        lista_palabras_hashtag[i] = "".join(lista_palabras_hashtag[i].split("#"))   
    return lista_palabras_hashtag
            
# ejemplo
extraer_hashtags("#ArribaElAmérica y abajo las chivas #Love")
        

            

#%%
####### EJERCICIO 8: VALIDAR CONTRASEÑA #######

"""Crea una función es_contrasena_valida(clave)
que determine si una cadena es una contraseña válida. La contraseña debe cumplir:
* Tener al menos 8 caracteres.
* Contener al menos una letra mayúscula.
* Contener al menos un número.
* Contener al menos un símbolo especial (como !@#$% )."""
                                         

def es_contrasena_valida(clave):
    caracteres_especiales = "!@#$%"
    
    # verificamos que la longitud de la clave sea de al menos 8 caracteres 
    if len(clave) < 8:
        return False
    # inicializamos las variables que determinan si la contraseña es valida
    mayuscula = False
    digito = False
    especial = False

    for caracter in clave:
        if caracter.isupper():
            mayuscula = True
        if caracter.isdigit():
            digito = True
        if caracter in caracteres_especiales:
            especial = True

    return mayuscula and digito and especial

clave = input("ingresa una contraseña: ")

es_contrasena_valida("HolaAtod12#$") 


if es_contrasena_valida(clave):
    print("Contraseña válida.")
else:
    print("Contraseña inválida")
            
#%%
####### EJERCICIO 9: HISTORIAL DE COMANDOS #######
    
"""Escribe una función historial_comandos(comandos)
que reciba una lista de comandos y devuelva un resumen en forma de
diccionario con:
    * El total de comandos.
    * El número de comandos únicos.
    * El comando que más veces se repite."""


def historial_comandos(comandos):
    lista = [] # definimos la lista en la que vamos a agregar los elementos del diccionario 
    # a esa lista la vamos a convertir en diccionario usando la funcion dict
    claves = ["El total de comandos", "El número de comandos únicos", "El comando que más veces se repite"] # claves que solicita el problema
    ###### Formamos una lista cuyos elementos sean pares mapeables a un objeto tipo dict
    for i in range(3):
        lista.append([claves[i]]) # agregamos a la lista "lista" 3 elementos, cada elemento esta formado por cada clave del diccionario
    lista[0].append(len(comandos))
    num_comandos_unicos = 0 
    # contamos cuántos comandos unicos hay
    for comando in comandos:
        contador_comandos = comandos.count(comando)
        if contador_comandos == 1:
            num_comandos_unicos += 1
    # agregamos a la lista el numero de comandos unicos
    lista[1].append(num_comandos_unicos)
    # vemos cual es el comando mas repetido usando la funcion max y lambda
    comando_mas_repetido = max(comandos, key = lambda v: comandos.count(v))
    lista[2].append(comando_mas_repetido)
    return dict(lista)

# ejemplo
comandos = [
    "ls",                  # repetido
    "cd /home",
    "mkdir nueva_carpeta", # repetido
    "ls",                  # repetido
    "rm archivo.txt",
    "echo 'Hola mundo'",
    "git status",
    "ls",                  # repetido
    "clear",
    "mkdir nueva_carpeta", # repetido
    "exit"
]

historial_comandos(comandos)

#%%


