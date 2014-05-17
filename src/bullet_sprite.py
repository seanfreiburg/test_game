__author__ = 'sean'
import pygame, math
from constants import Constants
from tile_sprite import TileSprite


class BulletSprite(pygame.sprite.Sprite):
  VELOCITY = 20

  BULLET_SIZE = 16

  def __init__(self, position, target):
    pygame.sprite.Sprite.__init__(self)

    x_side, y_side = target[0] - position[0], target[1] - position[1]
    hypotenus = math.sqrt(x_side ** 2 + y_side ** 2)
    self.xvel = self.VELOCITY * (x_side / hypotenus)
    self.yvel = self.VELOCITY * (y_side / hypotenus)

    self.image = pygame.transform.scale(pygame.image.load(Constants.BULLET_IMAGE), (self.BULLET_SIZE, self.BULLET_SIZE))
    self.rect = self.image.get_rect()
    x, y = position
    self.position = (x, y )
    self.rect.topleft = self.position


  def update(self, game, tiles):
    self.rect.left += self.xvel
    self.rect.top += self.yvel
    self.collide(game, tiles)

  def collide(self, game, tiles):
    for p in tiles:
      if p.destroyable and pygame.sprite.collide_rect(self, p):
        tiles.remove(p)
        tiles.add(TileSprite(Constants.IMAGE_PATH + 'grass.png', p.rect.topleft, True, False))
        game.bullet_group.remove(self)
