import pygame, sys

pygame.init()
pygame.mixer.init()

Xscreen = 800
Yscreen = 600
windowSize = (Xscreen, Yscreen)

screen = pygame.display.set_mode(windowSize)
pygame.mouse.set_visible(1)

arialFont = pygame.font.SysFont("Arial", 40)
startText = arialFont.render("Press space to start", 4, (0,0,0), (255,255,255))
startTextSize = startText.get_size()
escText = arialFont.render("Press ESC to exit", 4, (0,0,0), (255,255,255))
escTextSize = escText.get_size()
p1 = 0
p1Score = str(p1)
player1Score = arialFont.render(p1Score, 4, (0,0,0), (255,255,255))
player1ScoreSize = player1Score.get_size()
p2 = 0
p2Score = str(p2) 
player2Score = arialFont.render(p2Score, 4, (0,0,0), (255,255,255))
player2ScoreSize = player2Score.get_size()
winScreenP1 = arialFont.render("CPU wins!", 4, (0,0,0),(255,255,255))
winScreenP1size = winScreenP1.get_size()
winScreenP2 = arialFont.render("Player wins!", 4, (0,0,0),(255,255,255))
winScreenP2size = winScreenP2.get_size()
cpuIndicator = arialFont.render("CPU", 2, (0,0,0),(255,255,255))
a, b = 0, 250 #left paddle coordinates
c, d = 780, 250 #right paddle coordinates
e, f = 390,290 #ball coordinates
def intersectsX(x1,x2,w1,w2):
    if x1 >= x2 and x1 < (x2 + w2):
        return True
    if (x1 + w1) > x2 and (x1 + w1) <= (x2 + w2):
        return True
    return False
def intersectsY(y1,y2,h1,h2):
    if y1 >= y2 and y1 <= (y2 + h2):
        return True
    if (y1 + h1) >= y2 and (y1 + h1) <= (y2 + h2):
        return True
    return False
def p1score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("CPU: "+str(count), True, (0,0,0))
    textSize =  text.get_size()
    screen.blit(text,((390 - textSize[0]), 5))
def p2score(count):
    font = pygame.font.SysFont(None, 25)
    text2 = font.render(str(count) + " :P", True, (0,0,0))
    text2Size =  text2.get_size()
    screen.blit(text2,((410 + text2Size[0]), 5))
directionB = 1
directionE = 2
directionF = -1
clock = pygame.time.Clock()
stay1 = True
stay2 = True
while True:
    screen.fill((255,255,255)) 
    screen.blit(cpuIndicator,(0,200))       
    pygame.draw.rect(screen, (0,0,0), (a,b,20,100))
    pygame.draw.rect(screen, (0,0,0), (c,d,20,100))
    pygame.draw.rect(screen,(0,0,0),(e,f,20,20))
    screen.blit(startText, ((Xscreen/2 - startTextSize[0]/2), 10))
    screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), (10 + startTextSize[1])))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:    
                while True:
                    screen.fill((255,255,255))
                    for event in pygame.event.get(): 
                        if event.type == pygame.QUIT:
                            sys.exit()
                    pygame.draw.rect(screen, (0,0,0), (a,b,20,100))
                    pygame.draw.rect(screen, (0,0,0), (c,d,20,100))
                    pygame.draw.rect(screen,(0,0,0),(e,f,20,20))
                    keys = pygame.key.get_pressed()
                    e += 6*directionE
                    f += 6*directionF
                    if b < 0:
                        directionB *= -1
                    if d < 0:
                        d = 0
                    if b + 100 > Yscreen:
                        directionB *= -1
                    if d + 100 > Yscreen:
                        d = Yscreen - 100
                    if e > Xscreen:
                        p1 += 1
                        e,f = 390, 290
                        directionE = -2
                        pygame.display.update()
                    if e + 20 < 0:
                        p2 += 1
                        e,f = 390, 290
                        directionE = 2
                        pygame.display.update()
                    if f < 0 or f + 20 > Yscreen:
                        directionF *= -1
                    if intersectsX(e, a, 20, 20) == True and intersectsY(f, b, 20, 100) == True:
                        directionE *= -1
                    if intersectsX(e, c, 20, 20) == True and intersectsY(f, d, 20, 100) == True:
                        directionE *= -1
                    if keys[pygame.K_UP]:
                        d -= 8
                    if keys[pygame.K_DOWN]:
                        d += 8
                    b += 8*directionB
                    if p1 == 10:
                        a, b = 0, 250 #left paddle coordinates
                        c, d = 780, 250 #right paddle coordinates
                        p1 = 0
                        p2 = 0 
                        while True:
                            for event in pygame.event.get(): 
                                if event.type == pygame.QUIT:
                                    sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        stay1 = False
                            if stay1 == False:
                                break
                            screen.fill((255,255,255))
                            screen.blit(winScreenP1, ((400 - winScreenP1size[0]/2),300))
                            screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 400))
                            pygame.display.update()
                            clock.tick(30)
                        break
                    if p2 == 10:
                        a, b = 0, 250 #left paddle coordinates
                        c, d = 780, 250 #right paddle coordinates
                        p1 = 0
                        p2 = 0
                        while True:
                            for event in pygame.event.get(): 
                                if event.type == pygame.QUIT:
                                    sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        stay2 = False
                            if stay2 == False:
                                break
                            screen.fill((255,255,255))
                            screen.blit(winScreenP2, ((400 - winScreenP2size[0]/2),300))
                            screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 400))
                            pygame.display.update()
                            clock.tick(30)                            
                        break
                    p1score(p1)
                    p2score(p2)
                    pygame.display.update()
                    clock.tick(30)
    pygame.display.update()
    clock.tick(30)
    


