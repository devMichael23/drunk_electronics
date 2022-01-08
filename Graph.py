class Steps:
    def __init__(self, up=None, down=None, left=None, right=None):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def __str__(self):
        return '{\n\t\t\'up\':\t  ' + str(self.up) + ',\n\t\t\'down\':\t  ' + str(self.down) + ',\n\t\t\'left\':\t  ' \
               + str(self.left) + ',\n\t\t\'right\':  ' + str(self.right) + "\n\t}"


class Node:
    def __init__(self, id=None, steps=None, is_electronic=False, end=False, fuel=False):
        if id is None:
            id = [0, 0]
        if steps is None:
            steps = [0, 0, 0, 0]
        self.__id = type("", (), dict(y=id[0], x=id[1]))()
        self.__steps = Steps(steps[0], steps[1], steps[2], steps[3])
        self.__isElectronic = is_electronic
        self.__end = end
        self.__fuel = fuel

    def __repr__(self):
        id = '{\n\tid: [' + str(self.__id.y) + ', ' + str(self.__id.x) + '],\n\t'
        boolean = 'isElectronic: ' + str(self.__isElectronic) + '\n\t'
        end = 'end: ' + str(self.__end) + '\n\t'
        fuel = 'fuel: ' + str(self.__fuel) + '\n\t'
        s = id + boolean + end + fuel + str(self.__steps) + '\n}\n'
        return s

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


class Graph:
    def __init__(self, memory):
        self.__nodes = []
        self.__world = memory.get_silicon_world()
        self.create_graph()

    def __repr__(self):
        length = len(self.__nodes)
        s = '[\n'
        for i in range(0, length-1):
            id = '\t{\n\t\tid: [' + str(self.__nodes[i].get_id().y) + ', ' \
                 + str(self.__nodes[i].get_id().x) + '],\n\t\t'
            boolean = 'isElectronic: ' + str(self.__nodes[i].get_is_electronic()) + '\n\t\t'
            end = 'end: ' + str(self.__nodes[i].get_is_end()) + '\n\t\t'
            fuel = 'fuel: ' + str(self.__nodes[i].get_is_fuel()) + '\n\t\t'
            steps = '{\n\t\t\t\'up\':\t  ' + str(self.__nodes[i].get_steps().up) + ',\n\t\t\t\'down\':\t  ' \
                    + str(self.__nodes[i].get_steps().down) + ',\n\t\t\t\'left\':\t  ' \
                    + str(self.__nodes[i].get_steps().left) \
                    + ',\n\t\t\t\'right\':  ' + str(self.__nodes[i].get_steps().right) + "\n\t\t}"
            s += id + boolean + end + fuel + steps + '\n\t},\n'
        id = '\t{\n\t\tid: [' + str(self.__nodes[length-1].get_id().y) + ', ' \
             + str(self.__nodes[length-1].get_id().x) + '],\n\t\t'
        boolean = 'isElectronic: ' + str(self.__nodes[length-1].get_is_electronic()) + '\n\t\t'
        end = 'end: ' + str(self.__nodes[length-1].get_is_end()) + '\n\t\t'
        fuel = 'fuel: ' + str(self.__nodes[length-1].get_is_fuel()) + '\n\t\t'
        steps = '{\n\t\t\t\'up\':\t  ' + str(self.__nodes[length-1].get_steps().up) + ',\n\t\t\t\'down\':\t  ' \
                + str(self.__nodes[length-1].get_steps().down) + ',\n\t\t\t\'left\':\t  ' \
                + str(self.__nodes[length-1].get_steps().left) \
                + ',\n\t\t\t\'right\':  ' + str(self.__nodes[length-1].get_steps().right) + "\n\t\t}"
        s += id + boolean + end + fuel + steps + '\n\t}\n'
        s += ']'
        return s

    def create_graph(self):
        for i in range(0, self.__world.get_height()):
            for j in range(0, self.__world.get_width()):
                if self.__world.get_map_atom(i, j) == 0:
                    continue
                elif self.__world.get_map_atom(i, j) == 1:
                    self.__nodes.append(Node([i, j], steps=self.get_barrier(self.__world, i, j)))
                elif self.__world.get_map_atom(i, j) == 2:
                    self.__nodes.append(Node([i, j], steps=self.get_barrier(self.__world, i, j), fuel=True))
                elif self.__world.get_map_atom(i, j) == 3:
                    self.__nodes.append(Node([i, j], steps=self.get_barrier(self.__world, i, j), end=True))
                elif self.__world.get_map_atom(i, j) == 5:
                    self.__nodes.append(Node([i, j], steps=self.get_barrier(self.__world, i, j), is_electronic=True))

    def get_barrier(self, wold, h, w):
        try:
            if h - 1 < 0:
                up = 0
            elif wold.get_map_atom(h - 1, w) == 0:
                up = 0
            else:
                up = 1
        except Exception:
            up = 0
        try:
            if w - 1 < 0:
                left = 0
            elif wold.get_map_atom(h, w-1) == 0:
                left = 0
            else:
                left = 1
        except Exception:
            left = 0
        try:
            if wold.get_map_atom(h+1, w) == 0:
                down = 0
            else:
                down = 1
        except Exception:
            down = 0
        try:
            if wold.get_map_atom(h, w+1) == 0:
                right = 0
            else:
                right = 1
        except Exception:
            right = 0

        return [up, down, left, right]

    def get_node(self, id):
        return self.__nodes[id]

    def get_fuels(self):
        result = []
        for i in self.__nodes:
            if i.get_is_fuel():
                result.append(i)
        return result

    def get_end_node(self):
        for i in self.__nodes:
            if i.get_is_end():
                return i

    def get_electronic_node(self):
        for i in self.__nodes:
            if i.get_is_electronic():
                return i
