__author__ = 'sean'
import pygame,math

class PlayerSprite(pygame.sprite.Sprite):
  TURN_SPEED = 5
  ACCELERATION = 2
  MAX_FORWARD_SPEED = 10
  MAX_REVERSE_SPEED = -5

  def __init__(self,image,position):
    pygame.sprite.Sprite.__init__(self)
    self.src_image = pygame.image.load(image)
    self.position = position
    self.speed = self.direction = 0
    self.k_left = self.k_right = self.k_up = self.k_down = 0

  def update(self):
    self.speed += (self.k_up + self.k_down)
    if self.speed > self.MAX_FORWARD_SPEED:
      self.speed = self.MAX_FORWARD_SPEED
    if self.speed < self.MAX_REVERSE_SPEED:
      self.speed = self.MAX_REVERSE_SPEED
    self.direction += (self.k_right + self.k_left)
    x,y = self.position
    rad = self.direction *math.pi/180
    x += -self.speed*math.sin(rad)
    y += -self.speed*math.cos(rad)
    self.position = (x,y)

    self.image = pygame.transform.rotate(self.src_image,self.direction)
    self.rect = self.image.get_rect()
    self.rect.center = self.position

