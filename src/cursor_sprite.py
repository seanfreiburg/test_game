__author__ = 'sean'
import pygame
from constants import Constants


class CursorSprite(pygame.sprite.Sprite):
  CURSOR_SIZE = (16, 16)

  def __init__(self, image):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(pygame.image.load(image), self.CURSOR_SIZE)
    self.rect = self.image.get_rect()
    x, y = pygame.mouse.get_pos()
    self.position = (x, y)
    self.rect.center = self.position

  def update(self):
    self.rect.center = pygame.mouse.get_pos()
    self.position = pygame.mouse.get_pos()