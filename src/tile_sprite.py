__author__ = 'sean'
import pygame
from constants import Constants


class TileSprite(pygame.sprite.Sprite):
  def __init__(self, image, position, passable):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(pygame.image.load(image), (Constants.BLOCK_SIZE, Constants.BLOCK_SIZE))
    self.rect = self.image.get_rect()
    x,y = position
    self.position = (x * Constants.BLOCK_SIZE, y * Constants.BLOCK_SIZE)
    self.rect.topleft = self.position
    self.passable = passable

  def update(self):
    pass



