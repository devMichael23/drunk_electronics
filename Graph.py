from Memory import Memory

class Steps:
    def __init__(self, up=None, down=None, left=None, right=None):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def get_steps(self):
        return '{\n\t\'up\':\t ' + str(self.up) + ',\n\t\'down\':\t ' + str(self.down) + ',\n\t\'left\':\t  ' \
               + str(self.left) + ',\n\t\'right\': ' + str(self.right) + "\n}"

class Node:
    def __init__(self, steps=None, is_electronic=False):
        self.steps = Steps(steps[0], steps[1], steps[2], steps[3])
        self.isElectronic = is_electronic

    def __str__(self):
        s = self.steps.get_steps() + "\n" + str(self.isElectronic)
        return s