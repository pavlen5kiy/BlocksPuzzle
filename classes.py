from ursina import *

from settings import *

# player moves along z axis
class Player(Entity):
    def update(self):
        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a']) * 0
        ).normalized()

        origin = self.world_position
        distance = BOXCAST_DISTANCE * self.scale_z + BOXCAST_DISTANCE_MODIFIER
        thickness = (BOXCAST_THICKNESS * self.scale_x, BOXCAST_THICKNESS)

        hit_info = boxcast(origin, self.direction, ignore=(self,),
                           distance=distance, thickness=thickness)

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
        distance = BOXCAST_DISTANCE * self.scale_x + BOXCAST_DISTANCE_MODIFIER
        thickness = (BOXCAST_THICKNESS * self.scale_z, BOXCAST_THICKNESS)

        hit_info = boxcast(origin, self.direction, ignore=(self,),
                           distance=distance, thickness=thickness)

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
        distance = BOXCAST_DISTANCE * self.scale_z + BOXCAST_DISTANCE_MODIFIER
        thickness = (BOXCAST_THICKNESS * self.scale_x, BOXCAST_THICKNESS)

        hit_info = boxcast(origin, self.direction, ignore=(self,),
                           distance=distance, thickness=thickness)

        if not hit_info.hit:
            self.position += self.direction * SPEED * time.dt


# white blocks are static
class WhiteBlock(Entity):
    pass
