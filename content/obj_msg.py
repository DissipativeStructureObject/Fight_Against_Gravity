"""传输的太空对象信息"""


class ObjMsg:
    """传输的太空对象信息"""
    def __init__(self, obj=None, obj_msg=None):
        """
        obj:SpaceObj 各类太空对象，从太空对象中获取数据
        msg:list 传输的消息，从消息中获取数据
        """
        if obj:
            self.locx = obj.loc.x
            self.locy = obj.loc.y
            self.spdx = obj.spd.x
            self.spdy = obj.spd.y
            self.accx = obj.acc.x
            self.accy = obj.acc.y
            try:  # 如果是飞船
                self.angle = obj.angle
                self.player_name = obj.player_name
            except AttributeError as e:
                pass

        elif obj_msg:
            self.locx = obj_msg[0]
            self.locy = obj_msg[1]
            self.spdx = obj_msg[2]
            self.spdy = obj_msg[3]
            self.accx = obj_msg[4]
            self.accy = obj_msg[5]
            try:  # 如果是飞船消息
                self.angle = obj_msg[6]
                self.player_name = obj_msg[7]
            except IndexError as e:
                pass

    def make_msg(self):
        """生成用于传输的消息"""
        msg = [
            self.locx, self.locy,
            self.spdx, self.spdy,
            self.accx, self.accy
        ]
        try:
            msg.append(self.angle)
            msg.append(self.player_name)
        except AttributeError as e:
            pass
        finally:
            return msg


if __name__ == '__main__':
    msg = [0, 1, 2, 3, 4, 5]
    obj_msg = ObjMsg(obj_msg=msg)
    print(obj_msg)