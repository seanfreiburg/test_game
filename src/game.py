__author__ = 'sean'
import json
import sys

import pygame

from player_sprite import PlayerSprite
from tile_sprite import TileSprite
from constants import Constants
from camera import Camera


class Game():
  PLAYER_IMAGE = 'red.png'
  MAP_FILE = 'map.txt'

  def __init__(self):
    self.map = self.load_map(self.MAP_FILE)
    self.player = PlayerSprite(self.PLAYER_IMAGE, self.player_start_position, self.map_bounds)
    self.player_group = pygame.sprite.Group(self.player)

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
        elif entry == 1:
          image = 'water.png'
          passable = True
        elif entry == 2:
          image = 'lava.png'
          passable = False
        elif entry == 3:
          image = 'dirt.png'
          passable = True
        else:
          print("map file corrupted")
          sys.exit(1)
        # add on a new sprite at x*box_size, y*box_size
        block = TileSprite(image, (x, y), passable)
        blocks.append(block)
        x += 1
      y += 1

    total_level_width = len(map_array[0]) * Constants.BLOCK_SIZE  # calculate size of level in pixels
    total_level_height = len(map_array) * Constants.BLOCK_SIZE  # maybe make 32 an constant
    self.camera = Camera(Camera.complex_camera, total_level_width, total_level_height)

    self.tile_group = pygame.sprite.Group(*blocks)
    self.player_start_position = (
    Constants.BLOCK_SIZE * json_contents['start'][0], Constants.BLOCK_SIZE * json_contents['start'][1])
    self.map_bounds = (Constants.BLOCK_SIZE * len(map_array[0]), Constants.BLOCK_SIZE * len(map_array))




