#from settings import settings
import settings
import pygame
from math import atan2, atan, pi
from random import randint
class Enemy:
    def __init__(self, selectedMap, startPoint):
        self.imgDirs = [
            pygame.transform.flip(pygame.transform.scale(pygame.image.load('CrabBack.png').convert_alpha(), (settings.tSize, settings.tSize)), True, False),
            pygame.transform.scale(pygame.image.load('CrabBack.png').convert_alpha(), (settings.tSize, settings.tSize)), 
            pygame.transform.flip(pygame.transform.scale(pygame.image.load('Crab.png').convert_alpha(), (settings.tSize, settings.tSize)), True, False),
            pygame.transform.scale(pygame.image.load('Crab.png').convert_alpha(), (settings.tSize, settings.tSize)) 
        ]
        self.xIso = startPoint[0]
        self.yIso = startPoint[1]
        self.speed = 6
        self.x = settings.width + settings.tSize * (self.xIso - self.yIso) / 2
        self.y = settings.height - settings.tSize * (self.xIso + self.yIso) / 4
        self.theta = 0
        self.lastMove = 0
        self.dir = 0
        self.enemyID = randint(0, 2174000000)

    #def calcDist(pix, piy):
        #
    def update(self, pix, piy, tiles, endict):
        
        
        
        if self.lastMove > self.speed:
            self.calcDir(piy, pix)
            self.pathFind(pix, piy, tiles, endict)
        self.x = settings.width + settings.tSize * (self.xIso - self.yIso) / 2
        self.y = settings.height - settings.tSize * (self.xIso + self.yIso) / 4
        self.lastMove += 1
        

    def calcDir(self, piy, pix):
        self.theta = atan2((self.xIso - piy), (self.yIso - pix))
        if (self.theta > pi / -4 and self.theta < pi / 4):
            #print("Now is no time")
            self.dir = 0
        elif (self.theta >= pi / 4 and self.theta < 3 * pi / 4):
            #print("Now is 1 time")
            self.dir = 1
        elif (self.theta >= -3 * pi / 4 and self.theta < pi / -4):
            #print("Now is 2nd time", self.theta)
            self.dir = 2
        else:
            #print("meh meh meh", self.theta)
            self.dir = 3
        
    def pathFind(self, pix, piy, tiles, endict):
        # would prob be better to replace this witha  pathfinding algorithm
        #print(self.theta)
        #self.deg = atan((self.yIso - piy) / (self.xIso - pix))
        self.lastMove = 0
        #print(pix, piy, self.xIso, self.yIso)
        # print(self.theta)
        # print(tiles[self.yIso][self.xIso + 1].type,tiles[self.yIso][self.xIso - 1].type,tiles[self.yIso + 1][self.xIso].type,tiles[self.yIso - 1][self.xIso].type)
        if self.dir == 0:
            
            if(tiles[self.yIso - 1][self.xIso].type == 'p' and (not (self.xIso, self.yIso-1) in endict or not endict[(self.xIso, self.yIso - 1)])):
                self.move(0, -1, endict)
            else:
                if (self.theta > 0):
                    if(tiles[self.yIso][self.xIso - 1].type == 'p'and (not (self.xIso - 1, self.yIso) in endict or not endict[(self.xIso - 1, self.yIso)])):
                        self.dir = 1
                        self.move(-1, 0,endict) 
                elif (self.theta <= 0):
                    if(tiles[self.yIso][self.xIso + 1].type == 'p' and (not (self.xIso + 1, self.yIso) in endict or not endict[(self.xIso + 1, self.yIso)])):
                        self.dir = 2
                        self.move(1, 0,endict) 
                
        elif self.dir == 1:
            if(tiles[self.yIso][self.xIso - 1].type == 'p'and (not (self.xIso - 1, self.yIso) in endict or not endict[(self.xIso - 1, self.yIso)])):
                self.move(-1, 0,endict) 
            else: 
                if (self. theta > pi /2):
                    if(tiles[self.yIso - 1][self.xIso].type == 'p' and (not (self.xIso, self.yIso-1) in endict or not endict[(self.xIso, self.yIso - 1)])):
                        self.dir = 0
                        self.move(0, -1, endict)
                elif (self.theta <= pi / 2):
                    if(tiles[self.yIso][self.xIso + 1].type == 'p' and (not (self.xIso + 1, self.yIso) in endict or not endict[(self.xIso + 1, self.yIso)])):
                        self.dir = 2
                        self.move(1, 0,endict)  # maybe this should be 0, 1
                
        elif self.dir == 2:
            if(tiles[self.yIso][self.xIso + 1].type == 'p' and (not (self.xIso + 1, self.yIso) in endict or not endict[(self.xIso + 1, self.yIso)])):
                self.move(1, 0,endict) 
            else:
                if (self.theta > - pi * 2):
                    #print("Moving by other way")
                    if(tiles[self.yIso + 1][self.xIso].type == 'p' and (not (self.xIso, self.yIso + 1) in endict or not endict[(self.xIso, self.yIso + 1)])):
                        self.dir = 3
                        self.move(0, 1, endict) 
                elif (self.theta <= - pi * 2):
                    if(tiles[self.yIso - 1][self.xIso].type == 'p' and (not (self.xIso, self.yIso-1) in endict or not endict[(self.xIso, self.yIso - 1)])):
                        self.dir = 0
                        self.move(0, -1, endict)
                    
        elif self.dir == 3:
            if(tiles[self.yIso + 1][self.xIso].type == 'p' and (not (self.xIso, self.yIso + 1) in endict or not endict[(self.xIso, self.yIso + 1)])):
                self.move(0, 1, endict) 
            else: 
                if (self.theta <= -3 * pi / 4):
                    if(tiles[self.yIso][self.xIso + 1].type == 'p' and (not (self.xIso + 1, self.yIso) in endict or not endict[(self.xIso + 1, self.yIso)])):
                        self.dir = 2
                        self.move(1, 0,endict) 
                elif (self.theta >= 3 * pi / 4):
                    if(tiles[self.yIso][self.xIso - 1].type == 'p'and (not (self.xIso - 1, self.yIso) in endict or not endict[(self.xIso - 1, self.yIso)])):
                        self.dir = 1
                        self.move(-1, 0,endict) 


        
    def move(self, xDir, yDir, endict):
        endict[(self.xIso, self.yIso)] = False
        self.xIso += xDir
        self.yIso += yDir
        endict[(self.xIso, self.yIso)] = True


    def draw(self, screen, xOff, yOff):
        drawX = -(self.x - xOff) + settings.width
        drawY = -(self.y - yOff) + settings.height
        #print(drawX, drawY)
        #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.yIso * settings.size + 160, self.xIso * settings.size + 160, settings.size, settings.size), 2)
        screen.blit(self.imgDirs[self.dir], (drawX, drawY- 9 * settings.size))
        #pygame.draw.ellipse(screen, (255, 0, 0), (drawX, drawY, settings.tSize, settings.tSize / 3), 2)
        #pygame.draw.ellipse(screen, color, (self.x - xOff, self.y - yOff, settings.p_width, settings.p_length), 100)


