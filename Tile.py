import settings
import pygame
from pygame.locals import *
from Bow import Bow
import tileImages
class Tile:
    def __init__(self, x, y, type):
        self.img = None
        self.img2 = None
        self.img3 = None
        self.type = type
        self.x = x
        self.y = y
        self.isoX = settings.tSize * (x - y) / 2
        self.isoY = settings.tSize * (x + y) / 4
        self.selected = False
    
    def update(self, yIso, xIso, pos, s, mp):
        if (yIso - pos[1] < s / 2 and xIso - pos[0] < 0 and yIso - pos[1] > - s /2 and xIso - pos[0] > -s):
            self.selected = True
        else:
            self.selected = False
    
    def drawTile(self, screen, iso, pos, mp):
        screen.blit(self.img, iso)

        
class Empty(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, '.')
    def drawTile(self, screen, iso, pos, mp):
        return None
        
class Path(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, 'p')
        #print("Setting path at", x, y)
        self.img = tileImages.isometric#pygame.transform.scale(pygame.image.load('Isometric.png').convert_alpha(), (settings.tSize, settings.tSize))
    
    def drawTile(self, screen, iso, pos, mp):
        screen.blit(self.img, iso)
        #print(self.isoX)


class Wall(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, 'W')
        #print("Setting path at", x, y)
        self.img = tileImages.wall#pygame.transform.scale(pygame.image.load('Isometric.png').convert_alpha(), (settings.tSize, settings.tSize))
    
    def drawTile(self, screen, iso, pos, mp):
        screen.blit(self.img, iso)
        for i in range(0, 8):
            screen.blit(self.img, (iso[0], iso[1] - i * 9 * settings.size))
        #print(self.isoX)

class Floating(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, 'p')
        #print("Setting path at", x, y)
        self.img = tileImages.floaters#pygame.transform.scale(pygame.image.load('Isometric.png').convert_alpha(), (settings.tSize, settings.tSize))
    
    def drawTile(self, screen, iso, pos, mp):
        screen.blit(self.img, iso)
        
        
        #print(self.isoX)

class HeartAlter(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, 'H')
        self.img = pygame.transform.scale(pygame.image.load('Isometric.png').convert_alpha(), (settings.tSize, settings.tSize))
        self.img2 = pygame.transform.scale(pygame.image.load('Heart Alter.png').convert_alpha(), (settings.tSize, settings.tSize))
        self.img3 = pygame.transform.scale(pygame.image.load('Heart.png').convert_alpha(), (settings.tSize, settings.tSize))
    def drawTile(self, screen, iso, pos, mp):
        screen.blit(self.img, iso)
        screen.blit(self.img2, (iso[0], iso[1] - 9 * settings.size))
        screen.blit(self.img3, (iso[0], iso[1] - 18 * settings.size))


class Bush(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, 'p')
        self.img = pygame.transform.scale(pygame.image.load('Isometric.png').convert_alpha(), (settings.tSize, settings.tSize))
        self.img2 = pygame.transform.scale(pygame.image.load('Bush.png').convert_alpha(), (settings.tSize, settings.tSize))
    def drawTile(self, screen, iso, pos, mp):
        screen.blit(self.img, iso)
        screen.blit(self.img2, (iso[0], iso[1] - 9 * settings.size))

class Flag(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, 'F')
        self.img = pygame.transform.scale(pygame.image.load('Isometric.png').convert_alpha(), (settings.tSize, settings.tSize))
        self.img2 = pygame.transform.scale(pygame.image.load('Flag.png').convert_alpha(), (settings.tSize, settings.tSize))
    
    def drawTile(self, screen, iso, pos, mp):
        screen.blit(self.img, iso)
        screen.blit(self.img2, (iso[0], iso[1] - 9 * settings.size))
        
    

class Chest(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, 'C')
        self.img = pygame.transform.scale(pygame.image.load('Isometric.png').convert_alpha(), (settings.tSize, settings.tSize))
        self.img2 = pygame.transform.scale(pygame.image.load('ChestClosed.png').convert_alpha(), (settings.tSize, settings.tSize))
        self.contents = [Bow(3, 10, 100)]
    
    def update(self, yIso, xIso, pos, s, mp):
        if (yIso - pos[1] < s / 2 and xIso - pos[0] < 0 and yIso - pos[1] > - s /2 and xIso - pos[0] > -s):
            self.selected = True
            self.img2 = pygame.transform.scale(pygame.image.load('ChestHighlighted.png').convert_alpha(), (settings.tSize, settings.tSize))
            if(mp):
                self.open()
        else:
            self.selected = False
            self.img2 = pygame.transform.scale(pygame.image.load('ChestClosed.png').convert_alpha(), (settings.tSize, settings.tSize))
    def open(self):
        self.type = 'c'
        self.img2 = pygame.transform.scale(pygame.image.load('ChestLooted.png').convert_alpha(), (settings.tSize, settings.tSize))
        self.contents = []
    
    def drawTile(self, screen, iso, pos, mp):
        self.update(iso[1], iso[0], pos, settings.tSize, mp)
        screen.blit(self.img, iso)
        screen.blit(self.img2, (iso[0], iso[1] - 9 * settings.size))
        
        