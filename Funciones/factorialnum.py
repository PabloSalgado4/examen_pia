# Definimos la función
def calcular_factorial(numero):
    
    # Empezamos el resultado en 1. 
    # (¡Ojo! No en 0, porque si multiplicas por 0 todo se vuelve 0)
    resultado = 1
    
    # Hacemos un bucle que vaya desde el 1 hasta el número que nos han pedido.
    # Ponemos 'numero + 1' porque el range en Python SIEMPRE para un número antes.
    for i in range(1, numero + 1):
        
        # Vamos multiplicando lo que ya teníamos por el nuevo número
        resultado = resultado * i
        
    # Devolvemos el cálculo final
    return resultado

# --- ZONA DE PRUEBAS ---
mi_num = 5
total = calcular_factorial(mi_num)
print("El factorial de", mi_num, "es:", total)