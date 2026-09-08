import json
import pygame
from block import Block
from hazard import Hazard

class Level:

    def __init__(self, level_path):
        with open(level_path, "r") as file:
            data = json.load(file)

        self.blocks = []
        self.hazards = []

        for x, y in data["blocks"]:
            block = Block("assets/block.png", x, y)
            self.blocks.append(block)

        for hazard_type in data["hazards"]:
            image_path = "assets/" + hazard_type + ".png"
            for x, y in data["hazards"][hazard_type]:
                hazard = Hazard(image_path, x, y, hazard_type)
                self.hazards.append(hazard)