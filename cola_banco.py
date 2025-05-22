
# Implementación de una Cola usando clases y nodos
class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Dato del cliente
        self.siguiente = None  # Puntero al siguiente nodo

class Cola:
    def __init__(self):
        self.frente = None  # Inicio de la cola
        self.final = None   # Final de la cola

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, cliente):
        nuevo_nodo = Nodo(cliente)
        if self.final:
            self.final.siguiente = nuevo_nodo  # Enlazamos el nuevo nodo
        self.final = nuevo_nodo
        if self.frente is None:
            self.frente = nuevo_nodo  # Si estaba vacía, el nuevo nodo es también el frente

    def desencolar(self):
        if self.esta_vacia():
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente  # Avanzamos el frente
        if self.frente is None:
            self.final = None  # Si la cola queda vacía
        return dato

    def mostrar_cola(self):
        estado = []
        actual = self.frente
        while actual:
            estado.append(actual.dato)
            actual = actual.siguiente
        return estado

# Crear una instancia de Cola y definir los nombres de prueba
cola_banco = Cola()
nombres_prueba = ["Ada", "Esther", "Benedit"]
indice_nombre = 0

# Menú interactivo para simular la atención en el banco
def menu_banco():
    global indice_nombre
    continuar = True
    while continuar:
        print("\n--- MENÚ DEL BANCO ---")
        print("1. Añadir cliente")
        print("2. Atender cliente")
        print("3. Mostrar cola")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if indice_nombre < len(nombres_prueba):
                nombre = nombres_prueba[indice_nombre]
                indice_nombre += 1
            else:
                nombre = input("Ingrese el nombre del cliente: ")
            cola_banco.encolar(nombre)
            print(f"Cliente '{nombre}' añadido a la cola.")

        elif opcion == "2":
            atendido = cola_banco.desencolar()
            if atendido:
                print(f"Cliente '{atendido}' ha sido atendido.")
            else:
                print("La cola está vacía. No hay clientes para atender.")

        elif opcion == "3":
            estado = cola_banco.mostrar_cola()
            print("Estado actual de la cola:", estado if estado else "La cola está vacía.")

        elif opcion == "4":
            print("Programa finalizado.")
            continuar = False

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu_banco()
