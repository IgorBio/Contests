'''
Быстрый алгоритм Дейкстры
Вам дано описание дорожной сети страны.
Ваша задача – найти длину кратчайшего пути между городами А и B.

Формат ввода
Сеть дорог задана во входном файле следующим образом: первая строка содержит
числа N и K (1≤N≤100000,0≤K≤300000), где K – количество дорог.
Каждая из следующих K строк содержит описание дороги с
двусторонним движением – три целых числа ai, bi и li (1≤ai, bi≤N, 1≤li≤10^6).
Это означает, что имеется дорога длины li, которая ведет из города ai в город bi.
В последней строке находятся два числа А и В – номера городов,
между которыми надо посчитать кратчайшее расстояние (1≤A, B≤N)

Формат вывода
Выведите одно число – расстояние между нужными городами.
Если по дорогам от города А до города В доехать невозможно, выведите –1.

Пример
Ввод
6 4
1 2 7
2 4 8
4 5 1
4 3 100
3 1
Вывод
115
'''

import heapq
from typing import List

class Edge:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight

def dijkstra(graph: List[List[Edge]], distances: List[int], start: int) -> None:
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)
    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)
        if distances[current] < current_distance:
            continue
        for edge in graph[current]:
            new_distance = current_distance + edge.weight
            if new_distance < distances[edge.to]:
                distances[edge.to] = new_distance
                heapq.heappush(priority_queue, (new_distance, edge.to))

if __name__ == '__main__':
    n, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        a, b, w = map(int, input().split())
        graph[a].append(Edge(b, w))
        graph[b].append(Edge(a, w))
    distances = [float('inf')] * (n + 1)
    A, B = map(int, input().split())
    dijkstra(graph, distances, A)
    print(distances[B] if distances[B] != float('inf') else -1)