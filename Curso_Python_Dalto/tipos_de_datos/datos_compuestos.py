#Datos Compuesto: Son aquellos que tienen adentro varios datos juntos.

#Creando una lista (se puede modificar)
lista = ["Luis Enrique","Meran Cell", True, 1.65, "Virgo", "Septiembre", 14, 10, 1994]

#Creando una tupla (no se pueden modificar)
tupla = ("Luis Meran","Meran Cell", True, 1.65)

lista[3] = "Maquinola"

#esto no
#tupla [3] = "Maquinola"

#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)
conjunto = {"Luis Enrique","Meran Cell", True, 1.65}

#print(conjunto[3]) ---> no pude acceder al elemento

#creando un diccionario (dict) ( la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "Luis Meran",
    'canal' : "Meran Cell",
    'esta_emocionado' : True,
    'altura' : 1.65,
    #'dato_duplicado' : "Meran Cell"
}

print(diccionario)