from scene_class import Scene
from button_class import Button
from inputbox_class import InputBox
from label_class import Label
from scene_font import SceneFont
from scene_player_class import ScenePlayer
from panel_class import Panel
from Web import identify_client as ic
import os
import sys
import pygame


class LocalGameScene(Scene):
    def __init__(self, setting):
        super().__init__(setting)
        self.pause_panel = Panel((200, 300, 800, 200), '单击此处继续', 23, self.cancel_pause_clicked)
        pause_rect = pygame.Rect(950, 675, 50, 50)
        pause_button = Button('pause', self.pause_is_clicked, pause_rect, 'UI/Img/pause.png', 0)
        pause_button.add_img('UI/Img/pause_pressed.png')
        self.loaded = {'img': None, 'label': None, 'box': None, 'button': [pause_button], 'panel': []}

    def pause_is_clicked(self):
        self.loaded['panel'] = [self.pause_panel]

    def cancel_pause_clicked(self):
        self.loaded['panel'] = []

    def show(self, screen):
        screen.fill((10, 10, 10))
        self.draw_elements(screen)
        pygame.display.flip()
