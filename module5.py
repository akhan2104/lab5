for i in range(100):
    print("hello world")


lists=[12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in range(len(lists)):
    print(lists[i])


for i in range(len(lists)):
    square= lists[i] * lists[i]
    print(lists[i],"and its square is",square)



import turtle      
display = turtle.Screen()  
Adnan = turtle.Turtle()
Adnan.speed(0)
 
sides = int(input ("Number of sides in polygon?"  ))
length = int(input ("Length of the sides in polygon?" ))
colorname = input ("Color of polygon?" )
fcolor = input ("Fill color of polygon?")
 
Adnan.color(colorname)
Adnan.fillcolor(fcolor)
Adnan.begin_fill()
for i in range(sides):
   Adnan.forward (length)
   Adnan.left (360 / sides)
Adnan.end_fill()

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    elif i % 3 == 0:
        print("Divisible by three")
    elif i % 5 == 0:
        print("Divisible by five")
    else:
        print(i)


# Set up the turtle screen and pen
t = turtle.Turtle()
t.speed(0) # Set the drawing speed to the fastest possible
turtle.bgcolor("black") # Set the background color to black

# Draw the outer hexagon
t.penup()
t.goto(0, 200)
t.pendown()
t.pensize(3)
t.color("white")
for i in range(6):
    t.forward(100)
    t.right(60)

# Draw the inner hexagons and fill with color
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(6):
    t.penup()
    t.goto(0, 150)
    t.pendown()
    t.pensize(2)
    t.color(colors[i])
    t.right(60*i)
    t.forward(60)
    t.right(120)
    for j in range(6):
        t.forward(40)
        t.right(60)
    t.begin_fill()
    for j in range(6):
        t.forward(40)
        t.right(60)
    t.end_fill()

turtle.done()


#Mohammed Adnan Khan









































        
