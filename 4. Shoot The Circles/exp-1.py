from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

W_Width, W_Height = 500, 700

zones = []
score = 0
check = 0
shtrx , shtry = 250, 20
px, py = 250, 675
bkx, bky = 0, 675
ex, ey = 450, 700
bltx, blty = shtrx, 2*shtry+5
miss = 0
missFire = 0
shoot = False
play = True
gameOver = False
balls = []
x = random.uniform(50, 450)
y = random.randint(625, 640)
balls.append([x, y, 650-y])


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


def convert_center(x,y,c):
    global W_Width, W_Height
    cx,cy = c[0], c[1]
    x = x + cx
    y = y + cy
    return x, y


def drawPoint(c):
    glBegin(GL_POINTS)
    for i in (zones):
        x, y = convert_center(i[0], i[1], c)
        glVertex2f(x, y)
    glEnd()


def convertToZones(x,y):
    global zones
    zones.append((x,y))
    zones.append((y,x))
    zones.append((y,-x))
    zones.append((x,-y))
    zones.append((-x,-y))
    zones.append((-y,-x))
    zones.append((-y,x))
    zones.append((-x,y))
    
    
def circleDraw(cx,cy,r):
    global zones
    x = 0
    y = r
    zones = []
    convertToZones(x, y)
    d = 1-r
    dE = 2*x + 3
    dSE = 2*x - 2*y + 5
    while x < y:
        dE = 2*x + 3
        dSE = 2*x - 2*y + 5
        if d < 0:
            d += dE
            x += 1
        else:
            d += dSE
            x += 1
            y -= 1
        convertToZones(x, y)
    drawPoint((cx,cy))
    
    
def keyboardListener(key, x, y):
    global play, shtrx, bltx, shoot
    if not gameOver and play:
        if key==b'd':
            if shtrx + shtry != 500:
                shtrx = shtrx + 10
        if key==b'a':
            if shtrx - shtry != 0:
                shtrx = shtrx - 10
        if key==b' ' and shoot == False:
            bltx = shtrx
            shoot = True
    glutPostRedisplay()
    
    
def mouseListener(button, state, x, y):	#/#/x, y is the x-y of the screen (2D)
    global play, color, dmdX, dmdY, gameOver, speed, score, balls, check, miss, missFire, bltx, blty, shtrx, shtry, shoot, zones
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
            x, y = convert_coordinate(x,y)
            if bkx <= x <= bkx+50 and bky-25 <= y <= bky+25:
                if gameOver:
                    play = True
                    gameOver = False
                    print("Starting Over!")
                    shtrx , shtry = 250, 20
                    bltx, blty = shtrx, 2*shtry+5
                    zones = []
                    shoot = False
                    balls = []
                    score = 0
                    check = 0
                    miss = 0
                    missFire = 0
                else:
                    play = True
                    print("Starting Over!")
                    shtrx , shtry = 250, 20
                    bltx, blty = shtrx, 2*shtry+5
                    zones = []
                    shoot = False
                    balls = []
                    score = 0
                    check = 0
                    miss = 0
                    missFire = 0
            if px-25 <= x <= px+25 and py-25 <= y <= py+25:
                if not gameOver:
                    if play:
                        play = False
                    else:
                        play = True
            if ex <= x <= ex+50 and ey-50 <= y <= ey:
                print("Goodbye! Total Score:", score)
                glutLeaveMainLoop()  
    glutPostRedisplay()
    
    
def fallingBalls():
    global balls, check, miss, gameOver, play
    if play and not gameOver:
        if len(balls) < 5:
            if check == 0:
                check += 0.05
            elif math.floor(check) == 50:
                x = random.uniform(50, 450)
                y = random.randint(625, 640)
                balls.append([x, y, 650-y])
                for i in range(len(balls)):
                    balls[i][1] = balls[i][1] - 0.05
                check = 0
            else:
                for i in range(len(balls)):
                    balls[i][1] = balls[i][1] - 0.05
                check += 0.05
        else:
            for i in range(len(balls)):
                balls[i][1] = balls[i][1] - 0.05
                if math.floor(balls[i][1]) <= 0:
                    miss += 1
                    balls.pop(i)
                    break
            if miss == 3:
                balls = []
                miss = 0
                play = False
                gameOver = True
            if gameOver:
                print("Game Over!")
                print("Total Score:", score)

                
def shootingBalls():
    global play, gameOver, shoot, bltx, blty, shtrx, shtry, balls, missFire, score 
    hit = -1
    if not gameOver and play and shoot:
        if math.floor(blty) < 650:
            blty += 1
        else:
            shoot = False
            blty = 2*shtry+5
            missFire += 1
    if not gameOver and play and shoot:
        for i in range(len(balls)):
            x = (bltx - balls[i][0])**2
            y = (blty - balls[i][1])**2
            r = (balls[i][2]+5)**2
            if (x + y) <= r:
                hit = i
                score += 1
                print("Score:", score)
    if not gameOver and play:
        for i in range(len(balls)):
            x = (shtrx - balls[i][0])**2
            y = (shtry - balls[i][1])**2
            r = (balls[i][2]+20)**2
            if (x + y) <= r:
                blty = 2*shtry+5
                balls = []
                play = False
                gameOver = True
                break
        if gameOver:
            print("Game Over!")
            print("Total Score:", score)
    if hit != -1:
        balls.pop(hit)
        shoot = False
        blty = 2*shtry+5
    if not gameOver and missFire == 3:
        balls = []
        missFire = 0
        play = False
        gameOver = True
        print("Game Over!")
        print("Total Score:", score)
        
    
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
    
    global shtrx, shtry, bltx, blty, px, py, bkx, bky, ex, ey, check, idx, shoot, balls

    if not gameOver and shoot:
        circleDraw(bltx, blty, 5)
    circleDraw(shtrx, shtry, 20)
    
    for i in range(len(balls)):
        circleDraw(balls[i][0], balls[i][1], balls[i][2])
    
    drawExit(ex, ey, [1, 0, 0])
    drawBack(bkx, bky, [0, 0, 1])
    drawPausePlay(px, py, [1, 0.7, 0.02])
    
    glutSwapBuffers()
    

def animate():
    #//codes for any changes in Models, Camera
    glutPostRedisplay()
    global play, gameOver, shoot, bltx, blty, shtrx, shtry, balls
    fallingBalls()
    shootingBalls()


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

glutMouseFunc(mouseListener)
glutKeyboardFunc(keyboardListener)

glutMainLoop()		#The main loop of OpenGL