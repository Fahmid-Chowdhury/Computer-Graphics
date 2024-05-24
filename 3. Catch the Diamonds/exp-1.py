from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math
import random

W_Width, W_Height = 500, 700


dmdX, dmdY = random.uniform(50, 450), 650
bx, by = 250, 20
px, py = 250, 675
bkx, bky = 0, 675
ex, ey = 450, 700
speed = 0.06
score = 0
color = [random.uniform(0.6, 1.0), random.uniform(0.6, 1.0), random.uniform(0.6, 1.0)]
colorb = [1, 1, 1]
play = True
gameOver = False

def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x 
    b = (W_Height) - y 
    return a, b
    
def OriginalZone(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y
    
def zoneChangeToZero(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y
    
def drawLine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    zone = 0
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx < 0 and dy >= 0:
            zone = 3
        elif dx < 0 and dy < 0:
            zone = 4
        elif dx >= 0 and dy < 0:
            zone = 7
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx < 0 and dy >= 0:
            zone = 2
        elif dx < 0 and dy < 0:
            zone = 5
        elif dx >= 0 and dy < 0:
            zone = 6
    glColor3f(color[0], color[1], color[2])
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x1, y1)
    x1, y1 = zoneChangeToZero(x1, y1, zone)
    x2, y2 = zoneChangeToZero(x2, y2, zone)
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    dE = 2 * dy
    dNE = 2 * (dy - dx)
    x, y = x1, y1
    while x < x2:
        if d <= 0:
            d += dE
            x += 1
        else:
            d += dNE
            x += 1
            y += 1
        xx , yy = OriginalZone(x, y, zone)
        glVertex2f(xx, yy)
    glEnd()

def drawDiamond(x, y, color):
    drawLine(x, y, x-15, y-20, color)
    drawLine(x-15, y-20, x, y-40, color)
    drawLine(x, y-40, x+15, y-20, color)
    drawLine(x+15, y-20, x, y, color)
    
def drawBasket(x, y, colorb):
    drawLine(x-70, y, x+70, y, colorb)
    drawLine(x-40, 1, x+40, 1, colorb)
    drawLine(x-40, 1, x-70, y, colorb)
    drawLine(x+40, 1, x+70, y, colorb)

def drawExit(x, y, color):
    drawLine(x, y, x+50, y-50, color)
    drawLine(x, y-50, x+50, y, color)

def drawBack(x, y, color):
    drawLine(x, y, x+50, y, color)
    drawLine(x, y, x+20, y+25, color)
    drawLine(x, y, x+20, y-25, color)   

def drawPausePlay(x, y, color):
    if not play:
        drawLine(x-25, y+25, x-25, y-25, color)
        drawLine(x-25, y+25, x+25, y, color)
        drawLine(x-25, y-25, x+25, y, color)
    if play:
        drawLine(x-20, y+25, x-20, y-25, color)
        drawLine(x+20, y+25, x+20, y-25, color)

def keyboardListener(key, x, y):
    global play
    if key == b' ':
        if play:
            play = False
        else:
            play = True
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global bx, by
    if not gameOver and play:
        if key==GLUT_KEY_RIGHT:
            if bx + 70 != 500:
                bx = bx + 10
        if key==GLUT_KEY_LEFT:
            if bx - 70 != 0:
                bx = bx - 10

def mouseListener(button, state, x, y):	#/#/x, y is the x-y of the screen (2D)
    global play, color, dmdX, dmdY, gameOver, speed, score, colorb
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
            x, y = convert_coordinate(x,y)
            if bkx <= x <= bkx+50 and bky-25 <= y <= bky+25:
                if gameOver:
                    play = True
                    gameOver = False
                    print("Starting Over!")
                    dmdX = random.uniform(50, 450)
                    dmdY = 650
                    speed = 0.06
                    score = 0
                    colorb = [1, 1, 1]
                    color = [random.random(), random.random(), random.random()]
                else:
                    play = True
                    print("Restarting!")
                    dmdX = random.uniform(50, 450)
                    dmdY = 650
                    speed = 0.06
                    score = 0
                    color = [random.random(), random.random(), random.random()]
            if px-25 <= x <= px+25 and py-25 <= y <= py+25:
                if not gameOver:
                    if play:
                        play = False
                    else:
                        play = True
            if ex <= x <= ex+50 and ey-50 <= y <= ey:
                print("Exiting! Total Score:", score)
                glutLeaveMainLoop()  
    glutPostRedisplay()


def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    # iterate()
    glViewport(0, 0, 500, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 700, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    #//initialize the matrix
    global dmdX , dmdY, bx, by, color, colorb, gameOver
    if not gameOver:
        drawDiamond(dmdX, dmdY, color)
    drawBasket(bx, by, colorb)
    drawExit(ex, ey, [1, 0, 0])
    drawBack(bkx, bky, [0, 0, 1])
    drawPausePlay(px, py, [0, 1, 0])
    glutSwapBuffers()


def animate():
    #//codes for any changes in Models, Camera
    glutPostRedisplay()
    global dmdX, dmdY, speed, score, color, colorb, play, gameOver, x2
    if play:
        if math.floor(dmdY-40) == by and dmdX > bx-70 and dmdX < bx+70:
            dmdX = random.uniform(50, 450)
            dmdY = 650
            speed += 0.02
            score += 1
            color = [random.random(), random.random(), random.random()]
            print("Score:", score)
        elif math.floor(dmdY-40) > by:
            dmdY = (dmdY - speed)
        else:
            print("Game Over! Score:", score)
            score = 0
            colorb = [1, 0, 0]
            play = False
            gameOver = True


def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    #**(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) # //Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)   #display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()		#The main loop of OpenGL
