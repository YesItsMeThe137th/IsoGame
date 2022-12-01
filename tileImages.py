from ctypes.wintypes import PWIN32_FIND_DATAW
from re import I
import pygame
import settings

def init():
    global isometric, floaters, wall, player#, heartAlter[], chest[], 
    isometric = pygame.transform.scale(pygame.image.load('Isometric.png').convert_alpha(), (settings.tSize, settings.tSize))
    floaters = pygame.transform.scale(pygame.image.load('FloatieBoyz.png').convert_alpha(), (settings.tSize, settings.tSize))
    wall = pygame.transform.scale(pygame.image.load('Wall.png').convert_alpha(), (settings.tSize, settings.tSize))
    player = [[pygame.transform.scale(pygame.image.load('ActualIdle.png').convert_alpha(), (settings.p_length, settings.p_length)),
               pygame.transform.scale(pygame.image.load('ActualIdle.png').convert_alpha(), (settings.p_length, settings.p_length)), 
               pygame.transform.scale(pygame.image.load('ActualIdle.png').convert_alpha(), (settings.p_length, settings.p_length)), 
               pygame.transform.scale(pygame.image.load('ActualIdle.png').convert_alpha(), (settings.p_length, settings.p_length))],
               [pygame.transform.scale(pygame.image.load('Playerwalk1.png').convert_alpha(), (settings.p_length, settings.p_length)),
               pygame.transform.scale(pygame.image.load('ActualIdle.png').convert_alpha(), (settings.p_length, settings.p_length)),
               pygame.transform.flip(pygame.transform.scale(pygame.image.load('Playerwalk1.png').convert_alpha(), (settings.p_length, settings.p_length)), True, False),
               pygame.transform.scale(pygame.image.load('ActualIdle.png').convert_alpha(), (settings.p_length, settings.p_length)),],
               [pygame.transform.scale(pygame.image.load('PlayerWalkRight2.png').convert_alpha(), (settings.p_length, settings.p_length)),
               pygame.transform.scale(pygame.image.load('PlayerWalkRight.png').convert_alpha(), (settings.p_length, settings.p_length)),
               pygame.transform.scale(pygame.image.load('PlayerWalkRight3.png').convert_alpha(), (settings.p_length, settings.p_length)),
               pygame.transform.scale(pygame.image.load('PlayerWalkRight.png').convert_alpha(), (settings.p_length, settings.p_length))],
               [pygame.transform.flip(pygame.transform.scale(pygame.image.load('PlayerWalkRight2.png').convert_alpha(), (settings.p_length, settings.p_length)), True, False),
               pygame.transform.flip(pygame.transform.scale(pygame.image.load('PlayerWalkRight.png').convert_alpha(), (settings.p_length, settings.p_length)), True, False),
               pygame.transform.flip(pygame.transform.scale(pygame.image.load('PlayerWalkRight3.png').convert_alpha(), (settings.p_length, settings.p_length)), True, False),
               pygame.transform.flip(pygame.transform.scale(pygame.image.load('PlayerWalkRight.png').convert_alpha(), (settings.p_length, settings.p_length)), True, False)],
               [pygame.transform.scale(pygame.image.load('PlayerBack1.png').convert_alpha(), (settings.p_length, settings.p_length)),
               pygame.transform.scale(pygame.image.load('PlayerBack.png').convert_alpha(), (settings.p_length, settings.p_length)),
               pygame.transform.flip(pygame.transform.scale(pygame.image.load('PlayerBack1.png').convert_alpha(), (settings.p_length, settings.p_length)), True, False),
               pygame.transform.scale(pygame.image.load('PlayerBack.png').convert_alpha(), (settings.p_length, settings.p_length)),],
               [pygame.transform.scale(pygame.image.load('Jump.png').convert_alpha(), (settings.p_length, settings.p_length)),
               pygame.transform.scale(pygame.image.load('Jump.png').convert_alpha(), (settings.p_length, settings.p_length)),
               pygame.transform.scale(pygame.image.load('Jump.png').convert_alpha(), (settings.p_length, settings.p_length)),
               pygame.transform.scale(pygame.image.load('Jump.png').convert_alpha(), (settings.p_length, settings.p_length)),],
               [pygame.transform.flip(pygame.transform.scale(pygame.image.load('Jump.png').convert_alpha(), (settings.p_length, settings.p_length)), True, False),
               pygame.transform.flip(pygame.transform.scale(pygame.image.load('Jump.png').convert_alpha(), (settings.p_length, settings.p_length)), True, False),
               pygame.transform.flip(pygame.transform.scale(pygame.image.load('Jump.png').convert_alpha(), (settings.p_length, settings.p_length)), True, False),
               pygame.transform.flip(pygame.transform.scale(pygame.image.load('Jump.png').convert_alpha(), (settings.p_length, settings.p_length)), True, False)]
               ]