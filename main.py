import pygame
import sys
from sprite import AnimatedSprite

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Movimiento de Personaje")

# Configurar el reloj
clock = pygame.time.Clock()



def main():
    # Cargar las imágenes del sprite
    # Cargar el spritesheet
    spritesheet = pygame.image.load('assets/Goblin/Run.png').convert_alpha()

    # Crear una instancia del sprite
    num_frames = 8  # Número de frames en el spritesheet
    sprite = AnimatedSprite(spritesheet, num_frames, screen_width // 2, screen_height // 2, 0.1)

    
    # Crear un grupo de sprites
    all_sprites = pygame.sprite.Group()
    all_sprites.add(sprite)

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Obtener las teclas presionadas
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0

        # Mover el sprite según las teclas presionadas
        if keys[pygame.K_LEFT]:
            dx = -5
            sprite.animate = True
            sprite.facing_left = True
        if keys[pygame.K_RIGHT]:
            dx = 5
            sprite.animate = True
            sprite.facing_left = False
        if keys[pygame.K_UP]:
            dy = -5
            sprite.animate = True
        if keys[pygame.K_DOWN]:
            dy = 5
            sprite.animate = True

        # Si no se presiona ninguna tecla, detener la animación
        if dx == 0 and dy == 0:
            sprite.animate = False

        # Mover el sprite
        sprite.move(dx, dy)

        # Actualizar todos los sprites
        all_sprites.update()

        # Dibujar todo
        screen.fill((0, 0, 0))  # Limpiar la pantalla con color negro
        all_sprites.draw(screen)
        pygame.display.flip()

        # Limitar a 60 FPS
        clock.tick(60)

    # Salir de Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
