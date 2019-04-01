import numpy as np


def kurtosis(x):
    Dx = np.mean((x-np.mean(x))**2)
    N = len(x)
    kurtosis = np.sum(((x-np.mean(x))/np.sqrt(Dx))**4)/N -3
    return kurtosis