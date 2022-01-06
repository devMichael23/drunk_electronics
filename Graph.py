from Memory import *


class Steps:
    def __init__(self, up=None, down=None, left=None, right=None):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def get_steps(self):
        return '{\n\t\t\'up\':\t  ' + str(self.up) + ',\n\t\t\'down\':\t  ' + str(self.down) + ',\n\t\t\'left\':\t  ' \
               + str(self.left) + ',\n\t\t\'right\':  ' + str(self.right) + "\n\t}"


class Node:
    def __init__(self, id=None, steps=None, is_electronic=False, end=False):
        if id is None:
            id = [0, 0]
        if steps is None:
            steps = [0, 0, 0, 0]
        self.id = type("", (), dict(x=id[0], y=id[1]))()
        self.steps = Steps(steps[0], steps[1], steps[2], steps[3])
        self.isElectronic = is_electronic
        self.end = end

    def __str__(self):
        id = '{\n\tid: {' + str(self.id.x) + '; ' + str(self.id.y) + '},\n\t'
        boolean = 'isElectronic: ' + str(self.isElectronic) + '\n\t'
        end = 'end: ' + str(self.end) + '\n\t'
        s = id + boolean + end + self.steps.get_steps() + '\n}'
        return s


class Graph:
    def __init__(self):
        self.nodes = []

    def __str__(self):
        s = ''
        for i in self.nodes:
            s += str(i)
        return s

    def create_graph(self, memory: Memory):
        world = memory.get_silicon_world()
        for i in range(0, world.get_hight()):
            for j in range(0, world.get_weight()):
                if world.get_map_atom(i, j) == 0:
                    continue
                elif world.get_map_atom(i, j) == 1:
                    self.nodes.append(Node([i, j], steps=self.get_barrier(world, i, j)))
                elif world.get_map_atom(i, j) == 3:
                    self.nodes.append(Node([i, j], steps=self.get_barrier(world, i, j), end=True))
                elif world.get_map_atom(i, j) == 5:
                    self.nodes.append(Node([i, j], steps=self.get_barrier(world, i, j), is_electronic=True))

    def get_barrier(self, wold: SiliconWorld, h, w):
        try:
            if wold.get_map_atom(h - 1, w) == 0:
                up = 0
            else:
                up = 1
        except Exception:
            up = 0
        try:
            if wold.get_map_atom(h, w-1) == 0:
                left = 0
            else:
                left = 1
        except Exception:
            left = 0
        try:
            if wold.get_map_atom(h+1, w) == 0:
                down = 0
            else:
                down = 1
        except Exception:
            down = 0
        try:
            if wold.get_map_atom(h, w+1) == 0:
                right = 0
            else:
                right = 1
        except Exception:
            right = 0

        return [up, down, left, right]
