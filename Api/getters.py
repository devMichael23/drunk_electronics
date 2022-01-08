def get_nodes_to_move(graph):
    result = []
    for i in graph.get_graph():
        if i.get_is_electronic():
            if i.get_steps().up:
                result.append(graph.get_node_from_id(i.get_id().x, i.get_id().y-1))
            if i.get_steps().down:
                result.append(graph.get_node_from_id(i.get_id().x, i.get_id().y+1))
            if i.get_steps().left:
                result.append(graph.get_node_from_id(i.get_id().x-1, i.get_id().y))
            if i.get_steps().right:
                result.append(graph.get_node_from_id(i.get_id().x+1, i.get_id().y))
    return result
