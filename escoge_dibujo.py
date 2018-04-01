from turtle import Turtle
from VALID import OKI, ns, opt
import subprocess

def ver(lii):
    try:
        lii[0]==int(lii[0])
        lii[1]==int(lii[1])
        lii[2]==str(lii[0])
        return lii
    except:
        return False

#def col(lista):
    
        

def datt(li):
    li=li.split(",")
    lista=[]
    for i in li:
        try:
            i=int(i)
        except:
            try:
                i=float(i)
            except:
                i=str(i)
        lista.append(i)
    return lista

while True:
    t=Turtle()
    print("Escoja dibujo.")
    print("A)Flor")
    print("B)Hexagono com")
    print("C)Cuadrado")
    print("D)Hexagono simp")
    print("E)Cuadrado spiral")
    print("F)Raizes")
    print("G)Crear fig personalizada")
    op=opt(input("Introduzca su opción: "),["A","B","C","D","E","F","G"])
    
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
    elif op==("F"):
        import random
        atrib=[200,90,"black"]
        colors=["red","green","pink","blue","orange","yellow"]
    elif op==("G"):
        atrib=ver(datt(input("Introduce nºciclos, gragos giro y color de fondo, separados por coma: ")))
        while atrib==False:
            atrib=ver(datt(input("Orden incorrecto: ")))
        colors=datt(input("Introduce colores separados por coma: "))
        
            
    t.screen.bgcolor(atrib[2])
    for x in range(atrib[0]):
        if op==("A"):
            t.circle(x)
        t.color(colors[x%(len(colors))])
        if op==("B"):
                t.pensize(x/10+1)
        if op!=("A") and op!=("F"):
                t.fd(x)
        t.left(atrib[1])
        if op==("F"):
            sent=random.choice(["D","L","U","DW"])
            tam=random.randint(20,40)
            if sent==("D"):
                t.fd(tam)
                t.right(atrib[1])
            elif sent==("L"):
                t.fd(tam)
                t.left(atrib[1])
            elif sent==("U"):
                t.fd(tam)
            elif sent==("DW"):
                t.fd(tam)

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
    
