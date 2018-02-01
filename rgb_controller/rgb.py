#!/usr/bin/python

import serial
import pygame, sys
import time
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1366,768))
DISPLAYSURF.fill((255,255,255))
pygame.display.set_caption('Lab 1 Stone')
s = serial.Serial("/dev/ttyACM0")

def main():
  while(True):
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      l = s.readline()
      x = l.rstrip().lstrip().split(",")
      try:
        rgb = [int(val) for val in x]
        DISPLAYSURF.fill(rgb)    
        pygame.display.update()
        print rgb
      except ValueError:
        pass
     

main()


