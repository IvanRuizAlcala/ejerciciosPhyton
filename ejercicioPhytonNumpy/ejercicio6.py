import numpy as np
meses = np.array([0,0,0,0,0,0])
meses = np.cumsum(meses+500)
print(meses)