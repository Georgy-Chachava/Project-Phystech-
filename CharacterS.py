import pygame

class Character():
    """класс, описывающий персонажей"""
    def __init__(self, screen, image, replics, **kwargs):
        """инициализация Персонажа"""
        self.screen = screen
        self.image = image
        self.replics = replics
        self.name = kwargs.get('name')

    def output(self):
        """рисование персонажа"""
        rect = self.image.get_rect(center=(200, 345))
        self.screen.blit(self.image, rect)
