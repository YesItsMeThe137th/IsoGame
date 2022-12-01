from random import random
import settings
import os
from math import floor, ceil, sqrt
from collections import defaultdict
from random import randint
import pygame
from pygame.locals import *
from Tile import *
#from Ambiance import Ambiance

# purpose of map: hold a two-d array of the maps' contents and a variety of functions to access and interact w/ them
class Map: # DON'T USE lowercase map
    # LEGEND:
    '''
    b = boulder
    p = path
    s = Player start point (is also a path)
    w = wall
    . = empty
    '''
    def read_file(self, filename):
        with open(filename, "r") as f:
            return [[c for c in line] for line in f.readlines()]

    def load_map(self, file):
        newMap = self.read_file(file)
        for i in range(len(newMap)):
            if "\n" in newMap[i]:
                newMap[i].remove("\n")
        return newMap
    def __init__(self, selectedMap):
        print("Initialized Map")
        self.mapped = self.load_map(selectedMap)
        #print(self.mapped)
        self.tiles = []
        #thingDict = {}
        self.fogImg = pygame.transform.scale(pygame.image.load('fog.png').convert_alpha(), (settings.tSize / 2, settings.tSize / 2))
        for x, tiles in enumerate(self.mapped):
            row = []
            for y, tile in enumerate(tiles):
                #print(tile)
                if(tile == '.'):
                    #print("")
                    row.append(Empty(x, y))
                elif(tile == 'p' or tile == 's' or tile == 'e'):
                    row.append(Path(x, y))
                    #print("Adding path!")
                elif(tile == 'f'):
                    row.append(Floating(x, y))
                elif(tile == 'B'):
                    row.append(Bush(x, y))
                    #print("Adding path!")
                elif(tile == 'C'):
                    row.append(Chest(x, y))
                    #self.tiles[x][y].type = Chest(x, y)
                elif(tile == 'H'):
                    row.append(HeartAlter(x, y))
                elif(tile == 'F'):
                    row.append(Flag(x, y))
                elif(tile == 'W'):
                    row.append(Wall(x, y))
                
            self.tiles.append(row)
       

    def __str__(self):
        string = ""
        for t in self.tiles:
            for e in t:
                string += e
            string += "\n"
        return string
    
    def getAll(self, piece):
        places = []
        for x in range(len(self.tiles[0])):
            for y in range(len(self.tiles)):
                if(self.mapped[y][x]) == piece:
                    places.append([x, y])
        return places
        
    def getFirst(self, piece):
        for x in range(len(self.tiles[0])):
            for y in range(len(self.tiles)):
                if(self.mapped[y][x]) == piece:
                    return [x, y]
        return [None, None]

    

    def onScreen(self, x, y):
        if (x > - settings.tSize and x < settings.width):
            if (y > - settings.tSize and y < settings.height):
                return True
    def xOnScreen(self, x):
        if (x > - settings.tSize and x < settings.width):
            return True
    def yOnScreen(self, y):
        if (y > - settings.tSize and y < settings.height):
            return True

    def draw_map(self, xOff, yOff, screen, pos, mp, px, py): 
        minX = int(px - settings.width / settings.tSize) - 3 # number of tiles to the left of the player
        maxX = int(px + settings.width / settings.tSize) + 3
        minY = int(py - 2 * settings.height / settings.tSize)
        maxY = int(py + 2 * settings.height / settings.tSize)
        minX = max(0, minX)
        minY = max(0, minY)
        maxX = min(maxX, len(self.tiles) - 1)# Error seems to be here
        maxY = min(maxY, len(self.tiles[0]) -1)
        
        #print(minX, maxX, minY, maxY)
        #print(len(self.tiles), len(self.tiles[0]))
        #pygame.draw.rect(screen, (30, 30, 30), pygame.Rect(160,  160, len(self.tiles) * settings.size, len(self.tiles[0]) * settings.size), 2)
        for x in range(minX, maxX):
             for y in range(minY, maxY):
                #pygame.draw.rect(screen, (30, 30, 30), pygame.Rect(x * settings.size + 160, y * settings.size + 160, settings.size, settings.size), 2)
                xIso = xOff + self.tiles[x][y].isoX # + xIsoOff
                #if(self.xOnScreen(xIso)):
                yIso = yOff + self.tiles[x][y].isoY
                    #if(self.yOnScreen(yIso)):
                if (self.tiles[x][y].type != '.'):
                    self.tiles[x][y].drawTile(screen, (xIso, yIso), pos, mp)
                    #pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x * settings.size + 160, y * settings.size + 160, settings.size, settings.size), 2)
            
                
                # if (tile.type in ['p', 's', 'H', 'C', 'c', 'B', 'F']):
                #     if(self.xOnScreen(xIso)):
                #         yIso = yOff + self.tiles[x][y].isoY
                #         if(self.yOnScreen(yIso)):                                
                #             screen.blit(self.tiles[x][y].img, (xIso, yIso))
                #             if (tile.type in ['H', 'C', 'c']):
                #                 self.tiles[x][y].update(yIso, xIso, pos, s, mp)
                #                 screen.blit(self.tiles[x][y].img2, (xIso, yIso- 9 * settings.size))
                #                 if (tile.type in ['H']):
                #                     screen.blit(self.tiles[x][y].img3, (xIso, yIso- 18 * settings.size))
                #             elif (tile.type in ['B', 'F']):
                #                 screen.blit(self.tiles[x][y].img2, (xIso, yIso- 9 * settings.size))
                            
                            #pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x * settings.size + 160, y * settings.size + 160, settings.size, settings.size), 2)
                    #screen.blit(self.tiles[x][y].img, (xIso, yIso))
                            #if (tile == 'H'):
                                #screen.blit(self.heartAlter, (xIso, yIso + (-9 * settings.size)))
                                #screen.blit(self.heart, (xIso, yIso + (-18 * settings.size)))
                            #if (tile == 'C'):
                                #if ()
                                #screen.blit(self.chestClosed, (xIso, yIso + (-9 * settings.size)))
                                #screen.blit(self.heart, (xIso, yIso + (-18 * settings.size)))
                    

