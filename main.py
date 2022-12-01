import pygame
from pygame.locals import *
import sys
import settings
from Map import Map
from Player import Player
from Arrow import Arrow
from random import randint
from Enemy import Enemy
import tileImages
from Stars import Stars
from Planets import Planets
from ShootingStars import ShootingStars

def main():
    
    #SETUP
    pygame.init() 
    settings.init()
    screen = pygame.display.set_mode([1440, 870])
    tileImages.init()
    #             w,a,s,d
    incDec = True
    planetImgs = ['Planet1.png', 'Planet2.png', 'Planet3.png', 'Planet4.png', 'Planet5.png']
    c3 = 30
    keyPressed = [0,0,0,0,0]
    #map = Map("map.txt")
    
    #b1 = Bat()
    #print(map)
    #DRAW STUFF
    running = True
    
    #wall = pygame.image.load('wall1.png').convert()
    a = 0
    b = 0
    mapList = ('map9.txt', 'babymap.txt', 'map1.txt', 'map2.txt', 'map.txt', 'map3.txt', 'map4.txt', 'map5.txt', 'map6.txt', 'map7.txt', 'map8.txt', 'map9.txt')
    mapInd = 0
    
    map = Map(mapList[mapInd])
    winning = False
    p = Player(map)
    FPS = 60
    fpsClock = pygame.time.Clock()
    pos = [0, 0]
    arrows = []
    xOff, yOff = 0, 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    MousePressed = False
    t = 0
    getTicksLastFrame = 0
    # I need a function in Map that finds all of a specific tile type (ie. enemy tiles)
    # the function then reads all of these tiles and outputs their locations in a list of lists
    
    #print(enemyPos)
    stars, planets, shootingStars = [], [], []
    planetCount, starCount, shootingStarCount = 1, 120, 1
    for i in range (0, starCount):
        stars.append(Stars(p.x, p.y))
    for i in range (0, planetCount):
        planets.append(Planets(p.x, p.y, planetImgs[randint(0, len(planetImgs) - 1)]))
    for i in range (0, shootingStarCount):
        shootingStars.append(ShootingStars(p.x, p.y))
    enemyPos = map.getAll('e')
    enemies = []
    enemyDict = {}
    for en in enemyPos:
        enemies.append(Enemy(map, en))
        enemyDict[(en[0], en[1])] = True



    while running:
        t = pygame.time.get_ticks()
        # deltaTime in seconds.
        deltaTime = (t - getTicksLastFrame) / 1000.0 * 60
        
        getTicksLastFrame = t
        #print(deltaTime)
        # this enables us to exit the game
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_w:
                    keyPressed[2] = 1

                if event.key == K_a:
                    keyPressed[3] = 1
                    
                if event.key == K_s:
                    keyPressed[0] = 1

                if event.key == K_d:
                    keyPressed[1] = 1
                if event.key == K_SPACE:
                    keyPressed[4] = 1
                if event.key == K_RETURN:
                    mapInd += 1
                    if mapInd > len(mapList) - 1:
                        mapInd = 0
                    map = Map(mapList[mapInd])
                    p = Player(map)
                    enemyPos = map.getAll('e')
                    stars, planets, shootingStars = [], [], []
                    for i in range (0, starCount):
                        stars.append(Stars(p.x, p.y))
                    for i in range (0, planetCount):
                        planets.append(Planets(p.x, p.y, planetImgs[randint(0, len(planetImgs) - 1)]))
                    for i in range (0, shootingStarCount):
                        shootingStars.append(ShootingStars(p.x, p.y))
                    enemies = []
                    enemyDict = {}
                    for en in enemyPos:
                        enemies.append(Enemy(map, en))
                        enemyDict[(en[0], en[1])] = True
            elif event.type == KEYUP:
                if event.key == K_w:
                    keyPressed[2] = 0
                if event.key == K_a:
                    keyPressed[3] = 0
                if event.key == K_s:
                    keyPressed[0] = 0
                if event.key == K_d:
                    keyPressed[1] = 0
                if event.key == K_SPACE:
                    keyPressed[4] = 0
                # if event.key == K_UP:
                #     if (settings.size < 8):
                #         #settings.size += 1
                #         #settings.tSize = settings.size * settings.scale
                # if event.key == K_DOWN:
                #     if (settings.size > 0):
                        #settings.size -= 1
                        #settings.tSize = settings.size * settings.scale
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #print("mouse pressed")
                MousePressed = True
                if (p.bow.lastArrow > p.bow.firingSpeed) : 
                    p.bow.drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                #pos = pygame.mouse.get_pos()
                MousePressed = True
                p.bow.drawing = False
                p.bow.framesDrawn = 0
                #print(pos)
                if(p.bow.lastArrow > p.bow.firingSpeed and p.bow.bowStrength > .30):
                    arrows.append(Arrow(p.x, p.y, pos[0] + xOff, pos[1] + yOff, p.bow.velocity * p.bow.bowStrength))
                    #print("Creating an arrow!")
                    p.bow.lastArrow = 0
                
                #p.bow.fireBow(pos)
                #print(pos)

            elif event.type == pygame.QUIT:
                running = False
        #clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
        pos = pygame.mouse.get_pos() # Part A of Awesome
        #arrows.append(Arrow(p.x, p.y, pos[0] + xOff, pos[1] + yOff, p.bow.velocity * p.bow.bowStrength))
        # rest of code goes here
        # if c3 > 120:
        #     incDec = False
        # elif c3 < 20:
        #     incDec = True
        # if incDec:
        #     c3 += 1
        # else: 
        #     c3 -= 1
        screen.fill((0, 0, 30))
        for star in stars:
            star.drawX = -(star.x - xOff) + settings.width
            star.drawY = -(star.y - yOff) + settings.height
            star.update()
            star.draw_stars(screen)
            
        
        
        for planet in planets:
            planet.drawX = -(planet.x - xOff) + settings.width
            planet.drawY = -(planet.y - yOff) + settings.height
            planet.update()
            planet.draw_planets(screen)

        

        
        for star in shootingStars:
            star.drawX = -(star.x - xOff) + settings.width
            star.drawY = -(star.y - yOff) + settings.height
            star.update()
            star.draw_shooting_stars(xOff, yOff, screen)


        stars = newBack(stars, p, 0, planetImgs)
        planets = newBack(planets, p, 1, planetImgs)
        shootingStars = newBack(shootingStars, p, 2, planetImgs)

        if len(shootingStars) < shootingStarCount:
            shootingStars.append(ShootingStars(p.x, p.y))


        p.update(keyPressed, map.tiles, deltaTime)
        off = calcOff(p.x, p.y)
        xOff, yOff = off
        p.bow.update(pos[0] + xOff - p.x, pos[1] + yOff - p.y)
        for enemy in enemies:
            enemy.update(p.xIso, p.yIso, map.tiles, enemyDict)
        
        if (checkCollision(p, enemies)):
            p.gotHit()
        
        


        map.draw_map(xOff, yOff, screen, pos, MousePressed, p.xIso, p.yIso)
        p.draw_player(xOff, yOff, screen, pygame)
        p.bow.drawBow(screen, xOff, yOff, pygame, p.y, p.x)
        for enemy in enemies:
            enemy.draw(screen, xOff, yOff)


        for arrow in arrows:
            arrow.drawX = -(arrow.y - xOff) + settings.width
            arrow.drawY = -(arrow.x - yOff) + settings.height
            arrow.update(deltaTime)
            arrow.draw_arrow(xOff, yOff, screen, pygame)
            if (arrow.offMap(p.x, p.y)):
                arrows.remove(arrow)
                del arrow
        winning = checkWin(p, map)
        if winning:
            mapInd += 1
            if mapInd > len(mapList) - 1:
                mapInd = 0
            map = Map(mapList[mapInd])
            p = Player(map)
            enemyPos = map.getAll('e')
            stars, planets, shootingStars = [], [], []
            for i in range (0, starCount):
                stars.append(Stars(p.x, p.y))
            for i in range (0, planetCount):
                planets.append(Planets(p.x, p.y, planetImgs[randint(0, len(planetImgs) - 1)]))
            for i in range (0, shootingStarCount):
                shootingStars.append(ShootingStars(p.x, p.y))
            enemies = []
            enemyDict = {}
            for en in enemyPos:
                enemies.append(Enemy(map, en))
                enemyDict[(en[0], en[1])] = True


        #p.bow.drawBow(screen, xOff, yOff, pygame, p.y, p.x)
        
        
        #print(p.x)
        #del arrow


        
        #debugText = font.render("X:" + str(p.x) + "\n Y: " + str(p.y), True, (255, 255, 255), (0, 0, 0))
        #textRect2 = debugText.get_rect()

        # FPS is this _____________________________________________________
        #text = font.render(str(fpsClock), True, (255, 255, 255), (0, 0, 0))
        #textRect = text.get_rect()
        #screen.blit(text, textRect)
        # FPS is this _____________________________________________________

        #screen.blit(debugText, textRect2)
        #screen.fill((255, 0, 30, 255 - p.kbForce))
        pygame.display.update()
        
            
        fpsClock.tick(FPS)
        # draw background first

    #print(a)
    #print(b)
    
    print("Ending now")


def checkCollision(p, enemies):
    for e in enemies:
        if (p.xIso == e.yIso and p.yIso == e.xIso):
            return True
    return False
            #print("Player is hit!")
def newBack(stars, p, id, planetImgs):
    for star in stars:
        #print(star.drawX)
        if not checkStars(star):
                stars.remove(star)
                del star
                if id == 0:
                    stars.append(Stars(p.x ,p.y))
                elif id == 1:
                    stars.append(Planets(p.x ,p.y, planetImgs[randint(0, len(planetImgs) - 1)]))
                elif id == 2:
                    stars.append(ShootingStars(p.x ,p.y))
    return stars
def checkStars(star):
    if (star.drawX > settings.width + 300):
        return False
    if (star.drawX < -300):
        return False
    if (star.drawY > settings.height + 300):
        return False
    if (star.drawY < -300):
        return False
    return True

def checkWin(p, map):
    if map.tiles[p.xIso][p.yIso].type == 'F':
        print("You Win!")
        return True
    return False



def calcOff(x, y):

    Off = [x - settings.width / 2, y - settings.height / 2]
    #print(settings.size * len(tiles), " ", Off[1])
    return Off

if __name__ == "__main__":
    main()