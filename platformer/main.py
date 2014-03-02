__author__ = 'sean'
import pygame,sys,math,json
from pygame.locals import *
from box_sprite import *
HEIGHT = 768
WIDTH = 1024
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
BOX_SIZE  = 32
FRAMES_PER_SECOND = 30
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
rect = screen.get_rect()

# Load map
f = open('map.txt', 'r')
contents = f.read()
f.close()
map_array = json.loads(contents)['map']
# Draw map
blocks = []
y = 0
for row in map_array:
  x =0
  for entry in row:
    if entry == 0:
      color = RED
    elif entry == 1:
      color = BLUE
    else:
      color = BLACK
    # add on a new sprite at x*box_size, y*box_size
    block = BoxSprite(color,(x,y))
    blocks.append(block)
    x += 1
  y += 1

block_group = pygame.sprite.Group(*blocks)
while 1:
  deltat = clock.tick(FRAMES_PER_SECOND)
  for event in pygame.event.get():
    if(event.type == pygame.QUIT):
      sys.exit()
  screen.fill(WHITE)
  block_group.draw(screen)

  pygame.display.flip()