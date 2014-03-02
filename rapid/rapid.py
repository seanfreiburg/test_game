__author__ = 'sean'
import pygame,sys,math
from pygame.locals import *
HEIGHT = 768
WIDTH = 1024
screen = pygame.display.set_mode((WIDTH,HEIGHT))
car = pygame.image.load('car.png')
car = pygame.transform.rotate(car,-90)
clock = pygame.time.Clock()
k_up = k_down = k_left = k_right = 0
speed = direction = 0
position = (100,100)
TURN_SPEED = 5
ACCELERATION = 2
MAX_FORWARD_SPEED = 10
MAX_REVERSE_SPEED = -5
BLACK = (0,0,0)



FRAMES_PER_SECOND = 30

while 1:
  clock.tick(FRAMES_PER_SECOND)
  for event in pygame.event.get():
    if(event.type == pygame.QUIT):
      sys.exit()

    if not hasattr(event,'key'):
      continue
    down = event.type == KEYDOWN
    if event.key == K_RIGHT:
      k_right = down * -5
    elif event.key == K_LEFT:
      k_left = down * 5
    elif event.key == K_UP:
      k_up = down * 2
    elif event.key == K_DOWN:
      k_down = down * -2
    elif event.key == K_ESCAPE:
      sys.exit(0)
  screen.fill(BLACK)

  speed += (k_up + k_down)
  if speed > MAX_FORWARD_SPEED:
    speed = MAX_FORWARD_SPEED
  if speed < MAX_REVERSE_SPEED:
    speed = MAX_REVERSE_SPEED
  direction += (k_right + k_left)
  x,y = position
  rad = direction *math.pi/180
  x += -speed*math.sin(rad)
  y += -speed*math.cos(rad)
  position = (x,y)

  rotated = pygame.transform.rotate(car,direction)
  rect = rotated.get_rect()
  rect.center = position
  screen.blit(rotated,rect)
  pygame.display.flip()







  pygame.display.flip()