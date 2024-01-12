#Condiciones multiples

sensorNivelAgua=int(input("Digite el nivel del agua de la represa: "))

print(f"El nivel de agua es: {sensorNivelAgua}")

if sensorNivelAgua>0 and sensorNivelAgua<=150:
    print("Muy poca agua las puertas estan cerradas")
elif sensorNivelAgua>150 and sensorNivelAgua<=400:
     print("Operando normalmente")
elif sensorNivelAgua>400 and sensorNivelAgua<=420:
     print("Cuidado, revise el nivel de agua")
elif sensorNivelAgua>420:
     print("Peligro! Corra....")
else:
     print("Revise el sensor, medida no valida")