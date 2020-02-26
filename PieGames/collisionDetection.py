import sys, pygame
    
#main program begins
pygame.init()

Xscreen = 800
Yscreen = 600

screen = pygame.display.set_mode((Xscreen,Yscreen))
pygame.display.set_caption("Lightcycle")
tronFont = pygame.font.SysFont("TRON",20)
pygame.mouse.set_visible(1)

red = (255,0,0)
blue = (0,0,255)

p1x = 780
p1y = 10
p1 = [[780],[10]]
p1xList = []
p1yList = []
p1poss = p1x, p1y
pathP1 = 1 #4=up 3=right 2=left 1=down

p2x = 10
p2y = 580
p2 = [[10],[580]]
p2xList = []
p2yList = []
p2poss = p2x, p2y
pathP2 = 8 #8=up 7=right 6=left 5=down

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
screen.fill((255,255,255))
clock = pygame.time.Clock()

def p1wins():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        p1wins = tronFont.render("Player 1 wins!", 4, (0,0,0), (255,255,255))
        p1winsSize = p1wins.get_size()
        screen.blit(p1wins, ((Xscreen/2 - p1winsSize[0]/2), 30))
        escText = tronFont.render("Press ESC to Exit", 4, (0,0,0), (255,255,255))
        escTextSize = escText.get_size()
        screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
        pygame.display.update()
        clock.tick(30)
def p2wins():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    
        p2wins = tronFont.render("Player 2 wins!", 4, (0,0,0), (255,255,255))
        p2winsSize = p2wins.get_size()
        screen.blit(p2wins, ((Xscreen/2 - p2winsSize[0]/2), 30))
        escText = tronFont.render("Press ESC to Exit", 4, (0,0,0), (255,255,255))
        escTextSize = escText.get_size()
        screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
        pygame.display.update()
        clock.tick(30)
while True:      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP and pathP1 != 1:
                pathP1 = 4
            if event.key == pygame.K_RIGHT and pathP1 != 2:
                pathP1 = 3                
            if event.key == pygame.K_LEFT and pathP1 != 3:
                pathP1 = 2
            if event.key == pygame.K_DOWN and pathP1 != 4:
                pathP1 = 1
            if event.key == pygame.K_w and pathP2 != 5:
                pathP2 = 8
            if event.key == pygame.K_d and pathP2 != 6:
                pathP2 = 7
            if event.key == pygame.K_a and pathP2 != 7:
                pathP2 = 6
            if event.key == pygame.K_s and pathP2 != 8:
                pathP2 = 5
    
    if pathP1 == 4:
        p1y -= 3
        if screen.get_at((p1x,p1y-1)) == red:
            p2wins()
    elif pathP1 == 3:
        p1x += 3
        if screen.get_at((p1x+4,p1y)) == red:
            p2wins()
    elif pathP1 == 2:
        p1x -= 3
        if screen.get_at((p1x-1,p1y)) == red:
            p2wins()
    elif pathP1 == 1:
        p1y += 3
        if screen.get_at((p1x,p1y+4)) == red:
            p2wins()

    
    if pathP2 == 8:
        p2y -= 3
        if screen.get_at((p2x,p2y-1)) == blue:
            p1wins()        
    elif pathP2 == 7:
        p2x += 3
        if screen.get_at((p2x+4,p2y)) == blue:
            p1wins()
    elif pathP2 == 6:
        p2x -= 3
        if screen.get_at((p2x-1,p2y)) == blue:
            p1wins()
    elif pathP2 == 5:
        p2y += 3
        if screen.get_at((p2x,p2y+4)) == blue:
            p1wins()
        
    
            
  
    
    posP1 = p1x, p1y, 3, 3
    posP2 = p2x, p2y, 3, 3
    
    pygame.draw.rect(screen, red, posP1, 0)
    pygame.draw.rect(screen, blue, posP2, 0)
    
    p1[0].append(p1x)
    p1[1].append(p1y)
    p1xList.append(p1x)
    p1yList.append(p1y)    

    
    p2[0].append(p2x)
    p2[1].append(p2y)    
    p2xList.append(p2x)
    p2yList.append(p2y)
    
    count = -1
    for i in p2xList:
        count += 1
        if intersectsX(p1x, i, 3, 3) == True and intersectsY(p1y, p2yList[count], 3, 3) == True:
            p2wins()

    count1 = -1
    for q in p1xList:
        count1 += 1
        if intersectsX(p2x, q, 3, 3) == True and intersectsY(p2y, p1yList[count1], 3, 3) == True:
            p1wins()


    

    clock.tick(30)    
    pygame.display.update()
    
