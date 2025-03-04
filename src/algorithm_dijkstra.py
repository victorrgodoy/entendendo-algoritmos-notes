#best path between 'start' and 'end' (graph weighted)
#weights will need positives

graph = {}
values = {}
paths = {}

graph["start"] = {"a": 6, "b": 2}
graph["a"] = {"end": 1}
graph["b"] = {"a": 3, "end": 5}
graph["end"] = {}

values["start"] = 0
values["a"] = float("inf")
values["b"] = float("inf")
values["end"] = float("inf")

paths["a"] = None
paths["b"] = None
paths["end"] = None


def find_min_value(values, processed):
    min_value = float("inf")
    min_node = None
    for node in values:
        if min_value > values[node] and node not in processed:
            min_value = values[node]
            min_node = node
    return min_node

def algorithm_dijkstra(graph, values, paths):
    processed = []
    node = find_min_value(values, processed)
    while node is not None:
        value_node = values[node]
        neighbors = graph[node]
        for i in neighbors:
            new_value = value_node + neighbors[i]
            if values[i] > new_value:
                values[i] = new_value
                paths[i] = node
        processed.append(node)
        node = find_min_value(values, processed)
    return paths

print(algorithm_dijkstra(graph, values, paths))
    












