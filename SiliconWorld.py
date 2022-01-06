from termcolor import colored
from random import randint


class SiliconWorld:
    def __init__(self, w=10, h=10):
        self.w = w
        self.h = h
        self.SiliconWorld = [[1 for _ in range(0, self.w)] for _ in range(0, self.h)]
        self.generate_map()

    def create_fuel(self):
        for i in range(0, len(self.SiliconWorld)):
            for j in range(0, len(self.SiliconWorld[i])):
                fuel = randint(0, 19)
                if fuel == 1:
                    self.SiliconWorld[i][j] = 2

    def generate_map(self):
        for i in range(0, self.h - 1):
            j = 0
            rand_step = randint(0, self.w // 2)
            j = j + rand_step
            self.SiliconWorld[i][j] = 0
            self.SiliconWorld[i][j + 1] = 0
            self.SiliconWorld[i + 1][j] = 0
            self.SiliconWorld[i + 1][j + 1] = 0
            rand_step = randint(0, self.w // 2)
            while j + rand_step > self.w - 2:
                rand_step = randint(0, self.w // 2)
            j = j + rand_step
            self.SiliconWorld[i][j] = 0
            self.SiliconWorld[i][j + 1] = 0
            self.SiliconWorld[i + 1][j] = 0
            self.SiliconWorld[i + 1][j + 1] = 0
            if i < self.h - 4:
                i + self.h // 4

        self.create_fuel()

        end_x = randint(0, self.w)
        end_y = randint(0, self.h)
        while self.SiliconWorld[end_x][end_y] == 0:
            end_x = randint(0, self.w)
            end_y = randint(0, self.h)

        self.SiliconWorld[end_x][end_y] = 3

    def set_params_to_map(self, x, y, param):
        self.SiliconWorld[y][x] = param

    def __str__(self):
        result = ''
        for i in range(0, self.__h):
            for j in range(0, self.__w):
                if self.__SiliconWorld[i][j] == 5:
                    result += colored("|♌|", 'magenta', attrs=['bold'])
                elif self.__SiliconWorld[i][j] == 3:
                    result += colored("|E|", 'yellow', attrs=['bold'])
                elif self.__SiliconWorld[i][j] == 2:
                    result += colored("|Ω|", 'red')
                elif self.__SiliconWorld[i][j] == 1:
                    result += "|.|"
                elif self.__SiliconWorld[i][j] == 0:
                    result += colored("|#|", 'green')
            result += '\n'
        return result

    def get_weight(self):
        return self.w

    def get_hight(self):
        return self.h

    def get_map_atom(self, h, w):
        return self.SiliconWorld[h][w]
