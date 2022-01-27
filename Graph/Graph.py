from Graph.Node import Node


class Graph:
    def __init__(self, memory):
        self.__nodes = []
        self.__world = memory.get_silicon_world()
        self.create_graph()

    def __len__(self):
        return len(self.__nodes)

    def __repr__(self):
        length = len(self.__nodes)
        s = '[\n'
        for i in range(0, length - 1):
            num = '\t{\n\t\tnumber: ' + str(self.__nodes[i].get_number()) + '\n\t\t'
            id = 'id: [' + str(self.__nodes[i].get_id().y) + ', ' \
                 + str(self.__nodes[i].get_id().x) + '],\n\t\t'
            boolean = 'isElectronic: ' + str(self.__nodes[i].get_is_electronic()) + '\n\t\t'
            end = 'end: ' + str(self.__nodes[i].get_is_end()) + '\n\t\t'
            fuel = 'fuel: ' + str(self.__nodes[i].get_is_fuel()) + '\n\t\t'
            steps = '{\n\t\t\t\'up\':\t  ' + str(self.__nodes[i].get_steps().up) + ',\n\t\t\t\'down\':\t  ' \
                    + str(self.__nodes[i].get_steps().down) + ',\n\t\t\t\'left\':\t  ' \
                    + str(self.__nodes[i].get_steps().left) \
                    + ',\n\t\t\t\'right\':  ' + str(self.__nodes[i].get_steps().right) + "\n\t\t}"
            s += num + id + boolean + end + fuel + steps + '\n\t},\n'
        num = '\t{\n\t\tnumber: ' + str(self.__nodes[length - 1].get_number()) + '\n\t\t'
        id = 'id: [' + str(self.__nodes[length - 1].get_id().y) + ', ' \
             + str(self.__nodes[length - 1].get_id().x) + '],\n\t\t'
        boolean = 'isElectronic: ' + str(self.__nodes[length - 1].get_is_electronic()) + '\n\t\t'
        end = 'end: ' + str(self.__nodes[length - 1].get_is_end()) + '\n\t\t'
        fuel = 'fuel: ' + str(self.__nodes[length - 1].get_is_fuel()) + '\n\t\t'
        steps = '{\n\t\t\t\'up\':\t  ' + str(self.__nodes[length - 1].get_steps().up) + ',\n\t\t\t\'down\':\t  ' \
                + str(self.__nodes[length - 1].get_steps().down) + ',\n\t\t\t\'left\':\t  ' \
                + str(self.__nodes[length - 1].get_steps().left) \
                + ',\n\t\t\t\'right\':  ' + str(self.__nodes[length - 1].get_steps().right) + "\n\t\t}"
        s += num + id + boolean + end + fuel + steps + '\n\t}\n'
        s += ']'
        return s

    def create_graph(self):
        num = 0
        for i in range(0, self.__world.get_height()):
            for j in range(0, self.__world.get_width()):
                if self.__world.get_map_atom(i, j) == 0:
                    continue
                elif self.__world.get_map_atom(i, j) == 1:
                    self.__nodes.append(Node(number=num, id=[i, j], steps=self.get_barrier(self.__world, i, j)))
                    num += 1
                elif self.__world.get_map_atom(i, j) == 2:
                    self.__nodes.append(Node(number=num, id=[i, j], steps=self.get_barrier(self.__world, i, j), fuel=True))
                    num += 1
                elif self.__world.get_map_atom(i, j) == 3:
                    self.__nodes.append(Node(number=num, id=[i, j], steps=self.get_barrier(self.__world, i, j), end=True))
                    num += 1
                elif self.__world.get_map_atom(i, j) == 5:
                    self.__nodes.append(Node(number=num, id=[i, j], steps=self.get_barrier(self.__world, i, j), is_electronic=True))
                    num += 1

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
            elif wold.get_map_atom(h, w - 1) == 0:
                left = 0
            else:
                left = 1
        except Exception:
            left = 0
        try:
            if wold.get_map_atom(h + 1, w) == 0:
                down = 0
            else:
                down = 1
        except Exception:
            down = 0
        try:
            if wold.get_map_atom(h, w + 1) == 0:
                right = 0
            else:
                right = 1
        except Exception:
            right = 0

        return [up, down, left, right]

    def get_graph(self):
        return self.__nodes

    def get_node(self, id):
        return self.__nodes[id]

    def get_node_from_id(self, x, y):
        for i in self.__nodes:
            if i.get_id().x == x and i.get_id().y == y:
                return i

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

    def add_node(self, node):
        self.__nodes.append(node)