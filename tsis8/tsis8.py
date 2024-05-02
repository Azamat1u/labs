import pygame as py  
import pygame.gfxdraw
from pygame.locals import *
# define constants  
WIDTH = 500  
HEIGHT = 500  
FPS = 30  

# define colors  
BLACK = (0 , 0 , 0)  
GREEN = (0 , 255 , 0) 
WHITE=(255,255,255) 
BLUE = (0,0,255)
RED = (255, 0, 0)
PINK= (255,192,203)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
VIOLET = (177, 3, 252)
pencolour = GREEN
# initialize pygame and create screen  
py.init()  
screen = py.display.set_mode((WIDTH , HEIGHT)) 
#screen.fill(WHITE) 
# for setting FPS  
clock = py.time.Clock()  
clearrect = (100, 0, 500, 500)
col1= (5, 10, 30, 30)
col2= (50, 10, 30, 30)
col3= (5, 50, 30, 30)
col4= (50, 50, 30, 30)
col5= (5, 90, 30, 30)
col6= (50, 90, 30, 30)
col7= (5, 130, 30, 30)
col8= (50, 130, 30, 30)
buttonselect = (5,10,30,30)
def drawrectangle():    
    pygame.gfxdraw.box(screen, col1, BLACK)
    pygame.gfxdraw.box(screen, col2, BLUE)
    pygame.gfxdraw.box(screen, col3, RED)
    pygame.gfxdraw.box(screen, col4, GREEN)
    pygame.gfxdraw.box(screen, col5, PINK)
    pygame.gfxdraw.box(screen, col6, ORANGE)
    pygame.gfxdraw.box(screen, col7, YELLOW)
    pygame.gfxdraw.box(screen, col8, VIOLET)
drawrectangle()
trnsp=255
rot = 0  
rot_speed = 2  
sc=0
scaler=2
# define a surface (RECTANGLE)  
surf = py.Surface((100 , 100))  
# for making transparent background while rotating an image  
surf.set_colorkey(BLACK)  
# fill the rectangle / surface with green color  
surf.fill(GREEN)  
# creating a copy of orignal image for smooth rotation  
image = surf.copy()  
image.set_colorkey(BLACK)  
# define rect for placing the rectangle at the desired position  
rect = image.get_rect()  
rect.center = (WIDTH // 2 , HEIGHT // 2)  
# keep rotating the rectangle until running is set to False  
running = True  
while running:
    # set FPS  
    clock.tick(FPS)  
    # clear the screen every time before drawing new objects  
    screen.fill(WHITE) 
    drawrectangle() 
    # making a copy of the old center of the rectangle  
    old_center = rect.center
    # check for the exit  
    for event in py.event.get():  
        if event.type == py.QUIT:  
            running = False  
    t = pygame.mouse.get_pressed()
    if t[0] == 1:     
        mousepos = pygame.mouse.get_pos()
            # for drawing on display
            # if 122 < mousepos[0] < 678 and 21 < mousepos[1] < 480:
            #     pygame.gfxdraw.filled_ellipse(drawingwindow,mousepos[0], mousepos[1],4,4,pencolour)
        if 200 < mousepos[0] < 300 and 200 < mousepos[1] < 300:
            surf.fill(pencolour)

        elif 5 < mousepos[0] < 35 and 10 < mousepos[1] < 40:
            pencolour = BLACK
            drawrectangle()         
            buttonselect = (5, 10, 30, 30)

        elif 50 < mousepos[0] < 80 and 10 < mousepos[1] < 40:
            pencolour = BLUE
            drawrectangle()
            buttonselect = (50, 10, 30, 30)
                
        elif 5 < mousepos[0] < 35 and 50 < mousepos[1] < 80:
            pencolour = RED
            drawrectangle()
            buttonselect = (5,50,30,30)
                
        elif 50 < mousepos[0] < 80 and 50 < mousepos[1] < 80:
            pencolour = GREEN
            drawrectangle()
            buttonselect = (50,50,30,30)
                
        elif 5 < mousepos[0] < 35 and 90 < mousepos[1] < 120:
            pencolour = PINK
            drawrectangle()
            buttonselect = (5,90,30,30)
                
        elif 50 < mousepos[0] < 80 and 90 < mousepos[1] < 120:
            pencolour = ORANGE
            drawrectangle()
            buttonselect = (50,90,30,30)
                
        elif 5 < mousepos[0] < 35 and 130 < mousepos[1] < 160:
            pencolour = YELLOW
            drawrectangle()
            buttonselect = (5,130,30,30)
                
        elif 50 < mousepos[0] < 80 and 130 < mousepos[1] < 160:
            pencolour = VIOLET
            drawrectangle()
            buttonselect = (50,130,30,30)
    pygame.gfxdraw.rectangle(screen, buttonselect, WHITE)  
    keys = py.key.get_pressed()
    if keys[py.K_LEFT]:
        # defining angle of the rotation  
        rot = (rot + rot_speed) % 360
    elif keys[py.K_RIGHT]:
        # defining angle of the rotation  
        rot = (rot - rot_speed) % 360  
    elif keys[py.K_UP]:
        sc=sc+scaler
    elif keys[py.K_DOWN]:
        sc=sc-scaler
        if sc<-100:
            sc=-100
    elif keys[py.K_q]:
        trnsp=trnsp+1
        if trnsp>255:
            trnsp=255
    elif keys[py.K_w]:
        trnsp=trnsp-1
        if trnsp<0:
            trnsp=0
    surf.set_alpha(trnsp)
    # rotating the orignal image  
    zsurf=py.transform.scale(surf,(100+sc,100+sc))
    rsurf = py.transform.rotate(zsurf , rot)  
    rect = rsurf.get_rect()
    # set the rotated rectangle to the old center  
    rect.center = old_center  
    # drawing the rotated rectangle to the screen  
    screen.blit(rsurf , rect)

    
    # flipping the display after drawing everything  
    py.display.flip()  