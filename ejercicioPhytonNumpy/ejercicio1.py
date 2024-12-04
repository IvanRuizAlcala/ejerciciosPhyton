import numpy as np

ventasDiarias = [230,180,200,150,300,400,250]
ventasDiarias = np.array(ventasDiarias)
ventaTotal = np.sum(ventasDiarias)
print(ventaTotal)
ventaPromedio = np.mean(ventasDiarias)
print(ventaPromedio)
ventaPromedio = np.where(ventasDiarias>ventaPromedio,)[0]
print(ventaPromedio)

print(ventasDiarias[ventaPromedio])
