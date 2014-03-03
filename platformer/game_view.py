__author__ = 'sean'
import pygame
from colors import Colors

class GameView():
  HEIGHT = 768
  WIDTH = 1024


  def __init__(self):
    self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))

  def update(self,game):
    self.screen.fill(Colors.WHITE)
    game.block_group.draw(self.screen)
    game.player_group.draw(self.screen)
    pygame.display.flip()