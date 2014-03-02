__author__ = 'sean'
import pygame
class PadSprite(pygame.sprite.Sprite):
  normal = pygame.image.load('pad_normal.png')
  hit = pygame.image.load('pad_hit.png')
  def __init__(self,position):
    pygame.sprite.Sprite.__init__(self)
    self.rect = pygame.Rect(self.normal.get_rect())
    self.rect.center = position
    self.image = self.normal

  def update(self,hit_list):
    for key in hit_list:
      if self in hit_list[key]:
        self.image = self.hit
      else:
        self.image = self.normal