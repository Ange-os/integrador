def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    
    for palabra in palabras:
        palabra = palabra.lower()  # Convertir a minúsculas para considerar mayúsculas y minúsculas iguales
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
            
    return frecuencia

def palabra_mas_repetida(diccionario):
    max_frecuencia = 0
    palabra_mas_repetida = ""
    
    for palabra, frecuencia in diccionario.items():
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            palabra_mas_repetida = palabra
            
    return (palabra_mas_repetida, max_frecuencia)

cadena_input = input("Ingrese una cadena de caracteres: ")
resultado = contar_palabras(cadena_input)

print("Frecuencia de palabras:")
for palabra, frecuencia in resultado.items():
    print(f"{palabra}: {frecuencia}")

palabra_mas_repetida_tupla = palabra_mas_repetida(resultado)
print("Palabra más repetida:", palabra_mas_repetida_tupla[0])
print("Frecuencia:", palabra_mas_repetida_tupla[1])