from termcolor import colored
from random import randint


class SiliconWorld:
    def __init__(self, w=10, h=10):
        self.SiliconWorld = [[1 for _ in range(0, w)] for _ in range(0, h)]
        self.generate_map()

    def create_fuel(self):
        for i in range(0, len(self.SiliconWorld)):
            for j in range(0, len(self.SiliconWorld[i])):
                fuel = randint(0, 19)
                if fuel == 1:
                    self.SiliconWorld[i][j] = 2

    def generate_map(self):
        for i in range(0, len(self.SiliconWorld) - 1):
            j = 0
            rand_step = randint(0, len(self.SiliconWorld[i]) // 2)
            j = j + rand_step
            self.SiliconWorld[i][j] = 0
            self.SiliconWorld[i][j + 1] = 0
            self.SiliconWorld[i + 1][j] = 0
            self.SiliconWorld[i + 1][j + 1] = 0
            rand_step = randint(0, len(self.SiliconWorld[i]) // 2)
            while j + rand_step > len(self.SiliconWorld[i]) - 2:
                rand_step = randint(0, len(self.SiliconWorld[i]) // 2)
            j = j + rand_step
            self.SiliconWorld[i][j] = 0
            self.SiliconWorld[i][j + 1] = 0
            self.SiliconWorld[i + 1][j] = 0
            self.SiliconWorld[i + 1][j + 1] = 0
            if i < len(self.SiliconWorld) - 4:
                i + len(self.SiliconWorld) // 4

        self.create_fuel()

        end_x = randint(0, len(self.SiliconWorld[0]))
        end_y = randint(0, len(self.SiliconWorld))
        while self.SiliconWorld[end_x][end_y] == 0:
            end_x = randint(0, len(self.SiliconWorld[0]))
            end_y = randint(0, len(self.SiliconWorld))

        self.SiliconWorld[end_x][end_y] = 3

    def set_params_to_map(self, x, y, param):
        self.SiliconWorld[x][y] = param

    def print_map(self):
        for i in range(0, len(self.SiliconWorld)):
            for j in range(0, len(self.SiliconWorld[i])):
                if self.SiliconWorld[i][j] == 5:
                    print(colored("|♌|", 'magenta', attrs=['bold']), end='')
                elif self.SiliconWorld[i][j] == 3:
                    print(colored("|E|", 'yellow', attrs=['bold']), end='')
                elif self.SiliconWorld[i][j] == 2:
                    print(colored("|Ω|", 'red'), end='')
                elif self.SiliconWorld[i][j] == 1:
                    print("|.|", end="")
                elif self.SiliconWorld[i][j] == 0:
                    print(colored("|#|", 'green'), end='')
            print("\n", end="")
