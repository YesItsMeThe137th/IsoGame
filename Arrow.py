from math import atan, atan2, floor, sqrt, pi

import pygame

import settings


class Arrow:
    def __init__(self, x, y, mouseX, mouseY, velocity):
        self.y = x
        self.x = y
        mx = mouseX - x
        my = mouseY - y
        #print(mouseX - x, " ", mouseY - y)
        # now calculate dx and dy
        r = sqrt(mx * mx + my * my)
        self.v = velocity
        self.dy = self.v * mx / r
        self.dx = self.v * my / r
        self.theta = atan2(mx, my)
        self.deg = self.theta * 180 / pi
        self.arrowIm = pygame.transform.rotate(pygame.image.load('Arrow.png').convert_alpha(), self.deg + 180)
        self.drawX = 0
        self.drawY = 0
        
    def update(self, deltaTime):
        self.x -= (self.dx) * deltaTime
        self.y -= (self.dy) * deltaTime
        self.dx += .4 * deltaTime
        #if (tiles[floor(self.x / settings.size)][floor(self.y / settings.size)] in settings.walls):

    def offMap(self, px, py):
        
        #print(settings.width)
        
        if (self.y - px  > settings.width / 2 + 100):
            print("Deleting 1")
            return True
        elif (self.y < px - settings.width / 2 - 100): 
            print("Deleting 2")
            return True
        elif (self.x > py + settings.height / 2 + 100): 
            print("Deleting 3")
            return True
        #a  = yOff - self.y 
        #print(a)
        # if (self.x - px  < settings.width / 2):
        #     #print("Deleting 3")
        #     return True
        # if (px - self.x  < settings.width / 2):
        #     #print("Deleting 4")
        #     return True
    #def collision(self, tiles):


    def draw_arrow(self, xOff, yOff, screen, pygame):
        self.theta = atan2(self.dy, self.dx)
        
        self.deg = self.theta * 180 / pi
        self.arrowIm = pygame.transform.rotate(pygame.image.load('Arrow.png').convert_alpha(), self.deg + 180)
        #self.arrowIm = pygame.transform.rotate(pygame.image.load('Arrow.png'), self.deg + 180)
        screen.blit(self.arrowIm, (self.drawX, self.drawY))
        #pygame.draw.ellipse(screen, color, (self.y - xOff, self.x - yOff, settings.size / 8, settings.size / 8), 100)
