#1.there is a way between A and B?
#2.Which is the minumum way between A and B?
#3.use FIFO, first in, First out
#4.Graph not weighted

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["peggy", "anuj"]
graph["claire"] = ["thom", "jonny"]
graph["peggy"] = []
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = []

def is_seller(name):
    if name[-1] == "m":
        return True

def breadth_first_search(name, graph):
    queue = deque()
    queue += graph[name]
    visited = set()

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            if is_seller(vertex):
                print(f'{vertex} is seller!')
                return True
            else:
                visited.add(vertex)
                queue += graph[vertex]
    return False

print(breadth_first_search("you", graph))