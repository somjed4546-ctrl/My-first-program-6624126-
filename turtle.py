import turtle
import random
import math

# =========================
# SETUP
# =========================
screen = turtle.Screen()
screen.setup(1000, 700)
screen.bgcolor("black")
screen.title("Turtle Space")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# =========================
# STARS
# =========================
star = turtle.Turtle()
star.speed(0)
star.hideturtle()
star.penup()

for i in range(200):
    x = random.randint(-480, 480)
    y = random.randint(-330, 330)

    star.goto(x, y)

    size = random.choice([1,2, 3, 4])

    star.dot(size, random.choice([
        "white",
        "lightblue",
        "yellow",
        "lightgray",
        "Red",
        "violet",
        "orange"
    ]))
# =========================
# MOON
# =========================
moon = turtle.Turtle()
moon.speed(0)
moon.hideturtle()
moon.penup()

moon.goto(-300, 180)
moon.color("lightgray")
moon.dot(100)

# Moon craters
for i in range(12):
    x = random.randint(-340, -260)
    y = random.randint(140, 220)

    moon.goto(x, y)
    moon.dot(random.randint(5, 15), "gray")

# =========================
# PLANET
# =========================
planet = turtle.Turtle()
planet.speed(0)
planet.hideturtle()
planet.penup()

planet.goto(250, 80)
planet.dot(180, "royalblue")

# Continents
for i in range(15):
    x = random.randint(180, 320)
    y = random.randint(10, 150)

    planet.goto(x, y)
    planet.dot(random.randint(10, 30), "green")


# =========================
# Cat star
# =========================

cat = turtle.Turtle()
cat.speed(0)
cat.hideturtle()
cat.penup()

# H.
cat.goto(180, -180)
cat.color("Orange")
cat.dot(80)

# L.E
cat.goto(145, -140)
cat.setheading(0)
cat.pendown()
cat.begin_fill()
cat.goto(150, -100)
cat.goto(175, -135)
cat.goto(145, -140)
cat.end_fill()
cat.penup()

# R.E
cat.goto(185, -135)
cat.pendown()
cat.begin_fill()
cat.goto(215, -100)
cat.goto(220, -140)
cat.goto(185, -135)
cat.end_fill()
cat.penup()

# L.eye
cat.goto(165, -175)
cat.dot(12, "black")

# R.eye
cat.goto(195, -175)
cat.dot(12, "black")

# N.
cat.goto(180, -195)
cat.dot(8, "pink")

# M.
cat.goto(180, -200)
cat.setheading(-45)
cat.pendown()
cat.forward(10)
cat.penup()
# =========================
# Dog Star
# =========================

dog = turtle.Turtle()
dog.speed(0)
dog.hideturtle()
dog.penup()
# H.
dog.goto(-300, -200)
dog.color("yellow")
dog.dot(120)
# L.E
dog.goto(-350, -150)
dog.color("brown")
dog.begin_fill()

dog.pendown()
dog.goto(-300, -150)
dog.goto(-325, -240)
dog.goto(-350, -150)

dog.end_fill()
dog.penup()
# R.E
dog.goto(-300, -150)
dog.color("brown")
dog.begin_fill()

dog.pendown()
dog.goto(-250, -150)
dog.goto(-275, -240)
dog.goto(-300, -150)

dog.end_fill()
dog.penup()
# L.eye
dog.goto(-325, -190)
dog.dot(12, "black")
# R.eye
dog.goto(-275, -190)
dog.dot(12, "black")
# N.
dog.goto(-300, -215)
dog.dot(10, "black")
# M.
dog.goto(-300, -220)
dog.setheading(-45)
dog.pendown()
dog.forward(10)
dog.penup()
# =========================
# SHOOTING STARS
# =========================

shooting = turtle.Turtle()
shooting.speed(0)
shooting.hideturtle()
shooting.penup()

# 1
shooting.goto(-100, -50)
shooting.setheading(-35)
shooting.color("white")
shooting.pensize(3)

shooting.pendown()
shooting.backward(250)
shooting.penup()

shooting.goto(-100, -50)
shooting.dot(8, "white")


# 2
shooting.goto(350, 200)
shooting.setheading(-35)
shooting.color("lightblue")
shooting.pensize(2)

shooting.pendown()
shooting.backward(150)
shooting.penup()

shooting.goto(350, 200)
shooting.dot(7, "lightblue")

# =========================
# TITLE
# =========================
text = turtle.Turtle()
text.hideturtle()
text.penup()

text.goto(-150, -270)
text.color("white")
text.write(
    "It's okay to be Asia",
    font=("Arial", 20, "bold")
)
text.goto(-150, -300)
text.color("white")
text.write(
    "It's okay to be White",
    font=("Arial", 20, "bold")
)
text.goto(-150, -330)
text.color("white")
text.write(
    "It's okay to be ",
    font=("Arial", 20, "bold")
)
turtle.done()
