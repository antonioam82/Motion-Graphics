from turtle import Turtle
from VALID import OKI, ns

while True:
    t=Turtle()
    print("Escoja dibujo.")
    print("A)Flor")
    print("B)Hexagono")
    print("C)Cuadrado")
    op=input("Introduzca su opción: ")

    if op==("A"):
        t.screen.bgcolor("black")
        colors=["red","yellow","purple"]
        #t.screen.tracer(0,0)
        for x in range(100):
            t.circle(x)#"x" va tomando los valores del rango, por lo que el circulo se irá incrementando
            t.color(colors[x%3])
            t.left(60)
    elif op==("B"):
        colors=["red","purple","blue","green","orange"]
        t.screen.bgcolor("white")
        for x in range(150):
            t.color(colors[x%5])
            t.pensize(x/10+1)
            t.fd(x)
            t.left(59)
    elif op==("C"):
        t.screen.bgcolor("black")
        colors=["blue","purple","red","yellow"]
        for x in range(300):
            t.color(colors[x%4])
            t.fd(x)
            t.left(90)
    t.hideturtle()
    conti=ns(input("¿Continuar?: "))
    if conti==("s"):
        t.reset()
    else:
        break
