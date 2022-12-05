import pygame
from pygame import Vector2
from content.space_obj import SpaceObj
from content.obj_msg import ObjMsg


class Bullet(SpaceObj):
    """子弹"""
    # TODO:添加子弹拖尾特效

    COLOR = (0, 0, 0)
    next_id = 0

    def __init__(self, settings,
                 loc0: Vector2 = Vector2(0, 0), spd0: Vector2 = Vector2(0, 0)):
        super().__init__(settings, 1*loc0, 1*spd0)
        self.radius = settings.bullet_radius  # 子弹半径
        self.damage = settings.bullet_damage  # 子弹伤害
        self.id = Bullet.next_id
        Bullet.next_id += 1

    @staticmethod
    def init(settings):
        Bullet.COLOR = settings.bullet_color

    def __get_image__(self, settings):
        return settings.bullet_image

    def display(self, camera):
        super().display(camera)
        camera.draw_dot(Vector2(self.rect.center), Bullet.COLOR)

    def get_e_d_m(self, planets, center_v: Vector2):
        """获取机械能和质量的比值"""
        ekdm = self.get_ek_d_m(center_v)
        epdm = self.get_ep_d_m(planets)
        return ekdm + epdm

    def check_del(self, planets, ships, center_v: Vector2, max_dis: float) -> bool:
        """检查是否需要删除"""
        min_dis = 0  # 所有距离中最小的
        for objs in planets, ships:
            for obj in objs:
                dis = (self.loc-obj.loc).length()  # 这个距离
                if (self.spd-obj.spd)*(obj.loc-self.loc) > 0:  # 如果还在向星球/飞船飞则不删除
                    return False
                if dis < min_dis or min_dis == 0:
                    min_dis = dis
        edm = self.get_e_d_m(planets, center_v)
        if edm > 0 and min_dis > max_dis\
                or edm > -1e-5 and min_dis > max_dis*2\
                or edm > -1e-2 and min_dis > max_dis*3\
                or min_dis > max_dis*4:
            return True
        return False

    def update_by_msg(self, msg: list, planets):
        super().update_by_msg(msg, planets)
        msg = ObjMsg(msg)
        self.id = msg.id
