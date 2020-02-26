import pygame, sys #imports necessary modules

pygame.init() #initializes pygame

Xscreen = 800 #sets display
Yscreen = 600
windowSize = (Xscreen, Yscreen)

screen = pygame.display.set_mode(windowSize)
pygame.mouse.set_visible(1) #makes mouse visible

kArcadeFont = pygame.font.SysFont("Karmatic Arcade", 40) #creates shortcut for font to be used later
welcomeText = kArcadeFont.render("Welcome to Pie Games", 4, (0,0,0), (255,255,255)) #creates text objects to be used by screen.blit
welcomeTextSize = welcomeText.get_size() #finds size of text objects for optimal placement

pongOption = kArcadeFont.render("Pong", 1,(0,0,0),(255,255,255))
pongOptionSize = pongOption.get_size()

#testVal
print("workings")

lightCycleOption = kArcadeFont.render("Light Cycle",1,(0,0,0), (255,255,255))
lightCycleOptionSize = lightCycleOption.get_size()

pong1P = kArcadeFont.render("1 Player", 1, (0,0,0),(255,255,255))
pong1Psize = pong1P.get_size()
pong2P = kArcadeFont.render("2 Player", 1, (0,0,0),(255,255,255))
pong2Psize = pong2P.get_size()

pongExitOption = kArcadeFont.render("Exit", 1, (0,0,0),(255,255,255))
pEOsize = pongExitOption.get_size()



x, y = 0, 0 #sets coordinates for mouse
clock = pygame.time.Clock()

def intersectsX(x1,x2,w1,w2): #function used to check for collisions
    if x1 >= x2 and x1 < (x2 + w2): #checks if x (which is the mouse) is within the boundaries of a second object (x2)
        return True
    if (x1 + w1) > x2 and (x1 + w1) <= (x2 + w2): #checks if x's boundaries are within boundaries of second object (x2)
        return True
    return False
def intersectsY(y1,y2,h1,h2): #similar function as above, but for y coordinates
    if y1 >= y2 and y1 <= (y2 + h2):
        return True
    if (y1 + h1) >= y2 and (y1 + h1) <= (y2 + h2):
        return True
    return False

while True: #grandfather loop (encompasses entirety of game
    playerSelectExit = False #switch that turns on if player selects exits during screen where they select how many people are playing

    screen.fill((255,255,255)) #fills screen with white
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if quit button (Red X in corner) is selected, closes pygame window
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: #checks for events involving pressing mouse button
            if x > (Xscreen/2 - pongOptionSize[0]/2) and x < (Xscreen/2 - pongOptionSize[0]/2) + pongOptionSize[0]: #if x is within boundaries of Pong word
                if y > 200 and y < 200 + pongOptionSize[1]: #if y is within boundaries of Pong word
                    while True: #loop that is entered if it meets above conditions. this loop encompasses entirety of pong game
                        screen.fill((255,255,255))
                        pongStartScreenExit = False #switch that flips if player presses ESC in start screen after selecting player#
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if x > (Xscreen/2 - pong1Psize[0]/2) and x < (Xscreen/2 - pong1Psize[0]/2) + pong1Psize[0]: #if mouse is in boundaries of 1 player option
                                    if y > 250 and y < 250 + pong1Psize[1]:
                                        startText = kArcadeFont.render("Press space to start", 4, (0,0,0), (255,255,255)) #creates text for pong start screen
                                        startTextSize = startText.get_size()
                                        escText = kArcadeFont.render("Press ESC to exit", 4, (0,0,0), (255,255,255))
                                        escTextSize = escText.get_size()
                                        p1 = 0 #score for player 1
                                        p2 = 0 #score for player 2
                                        winScreenP1 = kArcadeFont.render("CPU wins!", 4, (0,0,0),(255,255,255)) #Text displayed if CPU wins
                                        winScreenP1size = winScreenP1.get_size()
                                        winScreenP2 = kArcadeFont.render("Player wins!", 4, (0,0,0),(255,255,255)) #Text displayed if Player wins
                                        winScreenP2size = winScreenP2.get_size()
                                        cpuIndicator = kArcadeFont.render("CPU", 2, (0,0,0),(255,255,255)) #Text to show which side is CPU
                                        a, b = 0, 250 #left paddle coordinates
                                        c, d = 780, 250 #right paddle coordinates
                                        e, f = 390,290 #ball coordinates
                                        def p1score(count): #function for displaying score. count is a parameter that will be occupied by the score values
                                            font = pygame.font.SysFont(None, 25)
                                            text = font.render("CPU: "+str(count), True, (0,0,0)) #creates text that displays str of count
                                            textSize =  text.get_size()
                                            screen.blit(text,((390 - textSize[0]), 5)) #displays text
                                        def p2score(count): #function similar to one above, for p2.
                                            font = pygame.font.SysFont(None, 25)
                                            text2 = font.render(str(count) + " :P", True, (0,0,0))
                                            text2Size =  text2.get_size()
                                            screen.blit(text2,((410 + text2Size[0]), 5))
                                        directionB = 1 #direction for left paddle on Y-Axis. will determine how CPU operates
                                        directionE = 2 #direction for ball on x-axis
                                        directionF = -1 #direction for ball on y-axis. the values of these directions will change as ball bounces
                                        clock = pygame.time.Clock()
                                        stay1 = True #switch that flips if escape is pressed while in win screen
                                        stay2 = True #similar switch, but for win screen of other player
                                        while True: #loop for 1 player Pong start screen
                                            screen.fill((255,255,255))
                                            if pongStartScreenExit == True: #once switch is flipped (see below), start screen loop is broken, returns to previous screen
                                                break
                                            screen.blit(cpuIndicator,(0,200))  #creates text object on screen above paddle
                                            pygame.draw.rect(screen, (0,0,0), (a,b,20,100)) #draws left paddle
                                            pygame.draw.rect(screen, (0,0,0), (c,d,20,100)) #draws right paddle
                                            pygame.draw.rect(screen,(0,0,0),(e,f,20,20)) #draws ball
                                            screen.blit(startText, ((Xscreen/2 - startTextSize[0]/2), 10))
                                            screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), (10 + startTextSize[1])))
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    sys.exit()
                                                if event.type == pygame.KEYDOWN:
                                                    if event.key == pygame.K_ESCAPE: #if escape is pressed in start screen, flips switch (see above)
                                                        pongStartScreenExit = True
                                                    if event.key == pygame.K_SPACE:#if space is pressed:
                                                        while True: #enters loop for actual game of 1 player pong
                                                            screen.fill((255,255,255))
                                                            for event in pygame.event.get():
                                                                if event.type == pygame.QUIT:
                                                                    sys.exit()
                                                            pygame.draw.rect(screen, (0,0,0), (a,b,20,100)) #redraws objects for game since screen has been filled again
                                                            pygame.draw.rect(screen, (0,0,0), (c,d,20,100))
                                                            pygame.draw.rect(screen,(0,0,0),(e,f,20,20))
                                                            keys = pygame.key.get_pressed()
                                                            e += 6*directionE #animates ball. changes coordinates six pixels at a time, based on direction
                                                            f += 6*directionF
                                                            if b < 0:
                                                                directionB *= -1 #bounces CPU paddle off top of screen
                                                            if d < 0: #doesn't allow player to go off screen
                                                                d = 0
                                                            if b + 100 > Yscreen: #bounces CPU paddle off bottom of screen
                                                                directionB *= -1
                                                            if d + 100 > Yscreen: #boundaries for player cont.
                                                                d = Yscreen - 100
                                                            if e + 20 > Xscreen: #if ball passes right side:
                                                                p1 += 1 #cpu gets the point
                                                                e,f = 390, 290 #ball reset to center
                                                                directionE = -2 #ball begins by traveling to left
                                                            if e < 0: #if ball passes left side:
                                                                p2 += 1 #player gets a point
                                                                e,f = 390, 290 #resets ball
                                                                directionE = 2 #ball begins by traveling to right

                                                            if f < 0 or f + 20 > Yscreen: #changes direction of ball on y-axis if it touches bottom or top of screen
                                                                directionF *= -1
                                                            if intersectsX(e, a, 20, 20) == True and intersectsY(f, b, 20, 100) == True: #checks if ball is colliding with left paddle
                                                                directionE *= -1 #if it collides, direction flipped
                                                            if intersectsX(e, c, 20, 20) == True and intersectsY(f, d, 20, 100) == True: #checks if ball is colliding with right paddle
                                                                directionE *= -1 #if it collides, direction flipped
                                                            if keys[pygame.K_UP]: #if up arrow is held down on keyboard, right paddle moves up 8 pixels at a time
                                                                d -= 8
                                                            if keys[pygame.K_DOWN]: #if down arrow is held down on keyboard, right paddle moves down 8 pixels at a time
                                                                d += 8
                                                            b += 8*directionB #animates right paddle (CPU)
                                                            if p1 == 10: #if CPU scores 10 points:
                                                                a, b = 0, 250 #left paddle coordinates
                                                                c, d = 780, 250 #right paddle coordinates. paddles are reset
                                                                p1 = 0
                                                                p2 = 0 #score reset
                                                                while True: #enters a loop that displays a new screen
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            sys.exit()
                                                                        if event.type == pygame.KEYDOWN:
                                                                            if event.key == pygame.K_ESCAPE: #if escape is pressed, flips switch
                                                                                stay1 = False
                                                                    if stay1 == False: #once switch is flipped, breaks loop for the current screen
                                                                        break
                                                                    screen.fill((255,255,255))
                                                                    screen.blit(winScreenP1, ((400 - winScreenP1size[0]/2),300)) #displays appropriate text
                                                                    screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 400))
                                                                    pygame.display.update()
                                                                    clock.tick(30)
                                                                break #if loop above is broken, breaks this loop to return to start screen
                                                            if p2 == 10: #same as above for p1, but for p2 in this case
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

                                if x > (Xscreen/2 - pong2Psize[0]/2) and x < (Xscreen/2 - pong2Psize[0]/2) + pong2Psize[0]: #same concept as 1 player pong. changes to code from above will be indicated.
                                    if y > 300 and y < 300 + pong2Psize[1]:
                                        kArcadeFont = pygame.font.SysFont("Karmatic Arcade", 40)
                                        startText = kArcadeFont.render("Press space to start", 4, (0,0,0), (255,255,255))
                                        startTextSize = startText.get_size()
                                        escText = kArcadeFont.render("Press ESC to exit", 4, (0,0,0), (255,255,255))
                                        escTextSize = escText.get_size()
                                        p1 = 0
                                        p2 = 0
                                        winScreenP1 = kArcadeFont.render("Player 1 wins!", 4, (0,0,0),(255,255,255))
                                        winScreenP1size = winScreenP1.get_size()
                                        winScreenP2 = kArcadeFont.render("Player 2 wins!", 4, (0,0,0),(255,255,255))
                                        winScreenP2size = winScreenP2.get_size()
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
                                            text = font.render("P1: "+str(count), True, (0,0,0))
                                            textSize =  text.get_size()
                                            screen.blit(text,((390 - textSize[0]), 5))
                                        def p2score(count):
                                            font = pygame.font.SysFont(None, 25)
                                            text2 = font.render(str(count) + " :P2", True, (0,0,0))
                                            text2Size =  text2.get_size()
                                            screen.blit(text2,((410 + text2Size[0]), 5))
                                        directionE = 2
                                        directionF = -1
                                        clock = pygame.time.Clock()
                                        stay1 = True
                                        stay2 = True
                                        while True:
                                            screen.fill((255,255,255))
                                            if pongStartScreenExit == True:
                                                break
                                            pygame.draw.rect(screen, (0,0,0), (a,b,20,100))
                                            pygame.draw.rect(screen, (0,0,0), (c,d,20,100))
                                            pygame.draw.rect(screen,(0,0,0),(e,f,20,20))
                                            screen.blit(startText, ((Xscreen/2 - startTextSize[0]/2), 10))
                                            screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), (10 + startTextSize[1])))
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    sys.exit()
                                                if event.type == pygame.KEYDOWN:
                                                    if event.key == pygame.K_ESCAPE:
                                                        pongStartScreenExit = True
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
                                                            if b < 0: #now if left paddle touches top or bottom of screen (few lines below), stops it from moving rather than bouncing it.
                                                                b = 0
                                                            if d < 0:
                                                                d = 0
                                                            if b + 100 > Yscreen:
                                                                b = Yscreen - 100
                                                            if d + 100 > Yscreen:
                                                                d = Yscreen - 100
                                                            if e + 20> Xscreen:
                                                                p1 += 1
                                                                e,f = 390, 290
                                                                directionE = -2
                                                                pygame.display.update()
                                                            if e < 0:
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
                                                            if keys[pygame.K_w]: #if w is pressed by second player, moves left paddle up 8 pixels at a time.
                                                                b -= 8
                                                            if keys[pygame.K_s]: #if s is pressed by second player, moves left paddle down 8 pixels at a time.
                                                                b += 8
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
                                                            p1score(p1) #applies the function, using the scores of both players as the count parameter
                                                            p2score(p2)
                                                            pygame.display.update()
                                                            clock.tick(30)
                                            pygame.display.update()
                                            clock.tick(30)
                                if x > (Xscreen/2 - pEOsize[0]/2) and x < (Xscreen/2 - pEOsize[0]/2) + pEOsize[0]:
                                    if y > 350 and y < 350 + pEOsize[1]:
                                        playerSelectExit = True  #flips switch is "exit" is selected
                        screen.blit(pong1P,((Xscreen/2 - pong1Psize[0]/2), 250))
                        screen.blit(pong2P,((Xscreen/2 - pong2Psize[0]/2), 300))
                        screen.blit(pongExitOption, ((Xscreen/2 - pEOsize[0]/2), 350))
                        mousePosition = pygame.mouse.get_pos()
                        x = mousePosition[0]
                        y = mousePosition[1]
                        if playerSelectExit == True:
                            break #breaks pong loop if exit is selected
                        pygame.display.update()
                        clock.tick(30)
            if x > (Xscreen/2 - lightCycleOptionSize[0]/2) and x < (Xscreen/2 - lightCycleOptionSize[0]/2) + lightCycleOptionSize[0]: #if mouse is pressed while within boundaries of light cycle text:
                if y > 275 and y < 275 + lightCycleOptionSize[1]:
                    red = (255,0,0)#Setting colors to use easily
                    blue = (0,0,255)

                    tronFont = pygame.font.SysFont("TRON", 40) #Creating a shortcut to use when making text
                    startText = tronFont.render("Press Space to start", 4, (0,0,0),(255,255,255))#text displayed during main screen
                    startTextSize = startText.get_size()#size of text to get proper placement when using screen.blit
                    escText = tronFont.render("Press ESC to Exit", 4, (0,0,0),(255,255,255))
                    escTextSize = escText.get_size()

                    clock = pygame.time.Clock()
                    mainScreenExit = False #switch that turns on if player presses ESC during lightcycle main screen
                    while True: #main game loop
                        winScreenExit = False #a switch that flips when ESC is pressed. if switch is on true, will break the game loop within main loop
                        collisionExit = False #a swtich that flips when entering win screen from loop that checks for collision
                        if mainScreenExit == True:
                            break
                        for event in pygame.event.get(): #for keyboard events
                            if event.type == pygame.QUIT:
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE: #another switch that flips if escape is pressed while in main menu
                                    mainScreenExit = True
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
                                        if p1x + 3 > Xscreen or p1x == 3 or p1y + 3 > Yscreen or p1y == 1: #boundary limits for player 1
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
                                        if p2x + 3 > Xscreen or p2x == 1 or p2y + 3 > Yscreen or p2y == 1: #boundary limits for player 2
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
                                            if screen.get_at((p1x,p1y)) == red: #checks for self collision by seeing if the pixel is the same color as the tail of the cycle.
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
                        screen.fill((255,255,255))
                        screen.blit(startText, ((Xscreen/2 - startTextSize[0]/2), 50)) #adds the text created above to main screen
                        screen.blit(escText, ((Xscreen/2 - escTextSize[0]/2), 120))
                        pygame.display.update()
                        clock.tick(30)
    pongIntHoverX = intersectsX(x,350,0,pongOptionSize[0]) #a value of either True or False based on return from function
    pongIntHoverY = intersectsY(y, 200, 0, pongOptionSize[1])
    if pongIntHoverX == True and pongIntHoverY == True: #using function to see if mouse within boundaries of pong text, rather than 2 conditional statements for when mouse button is pressed
        pygame.draw.rect(screen, (0,0,0), ((Xscreen/2 - pongOptionSize[0]/2)-1, 199,(pongOptionSize[0] + 2),(pongOptionSize[1] + 2)))
        screen.blit(pongOption, ((Xscreen/2 - pongOptionSize[0]/2), 200)) #draws a rectangle around pong text to show it is being hovered on
    if intersectsX(x, 300, 0, lightCycleOptionSize[0]) == True and intersectsY(y, 275, 0, lightCycleOptionSize[1]) == True: #uses function to see if mouse is within boundaries of light cycle text
        pygame.draw.rect(screen, (0,0,0), ((Xscreen/2 - lightCycleOptionSize[0]/2)-1, 274,(lightCycleOptionSize[0] + 2),(lightCycleOptionSize[1] + 2)))
        screen.blit(lightCycleOption, ((Xscreen/2 - lightCycleOptionSize[0]/2), 275))    #draws a rectangle around light cycle text to show it is being hovered on
    screen.blit(welcomeText,((Xscreen/2 - welcomeTextSize[0]/2),100)) #draws appropriate text
    screen.blit(pongOption, ((Xscreen/2 - pongOptionSize[0]/2), 200))
    screen.blit(lightCycleOption, ((Xscreen/2 - lightCycleOptionSize[0]/2), 275))
    mousePosition = pygame.mouse.get_pos() #gets the coordinates of the mouse.
    x = mousePosition[0] #sets x value to x coordinate of mouse.
    y = mousePosition[1] #sets y value to y coordinate of mouse.
    pygame.display.update()
    clock.tick(30)
