def get_int_recursivo():
    try:
        valor = int(input("Ingrese un valor entero: "))
        return valor
    except ValueError:
        print("Error: El valor ingresado no es válido. Intente nuevamente.")
        return get_int_recursivo()
entero = get_int_recursivo()
print(f"Usted ha ingresado el valor entero: {entero}")