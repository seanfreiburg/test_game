__author__ = 'sean'
import pygame,sys,math
from car_sprite import CarSprite
from pad_sprite import PadSprite
from pygame.locals import *
HEIGHT = 768
WIDTH = 1024
BLACK = (0,0,0)
FRAMES_PER_SECOND = 30
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

pads = [PadSprite((200,200)), PadSprite((800,200)), PadSprite((200,600)),
        PadSprite((800,600)),]
pad_group = pygame.sprite.RenderPlain(*pads)

rect = screen.get_rect()
car = CarSprite('car.png', rect.center)
car_group = pygame.sprite.RenderPlain(car)

background = pygame.image.load('track.png')
background = pygame.transform.scale(background,(WIDTH,HEIGHT))
screen.blit(background,(0,0))

while 1:
  deltat = clock.tick(FRAMES_PER_SECOND)
  for event in pygame.event.get():
    if(event.type == pygame.QUIT):
      sys.exit()

    if not hasattr(event,'key'):
      continue
    down = event.type == KEYDOWN
    if event.key == K_RIGHT:
      car.k_right = down * -5
    elif event.key == K_LEFT:
      car.k_left = down * 5
    elif event.key == K_UP:
      car.k_up = down * 2
    elif event.key == K_DOWN:
      car.k_down = down * -2
    elif event.key == K_ESCAPE:
      sys.exit(0)
  pad_group.clear(screen,background)
  car_group.clear(screen,background)

  car_group.update(deltat)

  collisions = pygame.sprite.groupcollide(car_group,pad_group,False,False)
  pad_group.update(collisions)
  pad_group.draw(screen)
  car_group.draw(screen)

  pygame.display.flip()