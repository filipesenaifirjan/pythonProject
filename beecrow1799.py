# encoding : utf-8
from heapq import heappush, heappop


def dijkstra(graph, start):
    a = {x: None for x in list(graph.keys())}
    queue = [(0, start)]
    while queue:
        distance, v = heappop(queue)
        if a[v] is None:
            a[v] = distance
            for w in graph[v]:
                if a[w] is None:
