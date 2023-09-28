"""Ejemplo de archivo de Python local"""
import os

import numpy as np

def regresar_home():
    """Regresa el path de HOME"""
    return os.environ["HOME"] 

def regresar_array_aleatorio(size:int = 10):
    """Regresa un array aleatorio"""
    print(size)
    return np.random.rand(size)

