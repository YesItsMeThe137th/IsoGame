import random
import settings
import pygame
class Planets:
    def __init__(self, px, py, planetImg):
        w = settings.width
        h = settings.height 
        self.life = 0
        s = random.randint(settings.scale, settings.tSize)
        self.img = pygame.transform.scale(pygame.image.load(planetImg).convert_alpha(), (s, s))
        randX, randY = random.randint(-settings.width / 2 - 300, settings.width / 2 + 300), random.randint(-settings.height / 2 - 300, settings.height / 2 + 300)
        while(randX > -settings.width / 2 and randX < settings.width / 2 and randY < settings.height / 2 and randY > -settings.height / 2):
            randX, randY = random.randint(-settings.width / 2 - 300, settings.width / 2 + 300), random.randint(-settings.height / 2 - 300, settings.height / 2 + 300)
        self.x = px + randX
        self.y = py + randY
        
        #print(self.x, self.y)
        self.drawX = 0
        self.drawY = 0
    def update(self):
        pass

    def draw_planets(self, screen):
        screen.blit(self.img, (self.drawX, self.drawY))
        #pygame.draw.ellipse(screen, self.color, (self.drawX - self.bright / 2, self.drawY  - self.bright / 2, self.bright, self.bright), 100)
