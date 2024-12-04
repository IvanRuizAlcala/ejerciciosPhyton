import numpy as np

salarioEmpleados = [1800,2200,2500,1900,2100,1600]
salarioEmpleados = np.array(salarioEmpleados)
incremento = np.where(salarioEmpleados<2000,salarioEmpleados*1.1,salarioEmpleados)
print(incremento)
