
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def julia_quadratic(zx, zy, cx, cy, iteracion):
    z = complex(zx, zy)
    c = complex(cx, cy)
    
    for i in range(iteracion):
        z = z**2 + c
        if abs(z) > 4.:  
            return i
        
    return iteracion - 1  #si no diverge

x_start, y_start = -2, -2  # zona inicial
ancho,alto = 4, 4  # diseño del area
densidad = 200  # densidad por unidad

# eje real y eje imaginario
re = np.linspace(x_start, x_start + ancho, ancho * densidad )
im = np.linspace(y_start, y_start + alto, alto * densidad)


iteracion = 200  # numero de iteraciones
frames = 100  # numero de frames

# c = r*cos(a) + i*r*sin(a) = r*e^{i*a}
r = 0.885
a = np.linspace(0, 2*np.pi, frames)

fig = plt.figure(figsize=(10, 10))  
ax = plt.axes()  

def animate(i):
    ax.clear()  # limpia el anterior
    ax.set_xticks([], [])  
    ax.set_yticks([], [])  
    
    X = np.empty((len(re), len(im)))  
    cx, cy = r * np.cos(a[i]), r * np.sin(a[i])
    
    # iteraciones
    for i in range(len(re)):
        for j in range(len(im)):
            X[i, j] = julia_quadratic(re[i], im[j], cx, cy, iteracion)
    
    img = ax.imshow(X.T, interpolation="bicubic", cmap='magma')
    return [img]

anim = animation.FuncAnimation(fig, animate, frames=frames, interval=50, blit=True)
anim.save('julia_set.gif', writer='imagemagick')