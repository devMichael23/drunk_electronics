from Imports.ALL_Imports import *


def choose_node(nodes: list[Node]):
    pass


def build_path(node: Node):
    result = []
    while node is not None:
        result.append(node)
        node = node.get_prev()
    return result
