from turtle import *


#we want to paint a house

#step 1: draw a square
width(5)
color("blue")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of the square

#drawing za door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#roof

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#window No 1
penup()
goto(30, 170)
pendown()

color("cyan")
left(30)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(17.5)
left(90)
forward(35)
left(90)
forward(17.5)
left(90)
forward(17.5)
left(90)
forward(35)

#window No 2

penup()
goto(170, 170)
pendown()

color("cyan")
left(-90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(17.5)
left(90)
forward(35)
left(90)
forward(17.5)
left(90)
forward(17.5)
left(90)
forward(35)

exitonclick()