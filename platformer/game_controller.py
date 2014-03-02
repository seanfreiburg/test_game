__author__ = 'sean'
import sys, pygame
from pygame.locals import *

class GameController():
  def __init__(self):
    pass

  def update(self,game):
    for event in pygame.event.get():
      if (event.type == pygame.QUIT):
        sys.exit()
      if not hasattr(event,'key'):
        continue
      down = event.type == KEYDOWN
      if event.key == K_RIGHT:
        game.player.k_right = down * -5
      elif event.key == K_LEFT:
        game.player.k_left = down * 5
      elif event.key == K_UP:
        game.player.k_up = down * 2
      elif event.key == K_DOWN:
        game.player.k_down = down * -2
      elif event.key == K_ESCAPE:
        sys.exit(0)