__author__ = 'sean'
import pygame

from src.colors import Colors
from constants import Constants


class GameView():
  def __init__(self):
    self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

  def update(self, game):
    self.screen.fill(Colors.WHITE)
    for tile in game.tile_group:
      move_rect = game.camera.apply(tile)
      if game.camera.state.contains(move_rect):
        self.screen.blit(tile.image, move_rect)
    self.screen.blit(game.player.image, game.camera.apply(game.player))
    pygame.display.flip()