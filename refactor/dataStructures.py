import random
import time
t = 10

score = 0

playTime = True

#win size
display_height = 600
display_width = 600
#creating arrays
X = [0,100,200,300,0,100,200,300,0,100,200,300]
Y = [0,0,0,0,100,100,100,100,200,200,200,200]
#colors
white = (255,255,255)
black = (0,0,0)


revealed = [False]*12
locked = [False]*12
opened = [False]*12


def ImageClicked(x,y):
    if(x<300 and y<600 ):
        global X
        global Y

        Clicked = False
        for count in range(len(X)):
            if X[count]<x and X[count] + 100 >x:
                if Y[count]<y and Y[count] + 100 >y:
                    if checkIfRevealed(count):#check if the image was clicked before
                        ImageIndex = None
                    else:
                        revealTile(count)
                        Clicked = True
                        ImageIndex = count

        return Clicked, ImageIndex
    else:
        return None, None

def revealTile(index):
    global revealed
    revealed[index] = True

def checkIfRevealed(index):
    global revealed
    return (revealed[index])

#image_1 and image_2 assigning
First = None

def Check(index):
    checkAlreadyChecked(index)
    global opened
    global First
    global score

    opened[index] = True
    print('score',score)
    if First == None:
        First = index 
        hideTempTiles()
    else:
        if order[index] == order[First]:#check if the clicked images are equal
            lockTitle(index)
            lockTitle(First) #lock if the images match
            score+=20

        else:
            # pygame.time.set_timer(pygame.USEREVENT,300)//       
           unrevealTile(index)
           unrevealTile(First)
           showTemporarily(First,index)
        First = None

tempshowtimestart = None
FirstTitle = None
SecondTitle = None 


def showTemporarily(FirstT, SecondT):
    global FirstTitle
    global SecondTitle
    FirstTitle = FirstT
    SecondTitle = SecondT
    global tempshowtimestart
    if(tempshowtimestart == None):
        tempshowtimestart = time.time()
    lockTitle(FirstTitle)
    lockTitle(SecondTitle)

def hideTempTiles():
    print('hide called')
    
    global FirstTitle
    global SecondTitle
    print('F',FirstTitle)
    print('s',SecondTitle)
    if(FirstTitle and SecondTitle):

        unLockTitle(FirstTitle)
        unLockTitle(SecondTitle)
        tempshowtimestart = None
        FirstTitle = None
        SecondTitle = None


def lockTitle(index):
    locked[index] = True

def unLockTitle(index):
    locked[index] = False

def unrevealTile(index):
    revealed[index] = False

def display_update():
    #bliting image
    global revealed
    global locked
    for count in range(len(X)):
         if revealed[count] == True or locked[count] == True:
             win.blit(order[count], (X[count],Y[count]))
         else:
            win.blit(cover, (X[count], Y[count]))
    #update display
    pygame.display.update()
#count dowm

def timerDisp():
    TimeLeft = calcTimeLeft()
    Font = pygame.font.SysFont('Comin Sans Ms', 32)
    SurfaceTime = Font.render(str(round(TimeLeft,1)), True, black)
    win.blit(SurfaceTime, (500,30))

def scoreDisplay():
    global score
    Font = pygame.font.SysFont('Comin Sans Ms', 32)
    SurfaceTime = Font.render(str(score), True, black)
    win.blit(SurfaceTime, (500,60))

def checkAlreadyChecked(index):
    global score
    global opened
    if(opened[index]):
        score-=5


def calcTimeLeft(StartTime):
     global t
     t = 5 - (time.time() - StartTime)
     if(t >= 0 ):
         return t
     else:
         return 0.0

def checkTimeOut():
    return (t<=0)

