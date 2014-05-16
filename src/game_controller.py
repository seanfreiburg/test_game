__author__ = 'sean'
import sys
import pygame
from pygame.locals import *


class GameController():
  def __init__(self):
    self.up = self.down = self.left = self.right = self.running = False

  def update(self, game):

    for e in pygame.event.get():
      if (e.type == pygame.QUIT):
        sys.exit()
      if not hasattr(e, 'key'):
        continue
      if e.type == KEYDOWN and e.key == K_UP:
        self.up = True
      if e.type == KEYDOWN and e.key == K_DOWN:
        self.down = True
      if e.type == KEYDOWN and e.key == K_LEFT:
        self.left = True
      if e.type == KEYDOWN and e.key == K_RIGHT:
        self.right = True
      if e.type == KEYDOWN and e.key == K_SPACE:
        self.running = True

      if e.type == KEYUP and e.key == K_UP:
        self.up = False
      if e.type == KEYUP and e.key == K_DOWN:
        self.down = False
      if e.type == KEYUP and e.key == K_RIGHT:
        self.right = False
      if e.type == KEYUP and e.key == K_LEFT:
        self.left = False
      if e.type == KEYUP and e.key == K_SPACE:
        self.running = False
      if e.type == KEYDOWN and e.key == K_ESCAPE:
        sys.exit(0)

    game.camera.update(game.player)
    game.player.update(self.up, self.down, self.left, self.right, self.running, game.tile_group)

    game.tile_group.update()
