__author__ = 'sean'
import pygame

from game import Game
from game_controller import GameController
from game_view import GameView
from constants import Constants

clock = pygame.time.Clock()

game_controller = GameController()
game_view = GameView()
game = Game()
while 1:
  deltat = clock.tick(Constants.FRAMES_PER_SECOND)
  game_controller.update(game)
  game_view.update(game)

