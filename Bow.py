import settings
import pygame
from math import atan2, sin, cos, pi
class Bow:
    def __init__(self, dmg, vel, fir):
        self.damage = dmg
        self.velocity = vel
        self.firingSpeed = fir
        self.framesDrawn = 0
        self.lastArrow = fir
        self.drawing = False
        self.bowStrength = 0.0
        self.bowIm = pygame.transform.scale(pygame.image.load('Bow.png').convert_alpha(), (settings.tSize, settings.tSize))
        self.arrowIm = pygame.transform.scale(pygame.image.load('Arrow.png').convert_alpha(), (settings.tSize, settings.tSize))
        
        

    def update(self, mx, my):
        self.deg = self.calcDeg(mx, my)
        self.bowIm = pygame.transform.rotate(pygame.image.load('Bow.png'), self.deg -90)
        self.arrowIm = pygame.transform.rotate(pygame.image.load('Arrow.png'), self.deg + 180)
        self.bowStrength = self.framesDrawn / self.firingSpeed
        if (self.drawing and self.framesDrawn < self.firingSpeed):
            self.framesDrawn += 1
        self.lastArrow += 1


    def calcDeg(self, mx, my):
        theta = atan2(mx, my)
        return theta * 180 / pi

    def drawBow(self, screen, xOff, yOff, pygame, x, y):
        red = (205, 30, 30)
        green = (30, 225, 30)
        gold = (255, 215, 0)
        blue = (10, 10, 188)
        height = 5
        width = settings.width / 2
        
        if (self.drawing):
            w = width * self.bowStrength
            pygame.draw.rect(screen, red, (settings.width / 4, settings.height - 20,  width, height), 2)
            pygame.draw.rect(screen, red, (settings.width / 4 + .3 *(settings.width / 2), settings.height - 20, 4  , height), 4)
            pygame.draw.rect(screen, green, (settings.width / 4, settings.height - 20, w, height), 2)
            if w == width:
                pygame.draw.rect(screen, gold, (settings.width / 4, settings.height - 20, width, height), 4)
            dy = 16 * sin(self.deg / 180 * pi) * (1.01 - self.bowStrength)
            dx = 16 * cos(self.deg / 180 * pi) * (1.01 - self.bowStrength)
            screen.blit(self.arrowIm, (y - xOff + dy, x - yOff + dx))
            screen.blit(self.bowIm, (y - xOff, x - yOff))
            
        elif (self.lastArrow < self.firingSpeed):
            w = width * (self.lastArrow / self.firingSpeed)
            pygame.draw.rect(screen, red, (settings.width / 4, settings.height - 20,  width, height), 2)
            pygame.draw.rect(screen, blue, (settings.width / 4, settings.height - 20, w, height), 2)
            # if w == width:
            #     pygame.draw.rect(screen, gold, (settings.width / 4, settings.height - 20, width, height), 4)
