'''
34.- Generar carpetas con python
'''

"""Para crear carpetas con python importamos el mdódulo 'os' o la librería 'pathlib'"""
import os
from pathlib import Path

list = "car, truck, bike, train"
for i in range(5):
    os.makedirs(list)