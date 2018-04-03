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

def col(lista):
    n=1
    res=[]
    for i in lista:
        if n>=4:
            res.append(i)
        n+=1
    return res
            
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
    print("Escoja opción.")
    print("A)Demo1 (Flor)")
    print("B)Demo2 (Hexagono com)")
    print("C)Demo3 (Cuadrado)")
    print("D)Demo4 (Hexagono simp)")
    print("E)Demo5 (Cuadrado spiral)")
    print("F)Crear fig personalizada")
    print("G)Cargar figura guardada")
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
        atrib=ver(datt(input("Introduce nºciclos, long lineas y color de fondo, separados por coma: ")))
        while atrib==False:
            atrib=ver(datt(input("Orden incorrecto: ")))
        colors=datt(input("Introduce colores separados por coma: "))
    elif op==("G"):
        import pickle
        fig=input("Introduzca el nombre de la figura guardada que desea ver: ")
        while True:
            try:
                atrib=pickle.load(open(fig,"rb"))
                colors=col(atrib)
                break
            except:
                fig=input("El archivo solicitado no se encontró o no es apto para este programa: ")

    try:
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
    except:
        print("El archivo",fig,"no es apto para ser ejecutado en este programa")

    if op==("F"):
        guard=ns(input("¿Desea guardar el dibujo creado?: "))
        if guard==("s"):
            import pickle
            dibujo=atrib+colors
            nom=input("¿Que nombre desea dar  al dibujo?: ")
            pickle.dump(dibujo,open(nom,"wb"))
        

    
    conti=ns(input("¿Continuar?: "))
    if conti==("s"):
        t.reset()
        t.hideturtle()
        subprocess.call(["cmd.exe","/C","cls"])
    else:
        break
#t.screen.exitonclick()
#t.screen.mainloop()
    
