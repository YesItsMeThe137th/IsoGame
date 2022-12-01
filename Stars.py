import random
import settings
import pygame
class Stars:
    def __init__(self, px, py):
        self.life = 0
        self.bright = 2
        self.lifeSpan = random.randint(60, 180)
        self.brightnessMin = self.bright
        self.brightnessMax = random.randint(4, 15)
        self.waxing = True
        # self.x = px + random.randint(-settings.width  / 2, settings.width  / 2)
        # self.y = py + random.randint(-settings.height / 2, settings.height / 2)
        self.x = px + random.randint(-settings.width / 2 - 300, settings.width / 2 + 300)
        self.y = py + random.randint(-settings.height / 2 - 300, settings.height / 2 + 300)
        self.drawX = 0
        self.drawY = 0
        
        self.color = (random.randint(160, 255),random.randint(160, 255),random.randint(160, 255))
    def update(self):
        if self.waxing:
            self.life += 1
            self.bright += (self.brightnessMax - self.brightnessMin) / self.lifeSpan
            #print(self.bright)
        else:
            self.life -= 1
            self.bright -= (self.brightnessMax - self.brightnessMin) / self.lifeSpan
            #print(self.bright)
            
        
        if self.life == self.lifeSpan:
            self.waxing = False
        elif self.life == 0:
            self.waxing = True

    def draw_stars(self, screen):
        pygame.draw.ellipse(screen, self.color, (self.drawX - self.bright / 2, self.drawY  - self.bright / 2, self.bright, self.bright), 100)
