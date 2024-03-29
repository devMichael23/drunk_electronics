from World.Memory import Memory
from Graph.Graph import Graph
from Api.getters import get_path

mem = Memory(25, 25)
g = Graph(mem)
copy = mem

print(mem.get_silicon_world())

path = get_path(g, mem)

print(mem.get_silicon_world())
print(path)