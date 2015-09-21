#! /usr/bin/env python

'''
Este es un script que busca el punto de
interseccion entre seno y coseno usando
el metodo de la biseccion.
'''

import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
plt.clf()

x_values = np.linspace(0, np.pi, 100)
plt.plot(x_values, np.sin(x_values), label='sin(x)')
plt.plot(x_values, np.cos(x_values), label='cos(x)')

plt.xlabel('x [radianes]')
plt.legend()
plt.show()
