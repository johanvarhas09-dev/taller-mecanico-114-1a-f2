from vehiculo import Vehiculo

class Auto(Vehiculo):
    pass

if __name__ == "__main__":
    v = Vehiculo("1234", 1930)
    v.ingresar_al_taller()
    print("Vehiculo en taller")
    print(v._en_taller)
    print(v.tarifa_hora())
    v.entregar_al_cliente()
    print(v._en_taller)
