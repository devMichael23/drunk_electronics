from World.SiliconWorld import SiliconWorld
from World.Electronic import Electronic


class Memory:
    def __init__(self, w, h):
        self.__silicon_world = SiliconWorld(w, h)
        self.__electronic = Electronic()
        self.__silicon_world.set_params_to_map(self.__electronic.location.x, self.__electronic.location.y, 5)

    def move_electronic(self, x, y):
        if self.__electronic.fuel.need:
            if self.__electronic.fuel.bank > 0:
                self.__electronic.fuel.bank = self.__electronic.fuel.bank - 1
            else:
                exit(0)
        self.__silicon_world.set_params_to_map(self.__electronic.location.x, self.__electronic.location.y, 1)
        self.__electronic.location.x = x
        self.__electronic.location.y = y
        self.update_electronic_pos()

    def update_electronic_pos(self):
        self.__silicon_world.set_params_to_map(self.__electronic.location.x, self.__electronic.location.y, 5)

    def get_silicon_world(self):
        return self.__silicon_world

    def get_electronic(self):
        return self.__electronic
