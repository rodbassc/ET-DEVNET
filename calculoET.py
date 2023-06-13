import math

def calculo_circunferencia(radio):
    pi_evaluacion = round(math.pi, 6)
    circunferencia = radio * pi_evaluacion * 2
    return circunferencia

radios_soli = [3, 8, 10]

for radio in radios_soli:
    circunferencia = calculo_circunferencia(radio)
    print("La circunferencia del radio " + str(radio) + " es " + str(circunferencia))

