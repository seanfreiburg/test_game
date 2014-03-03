__author__ = 'sean'
from colors import Colors
from box_sprite import BoxSprite
from player_sprite import PlayerSprite
import json
import pygame


class Game():
  PLAYER_IMAGE = 'car.png'
  PLAYER_START_LOCATION = (100,100)
  MAP_FILE = 'map.txt'

  def __init__(self):
    self.map = self.load_map(self.MAP_FILE)
    self.player = PlayerSprite(self.PLAYER_IMAGE, self.PLAYER_START_LOCATION )
    self.player_group = pygame.sprite.Group(self.player)

  def load_map(self,map):
    # Load map
    f = open(map, 'r')
    contents = f.read()
    f.close()
    map_array = json.loads(contents)['map']
    blocks = []
    y = 0
    for row in map_array:
      x = 0
      for entry in row:
        if entry == 0:
          color = Colors.RED
          passable = True
        elif entry == 1:
          color = Colors.BLUE
          passable = True
        elif entry == 2:
          color = Colors.GREEN
          passable = False
        else:
          color = Colors.BLACK
          passable = True
        # add on a new sprite at x*box_size, y*box_size
        block = BoxSprite(color, (x, y), passable)
        blocks.append(block)
        x += 1
      y += 1

    self.block_group = pygame.sprite.Group(*blocks)