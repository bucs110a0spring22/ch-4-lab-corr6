import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def setupWindow(myWindow = None):
  myWindow.reset()
  myWindow.setworldcoordinates(-360,-1,360,1)
def setupAxis(dart = None):
  dart.up()
  dart.goto(-360,0)
  dart.down()
  dart.goto(360,0)
  dart.up()
  dart.goto(0,-360)
  dart.down()
  dart.goto(0,360)
def drawSineCurve(dart = None):
  dart.up()
  dart.goto(-360,0)
  dart.color('blue')
  dart.down()
  for i in range(-360,361):
    y=math.sin(math.radians(i))
    dart.goto(i,y)
def drawCosineCurve(dart = None):
  dart.up()
  dart.goto(-360,1)
  dart.color('red')
  dart.down()
  for i in range(-360,361):
    y=math.cos(math.radians(i))
    dart.goto(i,y)
def drawTangentCurve(dart = None):
  dart.up()
  dart.goto(-360,0)
  dart.color('green')
  dart.down()
  for i in range(-360,361):
    y=math.tan(math.radians(i))
    dart.goto(i,y)
##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
