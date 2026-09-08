import pygame

class Hazard:

    def __init__(self, image_path, x, y, type):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x, y))
        self.type = type