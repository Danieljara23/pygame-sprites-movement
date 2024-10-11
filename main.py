import pygame
from config import *
from sprite import Sprite

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spritesheets")

clock = pygame.time.Clock()

run = True
while run:
  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
     # update background
  screen.fill(CUSTOM_COLOR)
  
  pygame.display.update()

  clock.tick(60)

pygame.quit()
