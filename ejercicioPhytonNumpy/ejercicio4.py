import numpy as np

ventasMensuales = np.array([500,600,700,800,650,750])
totalMensual = np.cumsum(ventasMensuales)
print(totalMensual)