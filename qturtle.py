import turtle as t
from error import Qin_input_type_check,Qin_TooBig_TooSmall_input_check
@Qin_input_type_check({"width":int,"height":int,"startx":int,"starty":int})
def setup(width=500, height=500, startx=None, starty=None):
    t.setup(width, height, startx, starty)
@Qin_input_type_check({"canvwidth":int,"canvheight":int,"bg":str})
def screensize(canvwidth=500, canvheight=500, bg=None):
    t.screensize(canvwidth, canvheight, bg)
@Qin_input_type_check({"titlestring":str})
def title(titlestring):
    t.title(titlestring)
def bye():
    t.bye()
def textinput(title, prompt):
    return t.textinput(title, prompt)
def numinput(title, prompt, default=None, minval=None, maxval=None):
    return t.numinput(title, prompt, default, minval, maxval)
@Qin_input_type_check({"x":int,"y":int})
def up(x,y):
    t.up()
    t.goto(x,y)
@Qin_input_type_check({"x":int,"y":int})
def down(x,y):
    t.down()
    t.goto(x,y)
@Qin_input_type_check({"x":int,"y":int})
@Qin_input_type_check({"r":int,"g":int,"b":int})
def colorFromRGB(r,g,b):
    t.color((r/255,g/255,b/255))
def clearscreen():
    t.clearscreen()
@Qin_input_type_check({"n":int,"l":int})
def draw_polygon(n,l):
    for i in range(n):
        t.forward(l)
        t.left(360/n)
@Qin_input_type_check({"l":int})
def draw_star(l):
    for i in range(5):
        t.forward(l)
        t.left(180-180/5)
@Qin_input_type_check({"color":str})
def fill_color(color):
    t.fillcolor(color)
def begin_fill():
    t.begin_fill()
def end_fill():
    t.end_fill()
@Qin_input_type_check({"l":int})
def forward(l):
    t.forward(l)
@Qin_input_type_check({"text":str})
def draw_text(text):
    t.write(text)
@Qin_input_type_check({"speed":int})
def speed(speed):
    t.speed(speed)
@Qin_input_type_check({"color":str})
def bgcolor(color):
    t.bgcolor(color)
@Qin_input_type_check({"color":str})
def pencolor(color):
    t.pencolor(color)
@Qin_input_type_check({"size":int})
def pensize(size):
    t.pensize(size)
def hideturtle():
    t.hideturtle()
def showturtle():
    t.showturtle()
def reset():
    t.reset()
def clear():
    t.clear()
def exitonclick():
    t.exitonclick()
@Qin_input_type_check({"flag":bool})
def tracer(flag):
    t.tracer(flag)
def undo():
    t.undo()

def home():
    t.home()
def up():
    t.up()
def down():
    t.down()
def left():
    t.left(90)
def right():
    t.right(90)
@Qin_input_type_check({"l":int})
def backward(l):
    t.backward(l)
@Qin_input_type_check({"x":float,"y":float})
def goto(x,y):
    t.goto(x,y)
@Qin_input_type_check({"x":int,"y":int})
def setpos(x,y):
    t.setpos(x,y)
@Qin_input_type_check({"h":int})
def setheading(h):
    t.setheading(h)
@Qin_input_type_check({"x":int,"y":int,"radius":int})
def circle(r,extent=360,steps=None):
    t.circle(r,extent,steps)
@Qin_input_type_check({"size":int,"color":str})
def dot(size=None,color=None):
    t.dot(size,color)
def begin_fill():
    t.begin_fill()
def end_fill():
    t.end_fill()
@Qin_input_type_check({"color":str})
def color(color, *args):
    t.color(color, *args)
@Qin_input_type_check({"width":int})
def pensize(width):
    t.pensize(width)
@Qin_input_type_check({"width":int})
def width(w):
    t.width(w)
def random_color():
    import random
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    t.color((r/255,g/255,b/255))
def random_color_hsv():
    import random
    import colorsys
    h = random.random()
    s = random.uniform(0.5,1)
    v = random.uniform(0.5,1)
    return colorsys.hsv_to_rgb(h,s,v)
def done():
    t.done()
def onscreenclick(fun, btn=1, add=None):
    t.onscreenclick(fun, btn, add)
def onclick(fun, btn=1, add=None):
    t.onclick(fun, btn, add)
def onkey(fun, key):
    t.onkey(fun, key)
def onkeypress(fun, key):
    t.onkeypress(fun, key)
def onkeyrelease(fun, key):
    t.onkeyrelease(fun, key)
def onrelease(fun):
    t.onrelease(fun)
def listen():
    t.listen()
def ondrag(fun, btn=1, add=None):
    t.ondrag(fun, btn, add)
def onrelease(fun):
    t.onrelease(fun)
def bk(x):
    t.bk(x)
def fd(x):
    t.fd(x)
def lt(a):
    t.lt(a)
def rt(a):
    t.rt(a)
def pu():
    t.pu()
def pd():
    t.pd()
def st():
    t.st()
def ht():
    t.ht()
def isdown():
    return t.isdown()
def isvisible():
    return t.isvisible()
def shape(name):
    t.shape(name)
@Qin_input_type_check({"stretch_wid":int, "stretch_len":int, "outline":int})
def shapesize(stretch_wid=None, stretch_len=None, outline=None):
    t.shapesize(stretch_wid, stretch_len, outline)
@Qin_input_type_check({"shear":float})
def shearfactor(shear):
    t.shearfactor(shear)
@Qin_input_type_check({"angle":float})
def settiltangle(angle):
    t.settiltangle(angle)
@Qin_input_type_check({"angle":float})
def tilt(angle):
    t.tilt(angle)
def tiltangle():
    return t.tiltangle()
@Qin_input_type_check({"m":int})
def shapetransform(m):
    t.shapetransform(m)
@Qin_input_type_check({"delay":int})
def delay(delay):
    t.delay(delay)
@Qin_input_type_check({"mode":int})
def colormode(mode):
    t.colormode(mode)
def getcanvas():
    return t.getcanvas()
def getturtle():
    return t.getturtle()
def getpen():
    return t.getpen()
def getscreen():
    return t.getscreen()
def getshapes():
    return t.getshapes()
def get_shapepoly():
    return t.get_shapepoly()
@Qin_input_type_check({"angle":float})
def seth(angle):
    t.seth(angle)
def setx(x):
    t.setx(x)
def sety(y):
    t.sety(y)
