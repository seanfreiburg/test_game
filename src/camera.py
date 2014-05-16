import pygame
from constants import Constants


class Camera(object):
  def __init__(self, camera_func, width, height):
    self.camera_func = camera_func
    self.state = pygame.Rect(0, 0, width, height)

  def apply(self, target):
    return target.rect.move(self.state.topleft)

  def update(self, target):
    self.state = self.camera_func(self.state, target.rect)

  def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect  # l = left,  t = top
    _, _, w, h = camera  # w = width, h = height
    HALF_WIDTH = Constants.SCREEN_WIDTH / 2
    HALF_HEIGHT = Constants.SCREEN_HEIGHT / 2
    return pygame.Rect(-l + HALF_WIDTH, -t + HALF_HEIGHT, w, h)

  def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    HALF_WIDTH = int(Constants.SCREEN_WIDTH / 2)
    HALF_HEIGHT = int(Constants.SCREEN_HEIGHT / 2)
    l, t, _, _ = -l + HALF_WIDTH, -t + HALF_HEIGHT, w, h  # center player

    l = min(0, l)  # stop scrolling at the left edge
    l = max(-(camera.width - Constants.SCREEN_WIDTH), l)  # stop scrolling at the right edge
    t = max(-(camera.height - Constants.SCREEN_HEIGHT), t)  # stop scrolling at the bottom
    t = min(0, t)  # stop scrolling at the top

    return pygame.Rect(l, t, w, h)