# Autonomo 4
# Nombre: Gabriela Ocampo
# Asignatura: Estructura de Datos
# Programa para invertir una cadena usando una pila

# Creamos la clase Pila para manejar los elementos según LIFO (Last In, First Out)
class Pila:
    def __init__(self):
        self.items = []  # Lista interna que almacena los elementos de la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Retorna True si no hay elementos

    def apilar(self, item):
        self.items.append(item)  # Agrega el elemento al final (cima de la pila)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Quita y devuelve el último elemento agregado

    def tamano(self):
        return len(self.items)  # Retorna cuántos elementos hay en la pila

# Función que invierte una cadena usando la clase Pila
def invertir_cadena(cadena):
    pila = Pila()  # Se crea una pila vacía

    # Paso 1: Cada carácter de la cadena se apila
    for caracter in cadena:
        pila.apilar(caracter)

    # Paso 2: Se desapilan los caracteres para formar la cadena invertida
    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()

    return cadena_invertida

# --- Entrada por consola ---
cadena_original = input("Ingrese una cadena para invertir: ")

# Llamamos a la función para invertir la cadena
cadena_invertida = invertir_cadena(cadena_original)

# Mostramos el resultado
print("\nCadena Original:")
print(cadena_original)
print("\nCadena Invertida:")
print(cadena_invertida)

# Si puedes soñarlo, puedes programarlo
