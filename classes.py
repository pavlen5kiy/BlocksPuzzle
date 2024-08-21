from ursina import *

from settings import *

class Player(Entity):
    def update(self):
        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a']) * 0
        ).normalized()

        origin = self.world_position
        hit_info = boxcast(origin, self.direction, ignore=(self,),
                           distance=.55, debug=False, thickness=(1, 1))
        if not hit_info.hit:
            self.position += self.direction * SPEED * time.dt


class ZMovableObst(Entity):
    def update(self):
        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s']) * 0
            + self.right * (held_keys['d'] - held_keys['a'])
        ).normalized()

        origin = self.world_position
        hit_info = boxcast(origin, self.direction, ignore=(self,),
                           distance=0.55 * self.scale_x, debug=False,
                           thickness=(1 * self.scale_z, 1))
        if not hit_info.hit:
            self.position += self.direction * SPEED * time.dt


class XMovableObst(Entity):
    def update(self):
        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a']) * 0
        ).normalized()

        origin = self.world_position
        hit_info = boxcast(origin, self.direction, ignore=(self,),
                           distance=0.55 * self.scale_z, debug=False,
                           thickness=(1 * self.scale_x, 1))
        if not hit_info.hit:
            self.position += self.direction * SPEED * time.dt


class StaticObst(Entity):
    pass
