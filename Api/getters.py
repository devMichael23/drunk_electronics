from Imports.ALL_Imports import *
from Api.paths_work import *


def get_nodes_to_move_from_electronic(graph):
    result = []
    for i in graph.get_graph():
        if i.get_is_electronic():
            if i.get_steps().up:
                result.append(graph.get_node_from_id(i.get_id().x, i.get_id().y - 1))
            if i.get_steps().down:
                result.append(graph.get_node_from_id(i.get_id().x, i.get_id().y + 1))
            if i.get_steps().left:
                result.append(graph.get_node_from_id(i.get_id().x - 1, i.get_id().y))
            if i.get_steps().right:
                result.append(graph.get_node_from_id(i.get_id().x + 1, i.get_id().y))
    return result


def get_nodes_to_move(graph: Graph, node: Node) -> list[Node]:
    result = []
    if node.get_steps().up:
        result.append(graph.get_node_from_id(node.get_id().x, node.get_id().y - 1))
    if node.get_steps().down:
        result.append(graph.get_node_from_id(node.get_id().x, node.get_id().y + 1))
    if node.get_steps().left:
        result.append(graph.get_node_from_id(node.get_id().x - 1, node.get_id().y))
    if node.get_steps().right:
        result.append(graph.get_node_from_id(node.get_id().x + 1, node.get_id().y))
    return result


def get_removes_list(reduced, deductible):
    for i in deductible:
        if i in reduced:
            reduced.remove(i)
    return reduced


def get_path(graph: Graph):
    reachable = graph
    explored = []
    while reachable:
        node = choose_node(get_nodes_to_move(reachable, reachable.get_node(0)))

        if node == graph.get_end_node():
            return build_path(graph.get_end_node())

        reachable.remove_element(node)
        explored.append(node)

        new_reachable = get_removes_list(get_nodes_to_move(reachable, node), explored)
        for moves in new_reachable:
            if moves not in reachable:
                moves.set_prev(node)

    return None
