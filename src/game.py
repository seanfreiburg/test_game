__author__ = 'sean'
import json
import sys

import pygame

from player_sprite import PlayerSprite
from tile_sprite import TileSprite
from constants import Constants
from camera import Camera
from bullet_sprite import BulletSprite
from cursor_sprite import CursorSprite


class Game():
  def __init__(self):
    self.map = self.load_map(Constants.MAP_FILE)
    self.player = PlayerSprite(Constants.PLAYER_IMAGES, self.player_start_position, self.map_bounds)
    self.bullet_group = pygame.sprite.Group()
    self.player_group = pygame.sprite.Group(self.player)
    self.cursor = CursorSprite(Constants.CURSOR_IMAGE)

  def load_map(self, map):
    # Load map
    f = open(map, 'r')
    contents = f.read()
    f.close()
    json_contents = json.loads(contents)
    map_array = json_contents['map']
    blocks = []
    y = 0
    for row in map_array:
      x = 0
      for entry in row:
        if entry == 0:
          image = 'grass.png'
          passable = True
          destroyable = False
        elif entry == 1:
          image = 'water.png'
          passable = False
          destroyable = True
        elif entry == 2:
          image = 'lava.png'
          passable = False
          destroyable = False
        elif entry == 3:
          image = 'dirt.png'
          passable = True
          destroyable = False
        else:
          print("map file corrupted")
          sys.exit(1)
        # add on a new sprite at x*box_size, y*box_size
        block = TileSprite(Constants.IMAGE_PATH + image, (x * Constants.BLOCK_SIZE, y * Constants.BLOCK_SIZE), passable,
                           destroyable)
        blocks.append(block)
        x += 1
      y += 1

    self.total_level_width = len(map_array[0]) * Constants.BLOCK_SIZE  # calculate size of level in pixels
    self.total_level_height = len(map_array) * Constants.BLOCK_SIZE  # maybe make 32 an constant
    self.camera = Camera(Camera.complex_camera, self.total_level_width, self.total_level_height)

    self.tile_group = pygame.sprite.Group(*blocks)
    self.player_start_position = (
    Constants.BLOCK_SIZE * json_contents['start'][0], Constants.BLOCK_SIZE * json_contents['start'][1])
    self.map_bounds = (Constants.BLOCK_SIZE * len(map_array[0]), Constants.BLOCK_SIZE * len(map_array))


  def add_bullet(self):
    self.bullet_group.add(BulletSprite(self.camera.apply(self.player).center, pygame.mouse.get_pos()))

  def update_bullets(self):
    for bullet in self.bullet_group:
      if not pygame.Rect(0, 0, self.total_level_width, self.total_level_height).contains(bullet.rect):
        self.bullet_group.remove(bullet)
      else:
        bullet.update(self, self.tile_group)




