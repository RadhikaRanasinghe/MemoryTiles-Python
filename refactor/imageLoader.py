import random

def loadImages(pygame):
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

    return makeOrder(sponge,patrick,squid)

def makeOrder(sponge,patrick,squid):
    order = [sponge,patrick,squid,sponge,patrick,squid,sponge,patrick,squid,sponge,patrick,squid]
    random.shuffle(order)
    return order