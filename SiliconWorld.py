from random import randint
from Electronic import Electronic

def generate_map(w, h, silicon_world):
    for i in range(0, h-1):
        j = 0
        rand_step = randint(0, w//2)
        j = j + rand_step
        silicon_world[i][j] = 0
        silicon_world[i][j + 1] = 0
        silicon_world[i + 1][j] = 0
        silicon_world[i + 1][j + 1] = 0
        rand_step = randint(0, w//2)
        while j+rand_step > w-2:
            rand_step = randint(0, w//2)
        j = j + rand_step
        silicon_world[i][j] = 0
        silicon_world[i][j + 1] = 0
        silicon_world[i + 1][j] = 0
        silicon_world[i + 1][j + 1] = 0
    if i < h - 4:
        i = i + h//4

    return silicon_world


class SiliconWorld:
    def __init__(self, w, h):
        self.SiliconWorld = [[1 for _ in range(0, w)] for _ in range(0, h)]
        self.SiliconWorld = generate_map(w, h, self.SiliconWorld)
        self.SiliconWorld[0][0] = 1
        self.electronic = Electronic()
        # self.SiliconWorld[0][0] = 1

    def get_silicon_world(self):
        return self.SiliconWorld

    def print_map(self, w, h):
        fuel_y = randint(2, h//2)
        fuel_x = randint(2, w//2)
        for i in range(0, h):
            for j in range(0, w):
                if i == self.electronic.location['x'] and j == self.electronic.location['y']:
                    print("|♌|", end='')
                elif i == fuel_y and j == fuel_x:
                    print("|இ|", end='')
                elif self.SiliconWorld[i][j] == 0:
                    print("|#|", end="")
                else:
                    print("|.|", end="")
            print("\n", end="")
