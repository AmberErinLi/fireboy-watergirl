import pygame

class Player:

    def __init__(self, image_path, x, y, element):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.element = element
        self.rect = self.image.get_rect(topleft = (x, y))

        self.x = float(self.rect.left)     # <-- true sub-pixel position
        self.y = float(self.rect.top)      # <-- true sub-pixel position

        self.velocity_x = 0
        self.velocity_y = 0

        self.jump_strength = -4
        self.on_ground = True