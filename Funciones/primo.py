# Definimos la función
def es_primo(numero):
    
    # Si el número es 1 o menor, por matemáticas sabemos que no es primo
    if numero <= 1:
        return False
        
    # Hacemos un bucle que vaya desde el 2 hasta justo un número antes del nuestro
    # Ejemplo: Si el número es 7, dividiremos entre 2, 3, 4, 5 y 6.
    for i in range(2, numero):
        
        # El operador '%' saca el resto de la división. 
        # Si el resto es 0, significa que la división es exacta.
        if numero % i == 0:
            # Si encontramos CUALQUIER división exacta, ya no es primo.
            # Salimos de la función inmediatamente devolviendo False
            return False
            
    # Si el bucle termina y no ha encontrado ninguna división exacta, ¡es primo!
    return True

# --- ZONA DE PRUEBAS ---
mi_numero = 7
if es_primo(mi_numero):
    print("El número", mi_numero, "SÍ es primo.")
else:
    print("El número", mi_numero, "NO es primo.")