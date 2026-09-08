import pygame
from player import Player
from block import Block
from hazard import Hazard
from level import Level

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fireboy and Watergirl")

clock = pygame.time.Clock()

level = Level("levels/level1.json")

fireboy = Player("assets/fireboy.png", 0, 0, "fire")
fireboy.rect.bottomleft = (0, 580)
fireboy.x = fireboy.rect.left
fireboy.y = fireboy.rect.top
#block = Block("assets/block.png", 0, 0)
#block.rect.midbottom = (screen.get_width() // 2, screen.get_height())
#water = Hazard("assets/water.png", 0, 0, "water")
#water.rect.bottomright = block.rect.bottomleft

GRAVITY = 0.15
MAX_FALL_SPEED = 6
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
        fireboy.velocity_x = -2.5
    elif keys[pygame.K_RIGHT]:
        fireboy.velocity_x = 2.5
    else:
        fireboy.velocity_x = 0

    prev_rect = fireboy.rect.copy()
    fireboy.x += fireboy.velocity_x     # accumulate on the float, no truncation lost
    fireboy.y += fireboy.velocity_y     # accumulate on the float, no truncation lost

    fireboy.rect.left = round(fireboy.x)   # rect only used for drawing/collision
    fireboy.rect.top = round(fireboy.y)

    if fireboy.rect.left < 0:
        fireboy.rect.left = 0
        fireboy.x = fireboy.rect.left      # keep float in sync after clamping
    elif fireboy.rect.right > screen.get_width():
        fireboy.rect.right = screen.get_width()
        fireboy.x = fireboy.rect.left      # keep float in sync after clamping

    if fireboy.rect.bottom >= screen.get_height():
        fireboy.on_ground = True
        fireboy.rect.bottom = screen.get_height()
        fireboy.y = fireboy.rect.top      # keep float in sync after clamping
        fireboy.velocity_y = 0
    else:
        fireboy.velocity_y += GRAVITY

    for block in level.blocks:
        if fireboy.rect.colliderect(block.rect):
            if fireboy.velocity_y > 0 and prev_rect.bottom <= block.rect.top:
                fireboy.rect.bottom = block.rect.top 
                fireboy.y = fireboy.rect.top      # keep float in sync after clamping
                fireboy.velocity_y = 0
                fireboy.on_ground = True
            elif fireboy.velocity_y < 0 and prev_rect.top >= block.rect.bottom:
                fireboy.rect.top = block.rect.bottom
                fireboy.y = fireboy.rect.top      # keep float in sync after clamping
                fireboy.velocity_y = 0
            elif fireboy.velocity_x < 0 and prev_rect.left >= block.rect.right:
                fireboy.rect.left = block.rect.right
                fireboy.x = fireboy.rect.left      # keep float in sync after clamping
            elif fireboy.velocity_x > 0 and prev_rect.right <= block.rect.left:
                fireboy.rect.right = block.rect.left
                fireboy.x = fireboy.rect.left      # keep float in sync after clamping

    for hazard in level.hazards:
        if fireboy.rect.colliderect(hazard.rect):
            if hazard.type != fireboy.element:
                fireboy.rect.bottomleft = (0, 580)
                fireboy.x = fireboy.rect.left
                fireboy.y = fireboy.rect.top
            else:
                if fireboy.velocity_y > 0:
                    fireboy.rect.bottom = hazard.rect.top 
                    fireboy.velocity_y = 0
                    fireboy.on_ground = True
                elif fireboy.velocity_x < 0:
                    fireboy.rect.left = hazard.rect.right
                elif fireboy.velocity_x > 0:
                    fireboy.rect.right = hazard.rect.left

    # Draw the background
    screen.fill((30, 30, 30))
    
    # Draw Fireboy
    screen.blit(fireboy.image, fireboy.rect)
    for block in level.blocks:
        screen.blit(block.image, block.rect)
    for hazard in level.hazards:
        screen.blit(hazard.image, hazard.rect)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

pygame.quit()