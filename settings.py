from ctypes.wintypes import PWIN32_FIND_DATAW
from re import I
import pygame

def init():
    global width, height, tSize, scale, size, p_width, p_length
    width = 1440 # my computer is 1440, normal is 1280
    height = 870 # my computer is 900, normal is 720
    scale = 16
    size = 4
    tSize = scale * size
    p_width = int(tSize / 4)
    p_length = int(tSize / 2)
    