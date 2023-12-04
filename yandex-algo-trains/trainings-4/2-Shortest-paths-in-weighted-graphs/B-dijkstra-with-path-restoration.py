'''
Дейкстра с восстановлением пути
Дан ориентированный взвешенный граф.
Найдите кратчайший путь от одной заданной вершины до другой.

Формат ввода
В первой строке содержатся три числа: N, S и F (1≤N≤100, 1≤S, F≤N),
где N — количество вершин графа, S — начальная вершина, а F — конечная.
В следующих N строках вводится по N чисел, не превосходящих 100,
– матрица смежности графа, где -1 означает, что ребра между вершинами нет,
а любое неотрицательное число — наличие ребра данного веса.
На главной диагонали матрицы записаны нули.

Формат вывода
Последовательно выведите все вершины одного (любого) из кратчайших путей,
или -1, если пути между указанными вершинами не существует

Примечания
Пример ввода:
3 2 1
0 1 1
4 0 1
2 1 0
Пример вывода:
2 3 1
'''


from typing import List
import heapq


def dijkstra(graph: List[List[int]], start: int, end: int) -> int:
    start, end = start - 1, end - 1
    min_distances = [float('inf')] * len(graph)
    min_distances[start] = 0
    visited = [-1] * len(graph)
    priority_queue = [(min_distances[start], start)]
    heapq.heapify(priority_queue)
    while priority_queue:
        current = heapq.heappop(priority_queue)[1]
        if current == end:
            path = [end]
            cur = end
            while visited[cur] != -1:
                cur = visited[cur]
                path.append(cur)
            path.reverse()
            return path
        for neighbor in range(len(graph)):
            if graph[current][neighbor] != -1 and min_distances[neighbor] > min_distances[current] + graph[current][neighbor]:
                min_distances[neighbor] = min_distances[current] + graph[current][neighbor]
                visited[neighbor] = current
                heapq.heappush(priority_queue, (min_distances[neighbor], neighbor))
    return []


if __name__ == '__main__':
    assert dijkstra([[0, 1, 1], [4, 0, 1], [2, 1, 0]], 2, 1) == [1, 2, 0], 'Test 1'
    n, start, end = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    path = [p + 1 for p in dijkstra(graph, start, end)]
    print(*path if path else -1)



