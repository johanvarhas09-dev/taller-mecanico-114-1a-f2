from vehiculo import Vehiculo

# Crear un vehículo con patente y año
auto = Vehiculo("KXPR84", 2019)

# Marcarlo como ingresado al taller
auto.ingresar()

# Imprimir su patente, año y tarifa por hora
print(f"Patente: {auto.patente}")
print(f"Año: {auto.anio}")
print(f"Tarifa por hora: ${auto.tarifa_hora()}")
