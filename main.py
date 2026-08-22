import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fireboy and Watergirl")

clock = pygame.time.Clock()

# Load Fireboy's image
fireboy_image = pygame.image.load("assets/fireboy.png").convert_alpha()

# Set Fireboy's initial position and velocity
fireboy_x = 100
fireboy_y = 300
fireboy_velocity_x = 0
fireboy_velocity_y = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
        fireboy_velocity_x = 0
    elif keys[pygame.K_LEFT]:
        fireboy_velocity_x = -5
    elif keys[pygame.K_RIGHT]:
        fireboy_velocity_x = 5
    else:
        fireboy_velocity_x = 0
    

    fireboy_x += fireboy_velocity_x
    fireboy_y += fireboy_velocity_y

    # Draw the background
    screen.fill((30, 30, 30))
    
    # Draw Fireboy
    screen.blit(fireboy_image, (fireboy_x, fireboy_y))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

pygame.quit()