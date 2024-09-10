# Diccionario para los valores de los números romanos
valores_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Lista de palabras con sus posibles valores en números romanos
palabras = ["Pixel", "Civil", "Paco", "Hijo", "Toxico", "Camion", "Clave", "Ximena", "Damian", "Lili", "Claudia", "Medallon", "Clima"]

def valor_romano_de_palabra(palabra):
    # Sumar el valor de las letras que correspondan a números romanos
    total = sum(valores_romanos.get(letra.upper(), 0) for letra in palabra)
    return total

"""
    Esta función recibe una palabra y calcula su valor basado en los números romanos.
    Usa una comprensión de lista dentro de sum() para iterar sobre cada letra de la palabra.
    letra.upper() convierte cada letra a mayúscula para que sea consistente con las claves del diccionario (valores_romanos).
    valores_romanos.get(letra.upper(), 0) busca el valor de la letra en el diccionario. Si la letra no está en el diccionario, devuelve 0.
    total es la suma de todos estos valores y se devuelve al final.
    """

# Ordenar las palabras en función del valor de sus letras romanas en orden ascendente
palabras_ordenadas = sorted(palabras, key=valor_romano_de_palabra, reverse=False)

# Imprimir el resultado
for palabra in palabras_ordenadas:
    print(f'{palabra}: {valor_romano_de_palabra(palabra)}')
