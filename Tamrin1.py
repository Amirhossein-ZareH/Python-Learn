import turtle

color = input("plz enter a color of your favor: (red/blue/yellow)")
if color == "red":
    turtle.color("red")
elif color == "blue":
    turtle.color("blue")
elif color == "yellow":
    turtle.color("yellow")
else:
    print (f("the {color} is not supported"))
    
shape = input("now plz enter a shape of your favor: (triangle/circle/square)")
if shape == "triangle":
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
elif shape == "circle":
    turtle.circle(50)
elif shape == "square":
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
else:
    print(f"shape {shape} is not recognized")
    
turtle.done()

