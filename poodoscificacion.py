# %%
import time
class doscificacion():
    largoTanque = 2
    Volumen = 3
    radio = 2
    ev1 = False
    ev2 = False
    motor = False

    def naranja_on(self):
        self.ev1 = True

    def naranja_off(self):
        self.ev1 = False

    def agua_on(self):
        self.ev2 = True

    def agua_off(self):
        self.ev2 = False

    def batir_on(self):
        self.motor = True

    def batir_off(self):
        self.motor = False

    def estado1(self):
        if self.ev1 == True:
            return("Electrovalvula1 abierta")
        else:
            return("Electrovalvula1 cerrada")

    def estado2(self):
        if self.ev2 == True:
            return("Electrovalvula2 abierta")
        else:
            return("Electrovalvula2 cerrada")

    def estado3(self):
        if self.motor == True:
            return("Motor Activado")
        else:
            return("Motor Desactivado")


tanque1 = doscificacion()
print(f"El largo del Tanque es:{tanque1.largoTanque}")
print(tanque1.estado1())
tanque1.naranja_on()
print(tanque1.estado1())
time.sleep(5)
tanque1.naranja_off()
print(tanque1.estado1())
time.sleep(2)
print(tanque1.estado2())
tanque1.agua_on()
print(tanque1.estado2())
time.sleep(7)
tanque1.agua_off()
print(tanque1.estado2())
time.sleep(2)
print(tanque1.estado3())
tanque1.batir_on()
print(tanque1.estado3())
time.sleep(10)
tanque1.batir_off()
print(tanque1.estado3())
print("fin del programa.......")

# Completar el funcionamiento del motor


# %%
