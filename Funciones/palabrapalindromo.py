# Definimos la función
def es_palindromo(palabra):
    
    # Primero, preparamos nuestra variable para guardar la palabra al revés
    palabra_invertida = ""
    
    # Le damos la vuelta letra por letra (como hicimos en el ejercicio anterior)
    for letra in palabra:
        palabra_invertida = letra + palabra_invertida
        
    # Ahora viene la magia: comprobamos si la palabra original 
    # es exactamente igual (==) a la palabra que hemos puesto del revés.
    if palabra == palabra_invertida:
        return True   # Sí es palíndromo
    else:
        return False  # No lo es

# --- ZONA DE PRUEBAS ---
prueba_1 = "radar"
prueba_2 = "python"

if es_palindromo(prueba_1):
    print(prueba_1, "SÍ es un palíndromo.")
else:
    print(prueba_1, "NO es un palíndromo.")















    # 1. NUESTRA FUNCIÓN CASERA PARA CONTAR (Reemplaza a len)
def contar_elementos(texto):
    total = 0
    for elemento in texto:
        total = total + 1
    return total

# 2. NUESTRA FUNCIÓN DE PALÍNDROMO NIVEL ARTESANO
def es_palindromo(palabra):
    
    # Usamos nuestra propia función para saber cuántas letras tiene la palabra
    cantidad_letras = contar_elementos(palabra)
    
    # Preparamos nuestra variable vacía para guardar la palabra al revés
    palabra_invertida = ""
    
    # Creamos nuestro propio contador para movernos por las posiciones de la palabra
    i = 0
    
    # Hacemos el bucle mientras no nos pasemos de la cantidad de letras
    while i < cantidad_letras:
        
        # Sacamos a mano la letra exacta que está en la posición 'i'
        letra_actual = palabra[i]
        
        # Ponemos la letra que acabamos de sacar DELANTE de lo que ya teníamos
        palabra_invertida = letra_actual + palabra_invertida
        
        # ¡CRÍTICO! Le sumamos 1 a 'i' a mano para que en la siguiente vuelta
        # mire la siguiente letra de la palabra.
        i = i + 1
        
    # Ahora comprobamos si la palabra original es exactamente igual (==) 
    # a la palabra que hemos montado del revés letra a letra.
    if palabra == palabra_invertida:
        return True   # Sí es palíndromo
    else:
        return False  # No lo es

# --- ZONA DE PRUEBAS ---
prueba_1 = "radar"
prueba_2 = "python"

if es_palindromo(prueba_1):
    print(prueba_1, "SÍ es un palíndromo.")
else:
    print(prueba_1, "NO es un palíndromo.")