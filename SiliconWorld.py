from termcolor import colored
from random import randint


class SiliconWorld:
    def __init__(self, w=10, h=10):
        self.__w = w
        self.__h = h
        self.__SiliconWorld = [[1 for _ in range(0, self.__w)] for _ in range(0, self.__h)]
        self.generate_map()

    def create_fuel(self):
        for i in range(0, self.get_hight()):
            for j in range(0, self.get_weight()):
                fuel = randint(0, 19)
                if fuel == 1:
                    self.set_params_to_map(i, j, 2)

    def generate_map(self):
        for i in range(0, self.__h - 1):
            j = 0
            rand_step = randint(0, self.__w // 2)
            j = j + rand_step
            self.__SiliconWorld[i][j] = 0
            self.__SiliconWorld[i][j + 1] = 0
            self.__SiliconWorld[i + 1][j] = 0
            self.__SiliconWorld[i + 1][j + 1] = 0
            rand_step = randint(0, self.__w // 2)
            while j + rand_step > self.__w - 2:
                rand_step = randint(0, self.__w // 2)
            j = j + rand_step
            self.__SiliconWorld[i][j] = 0
            self.__SiliconWorld[i][j + 1] = 0
            self.__SiliconWorld[i + 1][j] = 0
            self.__SiliconWorld[i + 1][j + 1] = 0
            if i < self.__h - 4:
                i + self.__h // 4

        self.create_fuel()

        end_x = randint(0, self.__w)
        end_y = randint(0, self.__h)
        while self.__SiliconWorld[end_x][end_y] == 0:
            end_x = randint(0, self.__w)
            end_y = randint(0, self.__h)

        self.set_params_to_map(end_x, end_y, 3)

    def set_params_to_map(self, x, y, param):
        self.__SiliconWorld[y][x] = param

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
        return self.__w

    def get_hight(self):
        return self.__h

    def get_map_atom(self, h, w):
        return self.__SiliconWorld[h][w]
