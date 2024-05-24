from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

W_Width, W_Height = 500,500


cor = []
start = -800
target = 1600
noOfPoints = 200
for i in range(noOfPoints):
    start = start + target//noOfPoints
    cor.append(start)
    
cor2 = []
for i in range(len(cor)):
    cor2.append(cor[i] + 2)

speed = []
for i in range(len(cor)):
    speed.append(random.uniform(0.1, 0.5))

base = 250
bx = cor
cor = tuple(cor)
by = [250]*len(cor)
bxx = cor2
color = [0.0, 0.0, 0.0]

arr = bxx


def drawHouse():
    glLineWidth(5)
    global m1, m2
    glBegin(GL_LINES)
    glColor3f(0.5, 0.0, 1.0)
    # roof
    glVertex2f(100, 65)
    glVertex2f(0, 100)
    m1 = (65-100)/(100-0)
    
    glVertex2f(-100, 65)
    glVertex2f(0, 100)
    m2 = (65-100)/(-100-0)
    # wall
    glVertex2f(80, -20)
    glVertex2f(80, 65)

    glVertex2f(-80, -20) 
    glVertex2f(-80, 65)
    # line under roof
    glVertex2f(100, 65)
    glVertex2f(-100, 65)
    # base
    glVertex2f(82.5, -20)
    glVertex2f(-82.5, -20)
    glEnd()
    
def drawDoorWindow():  
    glLineWidth(1)  
    # door
    glBegin(GL_LINES)
    glColor3f(0.5, 0.0, 1.0)
    glVertex2f(-60, 40)
    glVertex2f(-60, -20)
    
    glVertex2f(-20, 40)
    glVertex2f(-20, -20)
    
    glVertex2f(-60, 40)
    glVertex2f(-20, 40)
    # window
    glVertex2f(60, 40)
    glVertex2f(60, 10)
    glVertex2f(30, 40)
    glVertex2f(30, 10)
    glVertex2f(60, 40)
    glVertex2f(30, 40)
    glVertex2f(60, 10)
    glVertex2f(30, 10)
    glVertex2f(45, 40)
    glVertex2f(45, 10)
    glVertex2f(60, 25)
    glVertex2f(30, 25)
    glEnd()
    
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(-30, 10) #jekhane show korbe pixel
    glEnd()
    
def clipping(x, y, i):
    if 0 < x < 100:
        if math.floor(-y + m1*x + 100) == 0:
            x = cor[i]
            y = base
    elif -100 < x < 0:
        if math.floor(-y + m2*x + 100) == 0:
            x = cor[i]
            y = base
    return x, y

def speedCheck(sp, i):
    global m, dx, dy
    m = base/(cor[i]-bxx[i])
    d = math.atan(m)
    c = math.cos(d)
    s = math.sin(d)
    dx = abs(sp*(c))
    dy = abs(sp*(s))
    return dx, dy

def slopeCheck(x, y, x1, sp, n=0):
    global m , dx, dy
    dx, dy = speedCheck(sp, n)
    if x == x1:
        x = x 
        y = y - sp
        if math.floor(y) <= 0:
            x = cor[n]
            y = base
        x, y = clipping(x, y, n)
        return x, y
    if 0 < m < 1:
        x -= dx
        y -= m*(dx)
        if math.floor(y) <= 0:
            x = cor[n]
            y = base
        x, y = clipping(x, y, n)
        return x, y
    elif m > 1:
        x -= (1/m)*dy
        y -= dy
        if math.floor(y) <= 0:
            x = cor[n]
            y = base
        x, y = clipping(x, y, n)
        return x, y
    elif m < -1:
        x -= (1/m)*dy
        y -= dy
        if math.floor(y) <= 0:
            x = cor[n]
            y = base
        x, y = clipping(x, y, n)
        return x, y
    elif -1 < m < 0:
        x += dx
        y += m*(dx)
        if math.floor(y) <= 0:
            x = cor[n]
            y = base
        x, y = clipping(x, y, n)
        return x, y

def drawRain(x, y, i):
    global m
    m = base/(cor[i]-bxx[i])
    glColor3f(0, 0.2, 1)
    glBegin(GL_LINES)
    y1 = y + 20
    x1 = x + 20/m
    glVertex2f(x, y)
    glVertex2f(x1, y1)
    glEnd()

def keyboardListener(key, x, y):
    if key == b'd':
        if color[2] < 1.0:
            color[0] += 0.2
            color[1] += 0.2
            color[2] += 0.2

    if key == b'n':
        if color[2] > 0:
            color[0] -= 0.2
            color[1] -= 0.2
            color[2] -= 0.2
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global cor2, bxx
    glutPostRedisplay()
    if key==GLUT_KEY_RIGHT:
        cor2 = list(x + 5 for x in cor2)
        bxx = cor2
    if key==GLUT_KEY_LEFT:
        cor2 = list(x - 5 for x in cor2)
        bxx = cor2
        

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(color[0], color[1], color[2], 1.0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    # iterate()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,    0,1,0)
    glMatrixMode(GL_MODELVIEW)

    global bx, by
    for i in range(len(cor)):
        drawRain(bx[i], by[i], i)
    
    drawHouse()
    drawDoorWindow()

    glutSwapBuffers()

def animate():
    #//codes for any changes in Models, Camera
    glutPostRedisplay()
    global bx, by, bxx, cor2, arr
    for i in range(len(cor)):
        bx[i], by[i] = slopeCheck(bx[i], by[i], bxx[i], speed[i], i)
 
    

def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
# glutMouseFunc(mouseListener)

glutMainLoop()		#The main loop of OpenGL
