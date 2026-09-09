# Clase que representa una línea de detalle con cantidad y precio unitario
class LineaDetalle:
    # Declaración de atributos con sus tipos correspondientes
    cantidad: int
    precio_unitario: float

    # Constructor que inicializa los valores de la cantidad y el precio unitario
    def __init__(self, cantidad: int, precio_unitario: float):
        # Guarda la cantidad recibida en el atributo de la instancia
        self.cantidad = cantidad
        # Guarda el precio unitario recibido en el atributo de la instancia
        self.precio_unitario = precio_unitario

    # Método para calcular el subtotal de la línea de detalle
    def subtotal(self) -> float:
        # Retorna el resultado de multiplicar la cantidad por el precio unitario
        return self.cantidad * self.precio_unitario
