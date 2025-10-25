#مثلث

h = int(input("plz enter height: "))

for i in range(1, h + 1):
    print(" " * (h - i) + "*" * (2 * i - 1))


#مثلث برعکس

h = int(input("plz enter height: "))

for i in range(h, 0, -1):
    print(" " * (h - i) + "*" * (2 * i - 1))


#لوزی

h = int(input("plz enter height: "))

for i in range(1, h + 1):
    print(" " * (h - i) + "*" * (2 * i - 1))

for i in range(h - 1, 0, -1):
    print(" " * (h - i) + "*" * (2 * i - 1))


#مثلث چپه

h = int(input("plz enter height: "))

for i in range(1, h + 1):
    print(" " * (h - i) + "*" * i)

for i in range(h - 1, 0, -1):
    print(" " * (h - i) + "*" * i)


#مثلت راسته

h = int(input("plz enter height: "))

for i in range(1, h + 1):
    print("*" * i)

for i in range(h - 1, 0, -1):
    print("*" * i)



#سوال tutle 

import turtle

t = turtle.Turtle()

shape = input("what do you want? (triangle, square, 5side, 6side, circle): ").strip().lower()

length = 100

if shape == "triangle":
    n = 3
elif shape == "square":
    n = 4
elif shape == "5side":
    n = 5
elif shape == "6side":
    n = 6
elif shape == "circle":
    t.circle(100)
    turtle.done()
    exit()
else:
    print("invalid!")
    turtle.done()
    exit()

for _ in range(n):
    t.forward(length)
    t.right(360 / n)

turtle.done()