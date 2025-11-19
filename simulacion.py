import seaborn as sns
import math
import random
from scipy.special import erfinv
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")
import numpy as np
import pandas as pd

sigma = 4
miu = 30
cantidad = 200

def icdf(x):
    return miu + sigma * math.sqrt(2) * erfinv(2*x - 1)

valoresX = []

for i in range(cantidad):
    valor = icdf ( random.random() )
    valoresX.append(valor)
    
dataFrame = pd.DataFrame(valoresX, columns=["valoresX"])
arreglo = np.array(valoresX)
print(np.mean(arreglo))
print(np.std(arreglo))

sns.histplot(data=dataFrame, x="valoresX", kde=True)
print(valoresX)