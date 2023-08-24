def contar_palabras(cadena):
    palabras = cadena.split()  # Dividir la cadena en palabras
    frecuencia = {}

    for palabra in palabras:
        palabra = palabra.lower()  # Convertir a minúsculas para considerar mayúsculas y minúsculas iguales
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia
