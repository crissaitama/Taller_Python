#este es un código sencillo de un copo de nieve usando turtle
#es muy simple pero efectivo, para realizar fractales sencillos es tontalmente válido
#funciona bastante bien

import turtle

def koch(k, iteracion,largo, acort, angulo):
    if iteracion == 0: 
        k.forward(largo)
    else:
        iteracion=iteracion-1
        largo= largo/acort
        koch(k, iteracion,largo, acort, angulo)
        k.left(angulo)
        koch(k, iteracion,largo, acort, angulo)
        k.right(angulo*2)
        koch(k, iteracion,largo, acort, angulo)
        k.left(angulo)
        koch(k, iteracion,largo, acort, angulo)     
    
k= turtle.Turtle()
k.hideturtle()
k.pensize(2)
k.pencolor((0.7,0.2,1.0))
for i in range (3):
    koch(k, 4, 200, 3, 60)
    k.right(120)
turtle.mainloop()