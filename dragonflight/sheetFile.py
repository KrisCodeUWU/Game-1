import pygame


class Sheets():
    def __init__(self, image):
        self.sheet = image

    def getImage(self, frame, width, height, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image.set_colorkey(colour)
        return image
