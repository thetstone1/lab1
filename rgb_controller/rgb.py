#!/usr/bin/python

import serial
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1366,768))
DISPLAYSURF.fill((255,255,255))
pygame.display.set_caption('Lab 1 Stone')
s = serial.Serial("/dev/ttyACM0")

while(True):
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    l = s.readline()
    x = l.rstrip().lstrip().split(",")
    rgb = [int(val) for val in x]
    print rgb
    DISPLAYSURF.fill(rgb)    
    pygame.display.update()


