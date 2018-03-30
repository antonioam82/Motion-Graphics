from turtle import Turtle
from VALID import OKI, ns, opt
import subprocess

while True:
    t=Turtle()
    print("Escoja dibujo.")
    print("A)Flor")
    print("B)Hexagono com")
    print("C)Cuadrado")
    print("D)Hexagono simp")
    print("E)Cuadrado spiral")
    print("F)Raizes")
    op=opt(input("Introduzca su opción: "),["A","B","C","D","E"])

    if op==("A"):
        t.screen.bgcolor("black")
        colors=["red","yellow","purple"]
        for x in range(100):
            t.circle(x)
            t.color(colors[x%3])
            t.left(60)
    elif op==("B"):
        t.screen.bgcolor("white")
        colors=["red","purple","blue","green","orange"]
        for x in range(150):
            t.color(colors[x%5])
            t.width(x/10+1)
            t.fd(x)
            t.left(59)
    elif op==("C"):
        t.screen.bgcolor("black")
        colors=["blue","purple","red","yellow"]
        for x in range(300):
            t.color(colors[x%4])
            t.fd(x)
            t.left(90)
    elif op==("D"):
        t.screen.bgcolor("black")
        colors=["blue","purple","red","yellow","orange","brown"]
        for x in range(300):
            t.color(colors[x%6])
            t.fd(x)
            t.left(59)
    elif op==("E"):
        t.screen.bgcolor("white")
        colors=["red","green","blue","orange"]
        for x in range(200):
            t.color(colors[x%4])
            t.fd(x)
            t.left(91)
            
    t.hideturtle()
    conti=ns(input("¿Continuar?: "))
    if conti==("s"):
        t.reset()
        t.hideturtle()
        subprocess.call(["cmd.exe","/C","cls"])
    else:
        break
            
