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
    op=opt(input("Introduzca su opción: "),["A","B","C","D","E"])
    
    if op==("A"):
        atrib=[100,60,"black"]
        colors=["red","yellow","purple"]
    elif op==("B"):
        atrib=[150,59,"white"]
        colors=["red","purple","blue","green","orange"]
    elif op==("C"):
        atrib=[300,90,"black"]
        colors=["blue","purple","red","yellow"]
    elif op==("D"):
        atrib=[300,59,"black"]
        colors=["blue","purple","red","yellow","orange","brown"]
    elif op==("E"):
        atrib=[200,91,"white"]
        colors=["red","green","blue","orange"]
            
    t.screen.bgcolor(atrib[2])
    for x in range(atrib[0]):
        if op==("A"):
            t.circle(x)
        t.color(colors[x%(len(colors))])
        if op==("B"):
                t.pensize(x/10+1)
        if op!=("A"):
                t.fd(x)
        t.left(atrib[1])

    t.hideturtle()
    conti=ns(input("¿Continuar?: "))
    if conti==("s"):
        t.reset()
        t.hideturtle()
        subprocess.call(["cmd.exe","/C","cls"])
    else:
        break
#t.screen.exitonclick()
#t.screen.mainloop()
    
