from this import d
from math import floor, ceil
from Bow import Bow
import settings
import pygame
import tileImages

# purpose of map: hold a two-d array of the maps' contents and a variety of functions to access and interact w/ them
class Player: # DON'T USE lowercase map
    # LEGEND:
    '''
    b = boulder
    p = path
    w = wall
    . = empty
    '''
    def __init__(self, selectedMap):
        print("Initialized Player")
        self.checkPoint = selectedMap.getFirst("s")
        print(self.checkPoint)
        self.x = settings.width#start[0] * settings.size + settings.size / 4
        self.y = settings.height#start[1] * settings.size + settings.size / 4
        self.x = settings.width - (self.checkPoint[1] - self.checkPoint[0] + 1) / 2 * settings.tSize
        self.y = settings.height - (self.checkPoint[1] + self.checkPoint[0]  - 1) / 4 * settings.tSize 
        self.kbForce = 0
        print(self.x)
        print(self.y)
        self.xIso = 0
        self.yIso = 0
        self.maxSpeed = settings.tSize / 16
        self.acc = settings.tSize / 250
        self.dx = 0
        self.dy = 0  #dmg vel fspd
        self.bow = Bow(3, 10, 70)
        self.frame = 0
        self.imgLook = 0
        self.img = tileImages.player
        self.shadow = pygame.transform.scale(pygame.image.load('Shadow.png').convert_alpha(), (settings.tSize / 2, settings.tSize / 2))
        self.inventory = []
        self.shadowY = self.y
        
        self.gravity = 0
        #print(os.getcwd())
        #print(self.read_file("map1.txt"))

    def boundary(self, tile):
        return tile == 'b'
    
    def gotHit(self):
        self.kbForce = -13


    def checkBounds(self, tiles):
        #print(self.xIso, len(tiles[self.yIso]))
        #print(self.xIso, len(tiles))
        if (self.yIso > len(tiles[0]) - 2): # - 2
            return False
        if (self.xIso > len(tiles) - 2): # -5
            return False
        # if (self.xIso > len(tiles[0])):
        #     return False
        return True
    def update(self, keyPressed, tiles, deltaTime):
        if (self.kbForce < 0):
            self.kbForce += .2
        else:
            self.kbForce = 0

        self.dx += self.acc * (keyPressed[3] - keyPressed[1])
        self.dy += self.acc * (keyPressed[2] - keyPressed[0]) #'w' and 's' on the keyboard
    
        x = self.x - settings.width
        y = self.y - settings.height
        s = settings.tSize
        
        self.yIso = -round((2 * y - x) / s) + 1
        self.xIso = -round((2 * y + x) / s)

        
        g = .4 * deltaTime
        self.gravity -= g 
        
        if (self.checkBounds(tiles)):
            if (self.xIso < 0 or self.yIso < 0):
                self.tile = '.'
            else: 
                self.tile = tiles[self.xIso][self.yIso].type
            if (self.tile in ['p', 's', 'H', 'B']):
                if (self.tile == 'H'):
                    self.checkPoint = [self.yIso, self.xIso]
                if (keyPressed[4]):
                    if (self.gravity == -g):
                        self.gravity = 8.5 / (4 / settings.size)
                if(self.gravity < 0):
                    self.gravity = 0
            #if (self.tile == 'W'):
                # if(self.gravity > 0):
                #     self.gravity = 0
            
            #print(self.yIso, len(tiles))
        # COLLISIONS:
        else:
            self.x = settings.width - (self.checkPoint[1] - self.checkPoint[0] + 1) / 2 * settings.tSize
            self.y = settings.height - (self.checkPoint[1] + self.checkPoint[0]  - 1) / 4 * settings.tSize 
            self.kbForce = 0
            self.dx = 0
            self.dy = 0
            self.gravity = 0

        # xIso = xOff + s * (x - y) / 2
        # yIso = yOff + s * (x + y) / 4
        #
        #
        
        #print(self.xIso, self.yIso)
        #print(self.x, " ", self.y)
        if (self.dx > self.maxSpeed):
            self.dx = self.maxSpeed
        if (self.dx > self.acc * 4 /5):
            self.dx -= self.acc / 2
        elif (self.dx < -self.maxSpeed):
            self.dx = -self.maxSpeed
        elif (self.dx < -self.acc * 4 /5):
            self.dx += self.acc / 2
        else:
            self.dx = 0
        if (self.dy > self.maxSpeed):
            self.dy = self.maxSpeed
        if (self.dy > self.acc * 3 /5):
            self.dy -= self.acc / 2
        elif (self.dy < -self.maxSpeed):
            self.dy = -self.maxSpeed
        elif (self.dy < -self.acc * 3 /5):
            self.dy += self.acc / 2
        else:
            self.dy = 0
        
        #print(tiles[self.xIso][self.yIso + 1].type)
        # Try to get collisions working at some point in the future: not necessary now, might take a WHILE
        newX = self.dx * deltaTime + self.x - settings.width
        newY = self.dy * deltaTime + self.y - settings.height
        newyIso = -round((2 * newY - newX) / s) + 1
        newxIso = -round((2 * newY + newX) / s)
        
        #print(self.xIso, newxIso, self.yIso, newyIso)
        #if newxIso < self.xIso:
        # if newxIso < self.xIso and newyIso < self.yIso:
        if (not keyPressed[4] and (tiles[self.xIso][self.yIso].type != '.' and tiles[newxIso][newyIso].type == '.') or tiles[newxIso][newyIso].type == 'W'):
            if newxIso < self.xIso and newyIso < self.yIso:
                pass
            elif newxIso < self.xIso:       # UP and to the LEFT                
                if (self.dy > self.dx):
                    self.dy = -1/2 * self.dx
                else:                    
                    self.dy = -1/2 * self.dx
            
            elif newyIso < self.yIso:                
                if (self.dx > self.dy):
                    self.dy = 1/2 * self.dx
                else:                    
                    self.dy = 1/2 * self.dx
            if (tiles[newxIso][newyIso].type == 'W'):
                #print("Working")
                if self.gravity > 0:
                    self.gravity = 0
        self.y += ((self.dy + self.gravity + self.kbForce) * deltaTime)
        self.x += ((self.dx) * deltaTime) 



        if (self.tile != '.'):
            
            self.shadowY = self.y - settings.tSize / 8
        
        self.frame += (.03 * abs(self.dy / 2) + .03 * abs(self.dx / 2)) * deltaTime
        #print(self.frame)
        self.imgLook = 1
        if self.dx == 0 and self.dy == 0:
            self.imgLook = 0
        if self.gravity != 0:
            if self.dx > 0:
                self.imgLook = 6
                #print("Work5")
            else:
                self.imgLook = 5
                #print("Work6")

        elif abs(self.dy) >= abs(self.dx):
            if self.dy < 0:
                self.imgLook = 1
            elif self.dy > 0:
                self.imgLook = 4
        elif abs(self.dx) > abs(self.dy):
            if self.dx > 0:
                self.imgLook = 3
            elif self.dx < 0:
                self.imgLook = 2
        


        if self.frame >= 4:
            self.frame = 0
        #if (self.gravity < 0):
            #self.shadowY = self.y - 


    def draw_player(self, xOff, yOff, screen, pygame):
        color = (30, 255, 155)
        
        #pygame.draw.rect(screen, color, pygame.Rect(self.xIso * settings.size + 160, self.yIso * settings.size + 160, settings.size, settings.size), 2)
        #pygame.draw.rect(screen, color, pygame.Rect(0 * settings.size + 160, 0 * settings.size + 160, settings.size, settings.size), 2)
        #pygame.draw.rect(screen, color, pygame.Rect(3 * settings.size + 160, 3 * settings.size + 160, settings.size, settings.size), 2)
        if (self.y >= self.shadowY):
            screen.blit(self.shadow, (self.x - xOff, -(self.shadowY - yOff) + settings.height))
        screen.blit(self.img[self.imgLook][floor(self.frame)], (self.x - xOff, self.y - yOff))
        #print(self.imgLook, floor(self.frame))
        
        #pygame.draw.ellipse(screen, color, (self.x - xOff, self.y - yOff, settings.p_width, settings.p_length), 100)
        #self.bow.drawBow(screen, xOff, yOff, pygame, self.x, self.y)
        #elif(self.tiles[x][y] == "b"):
        #    pygame.draw.boulder(screen, color, (y * settings.size, x * settings.size, settings.size, settings.size), 1)
