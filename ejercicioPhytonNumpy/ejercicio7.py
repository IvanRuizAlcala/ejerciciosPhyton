import numpy as np
ventas = np.array([800,1200,950,1100,1250,900])
ventasAltas = np.where(ventas>1000)
print(ventas[ventasAltas])