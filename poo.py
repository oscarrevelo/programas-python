# %%
class Coche():
    def __init__(self):
        self.__largochasis=150
        self.__anchochasis=100
        self.__ruedas=3
        self.__enmarcha=False
    
    
    def encender(self, suitch):
        self.__enmarcha=suitch
        if self.__enmarcha==True:
            self.chequeo1=self.__chequeo()
        if self.__enmarcha==True and self.chequeo1==True:
            return("el vehiculo esta en movimiento")
        elif self.__enmarcha==True and self.chequeo1==False:
            return("algo salio mal.....revise su vehiculo")
        else:
            return("el vehiculo esta parado")
    

    def estadovehiculo(self):
        return("el largo del chasis es:",self.__largochasis,"el nuemro de ruedas es:",self.__ruedas, "el largo del chasis es:", self.__largochasis)
    
    def __chequeo (self):
        print("iniciando chequeo interno. Espere un momento........")
        self.gasolina="OK"
        self.aceite="OK"
        self.puertas="cerradas"
        if self.gasolina=="OK" and self.aceite=="OK" and self.puertas=="cerradas":
            return True
        else:
            return False
miCoche=Coche()
print(miCoche.encender(True))
print(miCoche.estadovehiculo())   


# %%
