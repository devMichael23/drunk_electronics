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
    def __init__(self, id=None, steps=None, is_electronic=False):
        if id is None:
            id = [0, 0]
        if steps is None:
            steps = [0, 0, 0, 0]
        self.id = type("", (), dict(x=id[0], y=id[1]))()
        self.steps = Steps(steps[0], steps[1], steps[2], steps[3])
        self.isElectronic = is_electronic

    def __str__(self):
        id = '{\n\tid: {' + str(self.id.x) + '; ' + str(self.id.y) + '},\n\t'
        boolean = 'isElectronic: ' + str(self.isElectronic) + '\n\t'
        s = id + boolean + self.steps.get_steps() + '\n}'
        return s


class Graph:
    def __init__(self):
        self.length = 0

    def __len__(self):
        return self.length