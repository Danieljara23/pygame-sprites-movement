import pygame
from config import GRAVITY, SCREEN_HEIGHT, JUMP_STRENGTH

class AnimatedSprite(pygame.sprite.Sprite):
  def __init__(self, images, x, y, animation_speed):
    super().__init__()
    self.images = images
    self.image = self.images[0]
    self.rect = self.image.get_rect(center=(x, y))
    self.animation_speed = animation_speed
    self.current_time = 0
    self.index = 0
    self.animate = False
    self.facing_left = False
    self.velocity_y = 0
    self.on_ground = False

  def update(self):
    self.velocity_y += GRAVITY
    self.rect.y += self.velocity_y

    # Detener el sprite al tocar el suelo
    if self.rect.bottom >= SCREEN_HEIGHT:
      self.rect.bottom = SCREEN_HEIGHT
      self.velocity_y = 0
      self.on_ground = True
    else:
      self.on_ground = False

    if self.animate:
      self.current_time += self.animation_speed
      if self.current_time >= 1:
        self.current_time = 0
        self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]

        if self.facing_left:
          self.image = pygame.transform.flip(self.image, True, False)

  def move(self, dx):
      self.rect.x += dx

  def jump(self):
    if self.on_ground:
      self.velocity_y = JUMP_STRENGTH
      self.on_ground = False
