# Esta clase sirve como el molde base para la creación de vehículos.
class Vehiculo:
    # Declaración de atributos privados con doble guion bajo
    __patente: str
    __anio: int
    __en_taller: bool

    # Constructor que recibe la patente y el año para inicializar el vehículo
    def __init__(self, patente: str, anio: int):
        # Guarda la patente recibida en el atributo privado de la instancia
        self.__patente = patente
        # Guarda el año recibido en el atributo privado de la instancia
        self.__anio = anio
        # Fija __en_taller siempre en False, ya que un vehículo recién registrado nunca parte dentro del taller
        self.__en_taller = False

    # Método para registrar el ingreso del vehículo al taller
    def ingresar(self) -> None:
        # Cambia el estado privado __en_taller a True indicando que ingresó al taller
        self.__en_taller = True

    # Alias de compatibilidad para ingresar al taller
    def ingresar_al_taller(self) -> None:
        self.ingresar()

    # Método para registrar la entrega del vehículo fuera del taller
    def entregar(self) -> None:
        # Cambia el estado privado __en_taller a False indicando que ya no está en el taller
        self.__en_taller = False

    # Alias de compatibilidad para entregar al cliente
    def entregar_al_cliente(self) -> None:
        self.entregar()

    # @property convierte este método en una propiedad de solo lectura, permitiendo acceder a la patente como vehiculo.patente
    @property
    def patente(self) -> str:
        # Retorna el valor del atributo privado __patente
        return self.__patente

    # @property convierte este método en una propiedad de solo lectura, permitiendo acceder al año como vehiculo.anio
    @property
    def anio(self) -> int:
        # Retorna el valor del atributo privado __anio
        return self.__anio

    # @property convierte este método en una propiedad de solo lectura, permitiendo consultar si está en el taller como vehiculo.en_taller
    @property
    def en_taller(self) -> bool:
        # Retorna el valor del atributo privado __en_taller
        return self.__en_taller

    # Alias de compatibilidad para acceder a _en_taller
    @property
    def _en_taller(self) -> bool:
        # Retorna el valor del atributo privado __en_taller
        return self.__en_taller

    # Método que retorna la tarifa por hora genérica para el vehículo
    def tarifa_hora(self) -> int:
        return 5000
