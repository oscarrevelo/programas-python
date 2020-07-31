# %% [markdown]
# ## **desarrollar un programa que calcule el area del circulo y rectangulo**
import math
print("calculo de areas geometricas(circulo y rectangulo con excepciones)")
print("ingrese la figura que desea calcular su area: Circulo-Rectangulo")
figura=(str(input("circulo-rectangulo")))
if figura=="circulo":
    while True:
        try:
            r=(float(input("ingrese el valor del radio")))
            if r<=0:
                raise ZeroDivisionError ("no se puede introducir valores menores o iguales a cero")
            else:    
                resultado=r*(math.pi)
                print(f"El area del circulo es:{resultado}")
            break
        except ValueError:
            print("ingrese valores numericos.Por favor")
        except ZeroDivisionError:
            print("ingrese valores mayores a cero")
elif figura=="rectangulo":
    while True:
        try:
            a=float(input("ingrese el valor de la altura: "))
            b=float(input("ingrese el valor de la base: "))
            if a<=0 or b<=0:
                raise ZeroDivisionError("no se puede introducir valores menores o iguales a cero")
            resultado=a*b
            print(f"el area del rectangulo es: {resultado}")
            break
        except ValueError:
            print("ingrese valores numericos. Por favor")
        except ZeroDivisionError:
            print("ingrese valores mayores a cero")
else:
    print("eleccion incorrecta")
print("fin del programa......")


# %%
