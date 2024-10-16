
import pygame
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, spritesheet, num_frames, x, y, animation_speed):
        super().__init__()
        self.images = self.load_images_from_spritesheet(spritesheet, num_frames)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(x, y))
        self.animation_speed = animation_speed
        self.current_time = 0
        self.index = 0
        self.animate = False
        self.facing_left = False

    def load_images_from_spritesheet(self, spritesheet, num_frames):
        sheet_width = spritesheet.get_width()
        sheet_height = spritesheet.get_height()
        frame_width = sheet_width // num_frames
        images = []

        for i in range(num_frames):
            frame = spritesheet.subsurface((i * frame_width, 0, frame_width, sheet_height))
            images.append(frame)

        return images

    def update(self):
        # Actualizar la animación
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
