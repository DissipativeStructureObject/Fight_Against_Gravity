from content.UI.scene_class import Scene
from content.UI.button_class import Button
from content.UI.inputbox_class import InputBox
from content.UI.label_class import Label
from content.UI.scene_font import SceneFont
from content.UI.scene_player_class import ScenePlayer
from content.UI.register_scene_class import RegScene
from content.UI.menu_scene import MenuScene
from Server import identify_client as ic
import os
import pygame


class LogInScene(Scene):
    """加载登录界面组件, 对应页面状态1"""

    def __init__(self, setting):
        super().__init__(setting)
        # os.chdir(self.setting.fag_directory)
        id_label = Label(330, 250, 98, "账号(用户名)")
        password_label = Label(330, 350, 42, "密码")
        id_box = InputBox(pygame.Rect(450, 250, 350, 35))  # 输入框的宽不由传入参数决定。
        password_box = InputBox(pygame.Rect(450, 350, 350, 35), is_pw=1)
        boxL = [id_box, password_box]
        """注册按钮"""
        register_rect = pygame.Rect(600, 450, 180, 40)
        register_button = Button("register", self.register_is_clicked, register_rect,
                                 self.setting.btbg_light, 0, '没有账号?注册', SceneFont.log_font)
        register_button.add_img(self.setting.btbg_light_pressed)
        """登录按钮"""
        login_rect = pygame.Rect(450, 450, 70, 40)
        login_button = Button("login", self.login_is_clicked, login_rect,
                              self.setting.btbg_light, 0, "登录", SceneFont.log_font)
        login_button.add_img(self.setting.btbg_light_pressed)
        self.loaded = {'img': None, 'label': [id_label, password_label], 'box': boxL,
                       'button': [self.back, register_button, login_button],
                       'panel': None}

    def show(self, screen):
        screen.fill((10, 10, 10))
        pygame.draw.rect(screen, (46, 46, 46), (300, 150, 600, 400), border_radius=15)
        self.draw_elements(screen)
        pygame.display.flip()

    def register_is_clicked(self):
        ScenePlayer.push(RegScene(self.setting))

    def login_is_clicked(self):
        userid = self.loaded['box'][0].text
        userpw = self.loaded['box'][1].text
        identify_client = ic.createIdentifyClient()
        answer = identify_client.login(userid, userpw)
        if answer:
            print("登录成功")
            ScenePlayer.push(MenuScene(self.setting))
        else:
            print("failed")


