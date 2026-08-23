import pygame
from player import Player

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fireboy and Watergirl")

clock = pygame.time.Clock()

fireboy = Player("assets/fireboy.png", 0, 568, "fire")

GRAVITY = 0.5
MAX_FALL_SPEED = 10
GROUND_Y = 600 - fireboy.rect.height

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and fireboy.on_ground:
                fireboy.velocity_y = fireboy.jump_strength
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
        fireboy.velocity_x = 0
    elif keys[pygame.K_LEFT]:
        fireboy.velocity_x = -5
    elif keys[pygame.K_RIGHT]:
        fireboy.velocity_x = 5
    else:
        fireboy.velocity_x = 0

    fireboy.x += fireboy.velocity_x
    fireboy.y += fireboy.velocity_y

    if fireboy.y >= GROUND_Y:
        fireboy.on_ground = True
        fireboy.y = GROUND_Y
        fireboy.velocity_y = 0
    else:
        fireboy.on_ground = False
        fireboy.velocity_y += GRAVITY

    # Draw the background
    screen.fill((30, 30, 30))
    
    # Draw Fireboy
    screen.blit(fireboy.image, (fireboy.x, fireboy.y))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

pygame.quit()