from Memory import *

mem = Memory()
world = SiliconWorld(50, 50)
electronic = Electronic()
mem.electronic = electronic
mem.silicon_world = world
mem.update_electronic_pos()
mem.silicon_world.print_map()
print('\n\n\n\n\n')
mem.move_electronic(5, 5)
mem.silicon_world.print_map()
