from termcolor import colored
from random import randint


class SiliconWorld:
    def __init__(self, w=10, h=10):
        self.__width = w
        self.__height = h
        self.__SiliconWorld = [[1 for _ in range(0, self.__width)] for _ in range(0, self.__height)]
        self.generate_map()

    def create_fuel(self):
        for i in range(0, self.get_height()):
            for j in range(0, self.get_width()):
                fuel = randint(0, 19)
                if fuel == 1:
                    self.set_params_to_map(i, j, 2)

    def generate_map(self):
        for i in range(0, self.__height - 1):
            j = 0
            rand_step = randint(0, self.__width // 2)
            j = j + rand_step
            self.__SiliconWorld[i][j] = 0
            self.__SiliconWorld[i][j + 1] = 0
            self.__SiliconWorld[i + 1][j] = 0
            self.__SiliconWorld[i + 1][j + 1] = 0
            rand_step = randint(0, self.__width // 2)
            while j + rand_step > self.__width - 2:
                rand_step = randint(0, self.__width // 2)
            j = j + rand_step
            self.__SiliconWorld[i][j] = 0
            self.__SiliconWorld[i][j + 1] = 0
            self.__SiliconWorld[i + 1][j] = 0
            self.__SiliconWorld[i + 1][j + 1] = 0
            if i < self.__height - 4:
                i + self.__height // 4

        self.create_fuel()

        end_x = randint(0, self.__width)
        end_y = randint(0, self.__height)
        try:
            while self.__SiliconWorld[end_x][end_y] == 0:
                end_x = randint(0, self.__width)
                end_y = randint(0, self.__height)
        except IndexError:
            end_x = randint(0, self.__width)
            end_y = randint(0, self.__height)

        self.set_params_to_map(end_x, end_y, 3)

    def set_params_to_map(self, x, y, param):
        self.__SiliconWorld[y][x] = param

    def __repr__(self):
        result = ''
        for i in range(0, self.__height):
            for j in range(0, self.__width):
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

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_map_atom(self, h, w):
        return self.__SiliconWorld[h][w]
