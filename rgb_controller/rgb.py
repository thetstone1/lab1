#!/usr/bin/python

import serial
import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400,400))
pygame.display.set_caption('Lab 1 Stone')
s = serial.Serial("/dev/ttyACM0")

def main():
  while(True):
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    try:
      l = s.readline()
      x = l.rstrip().split(",")
      color_r = int(x[0])
      color_g = int(x[1])
      color_b = int(x[2])
      DISPLAYSURF.fill((color_r,color_g,color_b))    
      pygame.display.update()
    except ValueError:
      pass
main()


