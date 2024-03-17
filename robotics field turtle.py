from turtle import *
import time

bgcolor('white')
pencolor('black')
penup()
setpos(-200,-200)
pensize(10)
pencolor('black')
pendown()
def square():
    for i in range(4):
        fd(550)
        lt(90)
square()

penup()
lt(90)
fd(20)
rt(90)

pendown()
pencolor('green')
def uphill():
    pensize(2)
    fd(50)
    lt(90)
    fd(500)
    rt(90)
    fd(50)
    rt(90)
    fd(500)
    lt(90)
for i in range(5):
    uphill()
fd(60)
penup()
shape("triangle")
setpos(-200,-180)
pendown()
uphill()
time.sleep(5)