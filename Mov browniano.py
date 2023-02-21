#Simulación del movimiento Browniano de una partícula dentro de una caja
#Jesús Enrique Armenta Lara, matrícula 201802397
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros de la simulación
D = 1.0  # Coeficiente de difusión
L = 10.0  # Longitud de la caja
n_part = 1  # Número de partículas
n_steps = 1000  # Número de pasos de tiempo

# Inicializar posición de la partícula
r = np.zeros((n_steps, n_part, 2))

# Generar ruido gaussiano
noise = np.random.randn(n_steps, n_part, 2)

# Actualizar posición de la partícula
r[1:] = r[:-1] + np.sqrt(2*D) * noise[1:]

# Mantener la partícula dentro de la caja
r = np.where(r < 0, -r, r)
r = np.where(r > L, 2*L-r, r)

# Función que actualiza la animación
def update(i):
    # Actualizar posición de la partícula
    r[i] = r[i-1] + np.sqrt(2*D) * noise[i]

    # Mantener la partícula dentro de la caja
    r[i] = np.where(r[i] < 0, -r[i], r[i])
    r[i] = np.where(r[i] > L, 2*L-r[i], r[i])

    # Actualizar la posición de la partícula en la animación
    line.set_data(r[:i, 0, 0], r[:i, 0, 1])
    return line,

# Inicializar la figura y la animación
fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-', linewidth=1)
ax.set_xlim(0, L)
ax.set_ylim(0, L)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Movimiento Browniano en una caja')
ani = FuncAnimation(fig, update, frames=n_steps, interval=50, blit=True) 
#interval es el tiempo en que la animación se actualiza, está en milisegundos

# Mostrar la animación
plt.show()
