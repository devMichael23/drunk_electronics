from Graph.Steps import Steps


class Node:
    def __init__(self, number=None, id=None, steps=None, is_electronic=False, end=False, fuel=False):
        self.__number = number
        if id is None:
            id = [0, 0]
        if steps is None:
            steps = [0, 0, 0, 0]
        self.__id = type("", (), dict(y=id[0], x=id[1]))()
        self.__steps = Steps(steps[0], steps[1], steps[2], steps[3])
        self.__isElectronic = is_electronic
        self.__end = end
        self.__fuel = fuel
        self.__prev = None

    def __repr__(self):
        num = '{\n\tnum: ' + str(self.__number) + '\n\t'
        id = 'id: [' + str(self.__id.y) + ', ' + str(self.__id.x) + '],\n\t'
        boolean = 'isElectronic: ' + str(self.__isElectronic) + '\n\t'
        end = 'end: ' + str(self.__end) + '\n\t'
        fuel = 'fuel: ' + str(self.__fuel) + '\n\t'
        s = num + id + boolean + end + fuel + str(self.__steps) + '\n}\n'
        return s

    def __iter__(self):
        return self.__id

    def get_id(self):
        return self.__id

    def get_steps(self):
        return self.__steps

    def get_is_fuel(self):
        return self.__fuel

    def get_is_end(self):
        return self.__end

    def get_is_electronic(self):
        return self.__isElectronic

    def get_number(self):
        return self.__number

    def set_prev(self, prev):
        self.__prev = prev

    def get_prev(self):
        return self.__prev
