

def dfs(graph, start, visited = None, result = None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    if start not in visited:
        visited.add(start)
        for next in sorted(graph[start] - visited):
            dfs(graph, next, visited, result)
        result.append(start)

def pack(graph):
    result = []
    visited = set()
    for node in graph: #Перебор каждой вершины
        if node not in visited:
            dfs(graph, node, visited, result)
    return result

graph = {'a': set([]),
         'b': set(['a']),
         'c': set(['a']),
         'd': set(['b', 'c']),}

devops = pack(graph)
print(devops)
