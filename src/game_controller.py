__author__ = 'sean'
import sys
import pygame
from pygame.locals import *
from bullet_sprite import BulletSprite


class GameController():
  def __init__(self):
    self.up = self.down = self.left = self.right = self.running = self.shooting = False

  def update(self, game):

    for e in pygame.event.get():
      if (e.type == pygame.QUIT):
        sys.exit()
      if e.type == KEYDOWN and (e.key == K_UP or e.key == K_w):
        self.up = True
      if e.type == KEYDOWN and (e.key == K_DOWN or e.key == K_s):
        self.down = True
      if e.type == KEYDOWN and (e.key == K_LEFT or e.key == K_a):
        self.left = True
      if e.type == KEYDOWN and (e.key == K_RIGHT or e.key == K_d):
        self.right = True
      if e.type == KEYDOWN and e.key == K_SPACE:
        self.running = True
      if e.type == MOUSEBUTTONDOWN:
        self.shooting = True

      if e.type == KEYUP and (e.key == K_UP or e.key == K_w):
        self.up = False
      if e.type == KEYUP and (e.key == K_DOWN or e.key == K_s):
        self.down = False
      if e.type == KEYUP and (e.key == K_RIGHT or e.key == K_d):
        self.right = False
      if e.type == KEYUP and (e.key == K_LEFT or e.key == K_a):
        self.left = False
      if e.type == KEYUP and e.key == K_SPACE:
        self.running = False
      if e.type == MOUSEBUTTONUP:
        self.shooting = False
      if e.type == KEYDOWN and e.key == K_ESCAPE:
        sys.exit(0)

    if self.shooting:
      game.add_bullet()
    game.camera.update(game.player)
    game.player.update(self.up, self.down, self.left, self.right, self.running, game.tile_group)
    game.update_bullets()
    game.tile_group.update()
    game.cursor.update()
