import pygame

class Player:

    def __init__(self, image_path, x, y, element):
        self.image = pygame.image.load(image_path).convert_alpha()

        self.x = x
        self.y = y
        self.element = element

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity_x = 0
        self.velocity_y = 0

        self.jump_strength = -10
        self.on_ground = True