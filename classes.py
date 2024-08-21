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
                           distance=0.75, debug=False, thickness=(BOXCAST_THICKNESS, BOXCAST_THICKNESS))
        if not hit_info.hit:
            self.position += self.direction * SPEED * time.dt


# blue blocks move along x axis
class BlueBlock(Entity):
    def update(self):
        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s']) * 0
            + self.right * (held_keys['d'] - held_keys['a'])
        ).normalized()

        origin = self.world_position
        hit_info = boxcast(origin, self.direction, ignore=(self,),
                           distance=0.55 * self.scale_x, debug=False,
                           thickness=(BOXCAST_THICKNESS * self.scale_z,
                                      BOXCAST_THICKNESS))
        if not hit_info.hit:
            self.position += self.direction * SPEED * time.dt


# blue blocks move along z axis
class PinkBlock(Entity):
    def update(self):
        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a']) * 0
        ).normalized()

        origin = self.world_position
        hit_info = boxcast(origin, self.direction, ignore=(self,),
                           distance=0.55 * self.scale_z, debug=False,
                           thickness=(BOXCAST_THICKNESS * self.scale_x,
                                      BOXCAST_THICKNESS))
        if not hit_info.hit:
            self.position += self.direction * SPEED * time.dt


# white blocks are static
class WhiteBlock(Entity):
    pass
