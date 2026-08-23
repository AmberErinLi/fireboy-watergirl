import pygame
from player import Player
from block import Block

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fireboy and Watergirl")

clock = pygame.time.Clock()

fireboy = Player("assets/fireboy.png", 0, 0, "fire")
fireboy.rect.bottomleft = (0, 600)
block = Block("assets/block.png", 0, 0)
block.rect.midbottom = (screen.get_width() // 2, screen.get_height())

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
                fireboy.on_ground = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
        fireboy.velocity_x = 0
    elif keys[pygame.K_LEFT]:
        fireboy.velocity_x = -5
    elif keys[pygame.K_RIGHT]:
        fireboy.velocity_x = 5
    else:
        fireboy.velocity_x = 0

    fireboy.rect.left += fireboy.velocity_x
    fireboy.rect.top += fireboy.velocity_y

    if fireboy.rect.left < 0:
        fireboy.rect.left = 0
    elif fireboy.rect.right > screen.get_width():
        fireboy.rect.right = screen.get_width()

    if fireboy.rect.bottom >= screen.get_height():
        fireboy.on_ground = True
        fireboy.rect.bottom = screen.get_height()
        fireboy.velocity_y = 0
    else:
        fireboy.velocity_y += GRAVITY

    if fireboy.rect.colliderect(block.rect):
        if fireboy.velocity_y > 0:
            fireboy.rect.bottom = block.rect.top 
            fireboy.velocity_y = 0
            fireboy.on_ground = True

    # Draw the background
    screen.fill((30, 30, 30))
    
    # Draw Fireboy
    screen.blit(fireboy.image, fireboy.rect)
    screen.blit(block.image, block.rect)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

pygame.quit()