import pygame

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


  def update(self):
    if self.animate:
      self.current_time += self.animation_speed
      if self.current_time >= 1:
        self.current_time = 0
        self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]

        if self.facing_left:
          self.image = pygame.transform.flip(self.image, True, False)

  def move(self, dx, dy):
      self.rect.x += dx
      self.rect.y += dy

