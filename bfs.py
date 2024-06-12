from collections import deque

def bipartite(graph):

    colors = {}
    for node in graph:
        colors[node] = 0

    for node in graph:
        if colors[node] != 0:
            continue

        colors[node] = 1
        q = deque([node])

        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if colors[neighbor] == colors[node]:
                    return False
                if colors[neighbor] == 0:
                    colors[neighbor] = -colors[node]
                    q.append(neighbor)
                    return  True
    return True

# Пример графа в виде списка смежности
graph = {
    'a': ['b', 'd'],
    'b': ['a', 'c'],
    'c': ['b', 'd'],
    'd': ['a', 'c']
}

if bipartite(graph):
    print("Граф двудольный.")
else:
    print("Граф не является двудольным.")
















