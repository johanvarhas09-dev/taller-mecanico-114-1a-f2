# Importa la clase base Vehiculo
from vehiculo import Vehiculo

# Definición de la clase Camion que hereda de Vehiculo
class Camion(Vehiculo):
    # Declaración del atributo propio para la capacidad de carga en kilos (entero)
    capacidad_carga: int

    # Constructor que recibe patente, año y capacidad de carga
    def __init__(self, patente: str, anio: int, capacidad_carga: int):
        # Llama al constructor de la clase base Vehiculo para inicializar patente y año
        super().__init__(patente, anio)
        # Guarda la capacidad de carga en kilos en el atributo de la instancia
        self.capacidad_carga = capacidad_carga
