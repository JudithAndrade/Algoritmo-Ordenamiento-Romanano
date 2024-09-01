# Diccionario con los valores de los números romanos
valores_romanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# Diccionario con los valores de las combinaciones especiales de números romanos
combinaciones_romanas = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}

# Función para calcular el valor romano en una palabra
def valor_romano(palabra):
    valor = 0
    palabra = palabra.upper()
    i = 0
    while i < len(palabra):
        # Verificar si hay una combinación especial
        if i + 1 < len(palabra) and palabra[i:i+2] in combinaciones_romanas:
            valor += combinaciones_romanas[palabra[i:i+2]]
            i += 2  # Saltar la combinación
        elif palabra[i] in valores_romanos:
            # Sumar solo si la letra es un número romano y no parte de una combinación
            valor += valores_romanos[palabra[i]]
            i += 1
        else:
            i += 1  # Avanzar si no es un número romano
    return valor

# Solicitar al usuario que ingrese palabras
palabras = []
print("Ingrese palabras (escriba 'fin' para terminar):")
while True:
    palabra = input()
    if palabra.lower() == 'fin':
        break
    palabras.append(palabra)

# Mostrar las palabras en el orden en que se ingresaron junto con su valor romano
print("\nPalabras ingresadas y sus valores romanos:")
for palabra in palabras:
    print(f"{palabra}: {valor_romano(palabra)}")
