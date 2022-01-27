from World.Memory import *
from Graph.Graph import Graph
from Api.getters import *

mem = Memory(25, 25)
g = Graph(mem)
copy = mem
print(mem.get_silicon_world())


path = get_path(g, mem)


print(mem.get_silicon_world())
