from Imports.ALL_Imports import *


def distance_node_to_end(node, end):
    result = (abs(node.get_id().x - end.get_id().x) + abs(node.get_id().y - end.get_id().y))
    return result


def choose_node(nodes, end):
    min_cost = 999999999999999
    result_node = None
    for node in nodes:
        start_cost = node.get_cost()
        cost_node = distance_node_to_end(node, end)
        result_cost = start_cost + cost_node

        if min_cost > result_cost:
            min_cost = result_cost
            result_node = node

    return result_node


def build_path(node):
    result = []
    while node is not None:
        result.append(node)
        node = node.get_prev()
    if not result:
        return None
    return result
