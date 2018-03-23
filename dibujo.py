from turtle import Turtle
t=Turtle()
t.screen.bgcolor("black")
colors=["red","yellow","purple"]
#t.screen.tracer(0,0)

for x in range(100):
    t.circle(x)#"x" va tomando los valores del rango, por lo que el circulo se irá incrementando
    t.color(colors[x%3])
    t.left(60)
#t.screen.exitonclick()
#t.screen.mainloop()
    
