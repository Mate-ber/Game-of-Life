import time
from turtle import Screen
import turtle
from GameOfLifeBlocks import Cell

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
centre = turtle.Turtle()
centre.shape("square")
centre.color("green")
centre.penup()
centre.goto(0, 0)
cell = Cell()
i = 99
while i > 0:
    time.sleep(1)
    screen.update()
    cell.update_grid()
    i -= 1
screen.exitonclick()


