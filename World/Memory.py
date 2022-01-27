from World.SiliconWorld import SiliconWorld
from World.Electronic import Electronic
from Graph.Graph import *


class Memory:
    def __init__(self, w, h):
        self.__silicon_world = SiliconWorld(w, h)
        self.__electronic = Electronic()
        self.__silicon_world.set_params_to_map(self.__electronic.location.x, self.__electronic.location.y, 5)

    def move_electronic(self, x, y, graph=None, node=None):
        if self.__electronic.fuel.need:
            if self.__electronic.fuel.bank > 0:
                self.__electronic.fuel.bank = self.__electronic.fuel.bank - 5
            else:
                print('fuel of')
                exit(0)
        self.__silicon_world.set_params_to_map(self.__electronic.location.x, self.__electronic.location.y, 9)
        self.__electronic.location.x = x
        self.__electronic.location.y = y
        if graph and node:
            self.update_electronic_pos()
            graph.get_electronic_node().set_is_electronic(False)
            graph.search_node(node).set_is_electronic(True)
            if graph.search_node(node).get_is_fuel():
                self.__electronic.set_fuel_bank(self.__electronic.get_fuel_bank() + 50)

    def update_electronic_pos(self):
        self.__silicon_world.set_params_to_map(self.__electronic.location.x, self.__electronic.location.y, 5)

    def get_silicon_world(self):
        return self.__silicon_world

    def get_electronic(self):
        return self.__electronic
