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