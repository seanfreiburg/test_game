__author__ = 'sean'
import sys
import pygame
from pygame.locals import *
from bullet_sprite import BulletSprite


class GameController():
  def __init__(self):
    self.up = self.down = self.left = self.right = self.running = False

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
        game.bullet_group.add(BulletSprite(game.camera.apply(game.player), pygame.mouse.get_pos()))

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
      if e.type == KEYDOWN and e.key == K_ESCAPE:
        sys.exit(0)

    game.camera.update(game.player)
    game.player.update(self.up, self.down, self.left, self.right, self.running, game.tile_group)
    for bullet in game.bullet_group:
      if not Rect(0, 0, game.total_level_width, game.total_level_height).contains(bullet.rect):
        game.bullet_group.remove(bullet)
      else:
        bullet.update()
    game.bullet_group.update()
    game.tile_group.update()
