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





#MAS ARTESANAL AUN



    # Definimos la función
def es_primo(numero):
    
    # Si el número es 1 o menor, no es primo
    if numero <= 1:
        return False
        
    # Como no podemos usar range(2, numero), creamos nuestro propio divisor manual.
    # Empezamos a probar desde el 2.
    divisor = 2
    
    # MIENTRAS el divisor sea más pequeño que nuestro número...
    while divisor < numero:
        
        # El operador '%' saca el resto de la división. 
        # Si el resto es 0, significa que la división es exacta y hemos encontrado un fallo.
        if numero % divisor == 0:
            # Si es divisible por cualquier número que no sea él mismo, no es primo.
            return False
            
        # ¡IMPORTANTE! Sumamos 1 a nuestro divisor para probar con el siguiente número.
        # Por ejemplo: primero prueba con 2, luego con 3, luego con 4...
        divisor = divisor + 1
            
    # Si el bucle termina y nunca encontró una división exacta, es que el número es primo.
    return True

# --- ZONA DE PRUEBAS ---
mi_numero = 7
if es_primo(mi_numero):
    print("El número", mi_numero, "SÍ es primo (calculado a mano).")
else:
    print("El número", mi_numero, "NO es primo.")