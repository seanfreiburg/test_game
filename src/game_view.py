__author__ = 'sean'
import pygame

from src.colors import Colors
from constants import Constants


class GameView():
  def __init__(self):
    self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    pygame.mouse.set_visible(False)
    self.screen.fill(Colors.WHITE)

  def update(self, game):
    dirty = []
    for tile in game.tile_group:
      move_rect = game.camera.apply(tile)
      if game.camera.state.contains(move_rect):
        dirty.append(self.screen.blit(tile.image, move_rect))
    dirty.append(self.screen.blit(game.player.image, game.camera.apply(game.player)))

    dirty.append(game.bullet_group.draw(self.screen))
    dirty.append(self.screen.blit(game.cursor.image, game.cursor.position))
    pygame.display.update()