from turtle import *
from math import *

colormode(255)
bgcolor(39,40,34)
speed(0)

Turtle()
hideturtle()

setpos(-1200, -670)

GRA = 90
GRAN = -90

le = 2

b = 1
a = 1
x = 1
y = 1
z = 1

pensize(2)
setheading(0)


while b <= 5:

    while a <= 5:

        while x <= 5:

            while y <= 5:

                while z <= 5:

                    pencolor("black")
                    fd(le)
                    lt(GRA)
                    pencolor("gray")
                    fd(le)
                    lt(GRAN)
                    pencolor("white")
                    fd(le)
                    lt(GRAN)
                    pencolor("gray")
                    fd(le)
                    lt(GRA)
                    pencolor("black")
                    fd(le)

                    if z == 1:
                        lt(GRA)

                    elif z == 2:
                        lt(GRAN)

                    elif z == 3:
                        lt(GRAN)

                    elif z == 4:
                        lt(GRA)

                    z = z + 1

                z = 1

                if y == 1:
                    lt(GRA)

                elif y == 2:
                    lt(GRAN)

                elif y == 3:
                    lt(GRAN)

                elif y == 4:
                    lt(GRA)

                y = y + 1

            y = 1

            if x == 1:
                lt(GRA)

            elif x == 2:
                lt(GRAN)

            elif x == 3:
                lt(GRAN)

            elif x == 4:
                lt(GRA)

            x = x + 1

        x = 1

        if a == 1:
            lt(GRA)

        elif a == 2:
            lt(GRAN)

        elif a == 3:
            lt(GRAN)

        elif a == 4:
            lt(GRA)

        a = a + 1

    a = 1

    if b == 1:
        lt(GRA)

    elif b == 2:
        lt(GRAN)

    elif b == 3:
        lt(GRAN)

    elif b == 4:
        lt(GRA)

    b = b + 1

b = 1
exitonclick()
