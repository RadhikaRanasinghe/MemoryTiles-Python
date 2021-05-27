import pygame
import time
import random
from dataStructures import *
from imageLoader import *

pygame.init()


# def level1():
#     playTime = True
#     t = 60
    
# def level2():
#     playTime = False
#     t = 8

def main():
    win = pygame.display.set_mode((display_width,display_height)) #game display
    pygame.display.set_caption("Memory Tiles") #game caption

    StartTime = time.time()

    order = loadImages(pygame)

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
        playTime = False
        win.fill((0,0,0))
        pygame.display.flip()

