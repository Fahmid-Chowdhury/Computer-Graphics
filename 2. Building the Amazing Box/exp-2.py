from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

points = []
speed = 1
play = True
blink = False

def mouseListener(button, state, x, y):
    global blink
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        color = [random.random(), random.random(), random.random(), 1]
        dirc = random.choice([(1, 1), (-1, 1), (1, -1), (-1, -1)])
        point = [x, 500-y, dirc[0], dirc[1], color]
        points.append(point)
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if blink:
            blink = False
        else:
            blink = True
        
def keyboardListener(key, x, y):
    global speed, play
    if key == b' ':
        if play:
            play = False
        else:
            play = True
    elif key == GLUT_KEY_UP:
        speed += 1
    elif key == GLUT_KEY_DOWN:
        if speed > 1:
            speed -= 1
        else:
            speed = 1  
        
def draw_points(x, y, size, color):
    # Draw a point from the given x and y coordinates
    glColor4f(color[0], color[1], color[2], color[3])
    glPointSize(size) 
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_POINTS)
    glVertex2f(x,y) 
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glLoadIdentity()
    iterate()
    
    for p in points:
        draw_points(p[0], p[1], 10, p[4])
    glutSwapBuffers()
    
def animate(yoo):
    if play:
        for p in points:
            p[0] += p[2]*speed
            p[1] += p[3]*speed
            if blink:
                p[4][3] = (p[4][3]+0.1)%1
            if p[0] > 500 or p[0] < 0:
                p[2] *= -1
            if p[1] > 500 or p[1] < 0:
                p[3] *= -1
       
    glutTimerFunc(30, animate, "yoo")
    glutPostRedisplay()
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutIdleFunc(animate("yoo"))#what you want to do in the idle time (when no drawing is occuring)
glutMouseFunc(mouseListener)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(keyboardListener)
glutMainLoop()