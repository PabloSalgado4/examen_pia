# Definimos la función
def calcular_factorial(numero):
    
    # Empezamos el resultado en 1. 
    # (¡Ojo! No en 0, porque si multiplicas por 0 todo se vuelve 0)
    resultado = 1
    
    # Como no usamos 'range', creamos nuestro propio contador.
    # Empezamos a multiplicar desde el 1.
    i = 1
    
    # Hacemos un bucle 'while' que funcione MIENTRAS nuestro contador 'i' 
    # sea menor o igual al número que nos han pedido.
    while i <= numero:
        
        # Vamos multiplicando lo que ya teníamos por el número actual de 'i'
        resultado = resultado * i
        
        # ¡CRÍTICO! Le sumamos 1 a 'i' a mano para que el bucle avance al siguiente número.
        # Si no ponemos esto, se quedará multiplicando por 1 para siempre.
        i = i + 1
        
    # Devolvemos el cálculo final
    return resultado

# --- ZONA DE PRUEBAS ---
mi_num = 5
total = calcular_factorial(mi_num)
print("El factorial de", mi_num, "es:", total)