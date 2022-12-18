import pygame
import visual

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
        visual.rotate_image(self.screen, self.image, 200, 345)
