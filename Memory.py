from SiliconWorld import SiliconWorld
from Electronic import Electronic


class Memory:
    def __init__(self):
        self.silicon_world = SiliconWorld()
        self.electronic = Electronic()
        self.silicon_world.set_params_to_map(self.electronic.location['x'], self.electronic.location['y'], 5)

    def move_electronic(self, x, y):
        if self.electronic.fuel['need']:
            if self.electronic.fuel['bank'] > 0:
                self.electronic.fuel["bank"] = self.electronic.fuel["bank"] - 1
            else:
                exit(0)
        self.silicon_world.set_params_to_map(self.electronic.location['x'], self.electronic.location['y'], 1)
        self.electronic.location = {
            'x': x,
            'y': y
        }
        self.update_electronic_pos()

    def update_electronic_pos(self):
        self.silicon_world.set_params_to_map(self.electronic.location['x'], self.electronic.location['y'], 5)