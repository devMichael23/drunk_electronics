class Steps:
    def __init__(self, up=None, down=None, left=None, right=None):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def get_steps(self):
        return '{\n\t\'up\':\t ' + str(self.up) + ',\n\t\'down\':\t ' + str(self.down) + ',\n\t\'left\':\t  ' \
               + str(self.left) + ',\n\t\'right\': ' + str(self.right) + "\n}"
