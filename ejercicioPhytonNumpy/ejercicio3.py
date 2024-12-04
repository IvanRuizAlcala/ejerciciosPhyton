import numpy as np
inventarioProductos = np.array([5,12,8,20,3,15,7])
productosInferioresAMinimo = np.where(inventarioProductos<10)
productosFinales = inventarioProductos[productosInferioresAMinimo]
print(len(productosFinales))