import pygame, sys

pygame.init()

Xscreen = 800
Yscreen = 600
windowSize = (Xscreen, Yscreen) #Hard Coding display

screen = pygame.display.set_mode(windowSize)
pygame.mouse.set_visible(1)#Making mouse visible

red = (255,0,0)#Setting colors to use easily
blue = (0,0,255)

tronFont = pygame.font.SysFont("TRON", 40) #Creating a shortcut to use when making text
startText = tronFont.render("Press Space to start", 4, (0,0,0),(255,255,255))#text displayed during main screen
startTextSize = startText.get_size()#size of text to get proper placement when using screen.blit
escText = tronFont.render("Press ESC to Exit", 4, (0,0,0),(255,255,255))
escTextSize = escText.get_size()

clock = pygame.time.Clock()

def intersectsX(x1,x2,w1,w2): #function used to check for intersections
    if x1 >= x2 and x1 < (x2 + w2):
        return True
    if (x1 + w1) > x2 and (x1 + w1) <= (x2 + w2):
        return True
    return False
def intersectsY(y1,y2,h1,h2): #similar to function above, but for y coordinates
    if y1 >= y2 and y1 <= (y2 + h2):
        return True
    if (y1 + h1) >= y2 and (y1 + h1) <= (y2 + h2):
        return True
    return False
while True: #main game loop
    winScreenExit = False #a switch that flips when ESC is pressed. if switch is on true, will break the game loop within main loop
    collisionExit = False #a swtich that flips when entering win screen from loop that checks for collision
    #if mainScreenExit == True:
        #break
    for event in pygame.event.get(): #for keyboard events
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:#if space is pressed, launches actual game
                p1x = 780 #setting coordinates for player 1
                p1y = 10
                p1xList = [] #list that compiles all x coordinates taken up by player 1
                p1yList = [] #similar to above list, but for y coordinates
                pathP1 = 1 #4=up 3=right 2=left 1=down
                
                p2x = 10 #see comments for player 1
                p2y = 580
                p2xList = []
                p2yList = []
                pathP2 = 8 #8=up 7=right 6=left 5=down
                
                screen.fill((255,255,255)) #fills screen
                clock = pygame.time.Clock()
                
                while True: #game loop for actual game
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP and pathP1 != 1: #changes values of path1 or path2 based on keyboard events
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
                    if p1x + 3 > Xscreen or p1x < 0 or p1y + 3 > Yscreen or p1y< 0: #boundary limits for player 1
                        while True: #loop that system enters if PLAYER 2 wins. was originally a function but use of function raised some complications.
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key ==  pygame.K_ESCAPE: #switches flip when ESC is pressed
                                        winScreenExit = True
                            if winScreenExit == True: #once switch is TRUE, leaves loop with player 2 win screen
                                break
                            p2wins = tronFont.render("Player 2 wins!", 4, (0,0,0), (255,255,255))
                            p2winsSize = p2wins.get_size()
                            screen.blit(p2wins, ((Xscreen/2 - p2winsSize[0]/2), 30))
                            escText = tronFont.render("Press ESC to Exit", 4, (0,0,0), (255,255,255))
                            escTextSize = escText.get_size()
                            screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
                            pygame.display.update()
                            clock.tick(30)
                        break #once loop above is broken, breaks current loop, returning to main screen
                    if p2x + 3 > Xscreen or p2x < 0 or p2y + 3 > Yscreen or p2y< 0: #boundary limits for player 2
                        while True: #similar loop for when PLAYER 1 wins. also used to be a function
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        winScreenExit = True
                            if winScreenExit == True:
                                break
                            p1wins = tronFont.render("Player 1 wins!", 4, (0,0,0), (255,255,255))
                            p1winsSize = p1wins.get_size()
                            screen.blit(p1wins, ((Xscreen/2 - p1winsSize[0]/2), 30))
                            escText = tronFont.render("Press ESC to Exit", 4, (0,0,0), (255,255,255))
                            escTextSize = escText.get_size()
                            screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
                            pygame.display.update()
                            clock.tick(30)
                        break
                    
                    if pathP1 == 4: #actions system takes based on value of path1 or path2. 
                        p1y -= 3 #each numerical value represents a different direction the player goes in. i.e: if pathp1 is 4, player 1 will go UP
                        if screen.get_at((p1x,p1y)) == red:
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key ==  pygame.K_ESCAPE:
                                            winScreenExit = True
                                if winScreenExit == True:
                                    break
                                p2wins = tronFont.render("Player 2 wins!", 4, (0,0,0), (255,255,255))
                                p2winsSize = p2wins.get_size()
                                screen.blit(p2wins, ((Xscreen/2 - p2winsSize[0]/2), 30))
                                escText = tronFont.render("Press ESC to Exit", 4, (0,0,0), (255,255,255))
                                escTextSize = escText.get_size()
                                screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
                                pygame.display.update()
                                clock.tick(30)
                            break
                    elif pathP1 == 3:
                        p1x += 3
                        if screen.get_at((p1x,p1y)) == red:
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key ==  pygame.K_ESCAPE:
                                            winScreenExit = True
                                if winScreenExit == True:
                                    break
                                p2wins = tronFont.render("Player 2 wins!", 4, (0,0,0), (255,255,255))
                                p2winsSize = p2wins.get_size()
                                screen.blit(p2wins, ((Xscreen/2 - p2winsSize[0]/2), 30))
                                escText = tronFont.render("Press ESC to Exit", 4, (0,0,0), (255,255,255))
                                escTextSize = escText.get_size()
                                screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
                                pygame.display.update()
                                clock.tick(30)
                            break
                    elif pathP1 == 2:
                        p1x -= 3
                        if screen.get_at((p1x,p1y)) == red:
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key ==  pygame.K_ESCAPE:
                                            winScreenExit = True
                                if winScreenExit == True:
                                    break
                                p2wins = tronFont.render("Player 2 wins!", 4, (0,0,0), (255,255,255))
                                p2winsSize = p2wins.get_size()
                                screen.blit(p2wins, ((Xscreen/2 - p2winsSize[0]/2), 30))
                                escText = tronFont.render("Press ESC to Exit", 4, (0,0,0), (255,255,255))
                                escTextSize = escText.get_size()
                                screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
                                pygame.display.update()
                                clock.tick(30)
                            break
                    elif pathP1 == 1:
                        p1y += 3
                        if screen.get_at((p1x,p1y)) == red:
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key ==  pygame.K_ESCAPE:
                                            winScreenExit = True
                                if winScreenExit == True:
                                    break
                                p2wins = tronFont.render("Player 2 wins!", 4, (0,0,0), (255,255,255))
                                p2winsSize = p2wins.get_size()
                                screen.blit(p2wins, ((Xscreen/2 - p2winsSize[0]/2), 30))
                                escText = tronFont.render("Press ESC to Exit", 4, (0,0,0), (255,255,255))
                                escTextSize = escText.get_size()
                                screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
                                pygame.display.update()
                                clock.tick(30)
                            break
                
                    
                    if pathP2 == 8: #similar concept as pathP1, but for player 2 and with different values
                        p2y -= 3
                        if screen.get_at((p2x,p2y)) == blue:
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            winScreenExit = True
                                if winScreenExit == True:
                                    break
                                p1wins = tronFont.render("Player 1 wins!", 4, (0,0,0), (255,255,255))
                                p1winsSize = p1wins.get_size()
                                screen.blit(p1wins, ((Xscreen/2 - p1winsSize[0]/2), 30))
                                escText = tronFont.render("Press ESC to Exit", 4, (0,0,0), (255,255,255))
                                escTextSize = escText.get_size()
                                screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
                                pygame.display.update()
                                clock.tick(30)
                            break        
                    elif pathP2 == 7:
                        p2x += 3
                        if screen.get_at((p2x,p2y)) == blue:
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            winScreenExit = True
                                if winScreenExit == True:
                                    break
                                p1wins = tronFont.render("Player 1 wins!", 4, (0,0,0), (255,255,255))
                                p1winsSize = p1wins.get_size()
                                screen.blit(p1wins, ((Xscreen/2 - p1winsSize[0]/2), 30))
                                escText = tronFont.render("Press ESC to Exit", 4, (0,0,0), (255,255,255))
                                escTextSize = escText.get_size()
                                screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
                                pygame.display.update()
                                clock.tick(30)
                            break
                    elif pathP2 == 6:
                        p2x -= 3
                        if screen.get_at((p2x,p2y)) == blue:
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            winScreenExit = True
                                if winScreenExit == True:
                                    break
                                p1wins = tronFont.render("Player 1 wins!", 4, (0,0,0), (255,255,255))
                                p1winsSize = p1wins.get_size()
                                screen.blit(p1wins, ((Xscreen/2 - p1winsSize[0]/2), 30))
                                escText = tronFont.render("Press ESC to Exit", 4, (0,0,0), (255,255,255))
                                escTextSize = escText.get_size()
                                screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
                                pygame.display.update()
                                clock.tick(30)
                            break
                    elif pathP2 == 5:
                        p2y += 3
                        if screen.get_at((p2x,p2y)) == blue:
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            winScreenExit = True
                                if winScreenExit == True:
                                    break
                                p1wins = tronFont.render("Player 1 wins!", 4, (0,0,0), (255,255,255))
                                p1winsSize = p1wins.get_size()
                                screen.blit(p1wins, ((Xscreen/2 - p1winsSize[0]/2), 30))
                                escText = tronFont.render("Press ESC to Exit", 4, (0,0,0), (255,255,255))
                                escTextSize = escText.get_size()
                                screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
                                pygame.display.update()
                                clock.tick(30)
                            break

                    posP1 = p1x, p1y, 3, 3 #value used as a parameter for draw.rect module. allows system to draw rectangle with new coordinate continuously
                    posP2 = p2x, p2y, 3, 3
                    
                    pygame.draw.rect(screen, red, posP1, 0) #draws the actual rectangle
                    pygame.draw.rect(screen, blue, posP2, 0)
                    
                    p1xList.append(p1x) #adds the new x coordinate to the list created above
                    p1yList.append(p1y)    
                
                    p2xList.append(p2x)
                    p2yList.append(p2y)
                    
                    #COLLISION DETECTION SYSTEM: (only for colliding with each other)
                    count = -1 #a counter used as an index value in the collision system
                    for i in p2xList: #for every value in list of X coordinates occupied by a rectangle
                        count += 1 #increased count by 1 so that it can be used as a matching index value when applied to the list of Y coordinates
                        if intersectsX(p1x, i, 3, 3) == True and intersectsY(p1y, p2yList[count], 3, 3) == True: #checks if both collision functions returns true
                            while True: #displays respective win screen
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key ==  pygame.K_ESCAPE:
                                            winScreenExit = True
                                if winScreenExit == True:
                                    break
                                collisionExit = True
                                p2wins = tronFont.render("Player 2 wins!", 4, (0,0,0), (255,255,255))
                                p2winsSize = p2wins.get_size()
                                screen.blit(p2wins, ((Xscreen/2 - p2winsSize[0]/2), 30))
                                escText = tronFont.render("Press ESC to Exit", 4, (0,0,0), (255,255,255))
                                escTextSize = escText.get_size()
                                screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
                                pygame.display.update()
                                clock.tick(30)
                            break
                    if collisionExit == True:
                            break
                
                    count1 = -1 #similar system as above for other player
                    for q in p1xList:
                        count1 += 1
                        if intersectsX(p2x, q, 3, 3) == True and intersectsY(p2y, p1yList[count1], 3, 3) == True:
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            winScreenExit = True
                                if winScreenExit == True:
                                    break
                                collisionExit = True
                                p1wins = tronFont.render("Player 1 wins!", 4, (0,0,0), (255,255,255))
                                p1winsSize = p1wins.get_size()
                                screen.blit(p1wins, ((Xscreen/2 - p1winsSize[0]/2), 30))
                                escText = tronFont.render("Press ESC to Exit", 4, (0,0,0), (255,255,255))
                                escTextSize = escText.get_size()
                                screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
                                pygame.display.update()
                                clock.tick(30)
                            break
                    if collisionExit == True:
                        break
                    clock.tick(30)    
                    pygame.display.update()
            if event.key == pygame.K_ESCAPE: #another switch that flips if escape is pressed while in main menu
                mainScreenExit = True
    screen.fill((255,255,255)) 
    screen.blit(startText, ((Xscreen/2 - startTextSize[0]/2), 50)) #adds the text created above to main screen
    screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
    pygame.display.update()
    clock.tick(30)