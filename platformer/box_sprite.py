__author__ = 'sean'
import pygame
class BoxSprite(pygame.sprite.Sprite):
  BOX_SIZE  = 64

  def __init__(self,color,position,passable):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((self.BOX_SIZE,self.BOX_SIZE))
    self.image.fill(color)
    self.rect = self.image.get_rect()
    x,y = position
    self.position = (x*self.BOX_SIZE,y*self.BOX_SIZE)
    self.rect.topleft = self.position
    self.passable = passable

  def update(self):
    self.rect = self.image.get_rect()
    self.rect.topleft = self.position
