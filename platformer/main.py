__author__ = 'sean'
import pygame,sys,math,json
from pygame.locals import *
from game import Game
from game_controller import GameController
from game_view import GameView

FRAMES_PER_SECOND = 30
clock = pygame.time.Clock()

game_controller = GameController()
game_view = GameView()
game = Game()
while 1:
  deltat = clock.tick(FRAMES_PER_SECOND)
  game_controller.update(game)
  game_view.update(game)

