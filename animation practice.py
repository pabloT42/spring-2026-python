import pygame

pygame.init()
screen = pygame.display.set_mode((475,350))
clock = pygame.time.Clock()

#spritesheet setup
link = pygame.image.load("spritesheet.png").convert_alpha()

framewidth = 64
frameheight = 64
numframes = 4

rownum = 0

#animation speed
ticker = 0
framenum = 0

#Positions duh
xpos = 175
ypos = 125

xpos1 = 250
ypos1 = 70

xpos2 = 150
ypos2 = 100

xpos3 = 250
ypos3 = 100

xpos4 = 150
ypos4 = 50

xpos5 = 325
ypos5 = 100

#game loop
running = True
while running:
    
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #animation
    ticker += 1

    if ticker % 10 == 0:
        framenum += 1
        
        if framenum >= numframes:
            framenum = 0
            
        
        #render sec
        screen.fill((135,206,235))
        
        screen.blit(link, (xpos, ypos),
                    (framewidth * framenum, rownum * frameheight, framewidth, frameheight))
        
        screen.blit(link, (xpos1, ypos1),
                    (framewidth * framenum, rownum * frameheight, framewidth, frameheight))
        
        screen.blit(link, (xpos2, ypos2),
                    (framewidth * framenum, rownum * frameheight, framewidth, frameheight))
        
        screen.blit(link, (xpos3, ypos3),
                    (framewidth * framenum, rownum * frameheight, framewidth, frameheight))
        
        screen.blit(link, (xpos4, ypos4),
                    (framewidth * framenum, rownum * frameheight, framewidth, frameheight))
        
        screen.blit(link, (xpos5, ypos5),
                    (framewidth * framenum, rownum * frameheight, framewidth, frameheight))
        
    pygame.display.flip()
    clock.tick(60)
