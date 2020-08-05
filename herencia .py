# %%
class vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    
    def arrancar(self):
        self.enmarcha=True
        
    def acelerar(self):
        self.acelera=True
        
    def frenar(self):
        self.frena=True
        
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,"\nEn Marcha: ",self.enmarcha,"\nAcelerando: ", self.acelera,"\nFrenando: ",self.frena)
class furgoneta(vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if (self.cargado):
            return("la furgoneta esta cargada")
        else:
            return("la furgoneta no esta cargada")
        
class moto(vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito= "estoy haciendo el caballito"
        def estado(self):
            print("Marca: ", self.marca, "\nModelo: ", self.modelo,"\nEn Marcha: ",self.enmarcha,"\nAcelerando: ", self.acelera,"\nFrenando: ",self.frena, "\nCaballito: ",self.hcaballito)

class Velectricos(vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia=100
    def cargaEnergia(self):
        self.cargando=True
    
    
    
    
miMoto=moto("Hona","CRB")
print(miMoto.estado())

mifurgoneta=furgoneta("renault","kangoo")
print(mifurgoneta.estado())
print(mifurgoneta.carga(True))


class BiciElectrica(Velectricos, vehiculos):
    pass
miBici=BiciElectrica("marca","ll")
print(miBici.estado())

# %% [markdown]
## uso de funcion super para 2 herencias
class persona():
    def __init__(self,nombre,edad,lugarResidencia):
        self.nombre=nombre
        self.edad=edad
        self.lugarResidencia=lugarResidencia
        
    def descripcion(self):
        print("Nombre: ",self.nombre,"Edad: ", self.edad, "Lugar de residencia: ", self.lugarResidencia)
    
class empleado(persona):
    def __init__(self,salario,antiguedad, nombre_empleado, edad_empleado,resisdencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, resisdencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print("el salario es: ", self.salario, "la antiguedad es: ", self.antiguedad)
antonio=empleado(1500,15,"Antonio",55,"Ecuador")
print(antonio.descripcion())
print(isinstance(antonio,empleado))


# %% [markdown]
# polimorfismo

class coche():
    def desplazamiento(self):
        print("me desplazo en 4 ruedas")
        
class motocicleta():
    def desplazamiento(self):
        print("me desplazo en 2 ruedas")

class camion():
    def desplazamiento(self):
        print("me desplazo en 6 ruedas")

def desplazamientoVehiculo(vehiculo):   
    vehiculo.desplazamiento()
    
miVehiculo=camion()
print(desplazamientoVehiculo(miVehiculo))

# %%
