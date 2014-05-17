__author__ = 'sean'
import pygame, math
from constants import Constants


class BulletSprite(pygame.sprite.Sprite):
  VELOCITY = 10
  BULLET_IMAGE = 'bullet.png'
  BULLET_SIZE = 16

  def __init__(self, position, target):
    pygame.sprite.Sprite.__init__(self)

    x_side, y_side = target[0] - position[0], target[1] - position[1]
    hypotenus = math.sqrt(x_side ** 2 + y_side ** 2)
    self.xvel = self.VELOCITY * (x_side / hypotenus)
    self.yvel = self.VELOCITY * (y_side / hypotenus)

    self.image = pygame.transform.scale(pygame.image.load(self.BULLET_IMAGE), (self.BULLET_SIZE, self.BULLET_SIZE))
    self.rect = self.image.get_rect()
    x, y, _, _ = position
    self.position = (x, y )
    self.rect.topleft = self.position


  def update(self):
    self.rect.left += self.xvel
    self.rect.top += self.yvel