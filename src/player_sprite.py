__author__ = 'sean'
import pygame, math
from constants import Constants


class PlayerSprite(pygame.sprite.Sprite):
  WALKING_VELOCITY = 12
  RUNNING_VELOCITY = 20

  def __init__(self, images, position, map_bounds):
    pygame.sprite.Sprite.__init__(self)
    self.images = images
    self.position = position
    self.rect = pygame.Rect(position[0], position[1], Constants.BLOCK_SIZE, Constants.BLOCK_SIZE)
    self.xvel = 0
    self.yvel = 0
    self.animation_state = 0
    self.set_image()

  def set_image(self):
    self.image = pygame.transform.scale(pygame.image.load(self.images[self.animation_state]),
                                        (Constants.BLOCK_SIZE, Constants.BLOCK_SIZE))


  def update(self, up, down, left, right, running, tiles):
    if not (left or right):
      self.xvel = 0

    if not (up or down):
      self.yvel = 0
      self.animation_state = 0

    if running:
      running_speed = self.RUNNING_VELOCITY
    else:
      running_speed = 0
    if up:
      self.yvel = -(self.WALKING_VELOCITY + running_speed)
      self.animation_state = (self.animation_state + 1) % len(self.images)
    if down:
      self.yvel = (self.WALKING_VELOCITY + running_speed)
      self.animation_state = (self.animation_state + 1) % len(self.images)

    if left:
      self.xvel = -(self.WALKING_VELOCITY + running_speed)
    if right:
      self.xvel = (self.WALKING_VELOCITY + running_speed)


    # increment in x direction
    self.rect.left += self.xvel
    # do x-axis collisions
    self.collide(self.xvel, 0, tiles)
    # increment in y direction
    self.rect.top += self.yvel
    # do y-axis collisions
    self.collide(0, self.yvel, tiles)
    self.set_image()
    self.position = self.rect.topleft

  def collide(self, xvel, yvel, tiles):
    for p in tiles:
      if (not p.passable) and pygame.sprite.collide_rect(self, p):
        if xvel > 0:
          self.rect.right = p.rect.left
        if xvel < 0:
          self.rect.left = p.rect.right
        if yvel > 0:
          self.rect.bottom = p.rect.top
        if yvel < 0:
          self.rect.top = p.rect.bottom


