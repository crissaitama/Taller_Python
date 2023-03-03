import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def mandelbrot(x, y, threshold):
   # condicion inicial
    c = complex(x, y)
    z = complex(0, 0)
    
    for i in range(threshold):
        z = z**2 + c
        if abs(z) > 4.:  
            return i
        
    return threshold - 1  

x_start, y_start = -2, -1.5  
ancho, alto = 3, 3  
densidad = 250  

# ejes reales e imaginarios
re = np.linspace(x_start, x_start + ancho, ancho *densidad )
im = np.linspace(y_start, y_start + alto, alto * densidad)

fig = plt.figure(figsize=(10, 10))
ax = plt.axes()  

def animate(i):
    ax.clear()  
    ax.set_xticks([], []) 
    ax.set_yticks([], [])  
    
    X = np.empty((len(re), len(im)))
    threshold = round(1.15**(i + 1))  
    
    for i in range(len(re)):
        for j in range(len(im)):
            X[i, j] = mandelbrot(re[i], im[j], threshold)
    
    img = ax.imshow(X.T, interpolation="bicubic", cmap='magma')
    return [img]
 
anim = animation.FuncAnimation(fig, animate, frames=45, interval=120, blit=True)
anim.save('mandelbrot.gif',writer='imagemagick')