__author__ = 'sean'
import sys
import pygame
from pygame.locals import *

class GameController():
  def __init__(self):
    pass

  def update(self,game):
    for event in pygame.event.get():
      if (event.type == pygame.QUIT):
        sys.exit()
      if not hasattr(event,'key'):
        continue
      down = event.type == KEYDOWN
      if event.key == K_RIGHT:
        game.player.k_right = down * -5
      elif event.key == K_LEFT:
        game.player.k_left = down * 5
      elif event.key == K_UP:
        game.player.k_up = down * 2
      elif event.key == K_DOWN:
        game.player.k_down = down * -2
      elif event.key == K_ESCAPE:
        sys.exit(0)
    game.block_group.update()

    non_passable_blocks = []
    for sprite in game.block_group:
      if not sprite.passable:
        non_passable_blocks.append(sprite)
    non_passable_block_group = pygame.sprite.Group(non_passable_blocks)
    collisions = pygame.sprite.groupcollide(game.player_group,non_passable_block_group,False,True)
    game.player_group.update()