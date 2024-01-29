cadena1 = "holacomoestas"
cadena2 = "Bienvenido meran"

#convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minusculas
minusc = cadena1.lower()

#nos muestra la 1ra letra del texto en mayuscula
primer_letra_mayuscula = cadena1.capitalize()

#buscamos una cadena en otro cadena
busqueda_find = cadena1.find("s")

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion
busqueda_index = cadena1.index("h")

#si es numerico, devolvemos True, si no devolvemos False
es_numerico = cadena1.isnumeric()

#si es alfa numerico devuelve True
es_alfa_numerico = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida.
contar_coincidencias = cadena1.count("a")


print(contar_coincidencias)