nombre_completo = input("Ingrese su nombre completo: ")
dias = int(input("Ingrese sus dias laborados: "))
salario = float(input("Ingrese su salario: "))

def prima ():
    valorPrima = (salario*dias)/360
    return valorPrima
def intereses ():
    valorIntereses = ((salario*dias/360) *0.12)/dias
    return valorIntereses
def vacaciones ():
    valorVacaiones = (salario*dias)/720
    return valorVacaiones
def liquidacion ():
    valorLiquidacion = ((((salario*dias)/360)*2) +(((salario*dias/360) *0.12)/dias) + ((salario*dias)/720))
    return valorLiquidacion
print(f"señor {nombre_completo} para los {dias} dias laborados"
      f" y salario {salario}, su liquidacion se compone asi:")
print(f"Prima: {prima():.2f}")
print(f"Cesantias:  {prima():.2f}")
print(f"Intereses cesantias: {intereses():.2f}")
print(f"Vacaciones: {vacaciones():.2f}")
print(f"Liquidacion: {liquidacion():.2f}")