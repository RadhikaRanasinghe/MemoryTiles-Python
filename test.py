import pygame
import time
import random

pygame.init()

t = 10

score = 0

playTime = False

#win size
display_height = 600
display_width = 600
#creating arrays
X = [0,100,200,300,0,100,200,300,0,100,200,300]
Y = [0,0,0,0,100,100,100,100,200,200,200,200]
#colors
white = (255,255,255)
black = (0,0,0)
    
#load images
cover = pygame.image.load('Cover.jpg')
sponge= pygame.image.load('Image1.jpg')
patrick = pygame.image.load('Image2.jpg')
squid = pygame.image.load('Image3.png')

#scale images
cover = pygame.transform.scale(cover,(100,100))
sponge = pygame.transform.scale(sponge,(100,100))
patrick = pygame.transform.scale(patrick,(100,100))
squid = pygame.transform.scale(squid,(100,100))


order = [sponge,patrick,squid,sponge,patrick,squid,sponge,patrick,squid,sponge,patrick,squid]
random.shuffle(order)
revealed = [True]*12
locked = [True]*12
opened = [False]*12


win = pygame.display.set_mode((display_width,display_height)) #game display

pygame.display.set_caption("Memory Tiles") #game caption
# image click func





#count dowm
def timerDisp():
    TimeLeft = calcTimeLeft(8)
    Font = pygame.font.SysFont('Comin Sans Ms', 32)
    SurfaceTime = Font.render(str(round(TimeLeft,1)), True, black)
    win.blit(SurfaceTime, (500,30))


def calcTimeLeft(seconds):
     global t
     t = seconds - (time.time() - StartTime)
     if(t >= 0 ):
         return t
     else:
         return 0.0

def checkTimeOut():
    return (t<=0)
    
def level2():
    StartTime = time.time()

    run = True
    while run:
        pygame.time.delay(100) #game delay
        win.fill((white))
        timerDisp()#timer
        scoreDisplay()
        for event in pygame.event.get(): #keyboard or mouse events
            if event.type == pygame.QUIT: #event for close button clicked
                run = False
            if (event.type == pygame.MOUSEBUTTONDOWN and playTime): #event for mouse button clicked and checking if playtime ==true
                x,y = pygame.mouse.get_pos()
                Clicked, ImageIndex = ImageClicked(x,y)
                if ImageIndex != None:
                    Check(ImageIndex)
        display_update()

        
        if checkTimeOut():
            if(playTime == False):
                revealed = [False]*12
                locked = [False]*12
                playTime = True
        

        



pygame.quit()
