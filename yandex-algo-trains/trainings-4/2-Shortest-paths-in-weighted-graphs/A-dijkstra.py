'''
Дейкстра
Дан ориентированный взвешенный граф. Найдите кратчайшее расстояние от одной заданной вершины до другой.

Формат ввода
В первой строке содержатся три числа: N, S и F (1≤N≤100, 1≤S, F≤N),
где N — количество вершин графа, S — начальная вершина, а F — конечная.
В следующих N строках вводится по N чисел, не превосходящих 100, – матрица смежности графа,
где -1 означает что ребра между вершинами нет, а любое неотрицательное число — наличие ребра данного веса.
На главной диагонали матрицы записаны нули.

Формат вывода
Выведите искомое расстояние или -1, если пути между указанными вершинами не существует.

Пример
Ввод
3 2 1
0 1 1
4 0 1
2 1 0
Вывод
3
'''


from typing import List
import heapq


def dijkstra(graph: List[List[int]], start: int, end: int) -> int:
    start, end = start - 1, end - 1
    min_distances = [float('inf')] * len(graph)
    min_distances[start] = 0
    priority_queue = [(min_distances[start], start)]
    heapq.heapify(priority_queue)
    while priority_queue:
        current = heapq.heappop(priority_queue)[1]
        if current == end:
            return min_distances[end]
        for neighbor in range(len(graph)):
            if graph[current][neighbor] != -1 and min_distances[neighbor] > min_distances[current] + graph[current][neighbor]:
                min_distances[neighbor] = min_distances[current] + graph[current][neighbor]
                heapq.heappush(priority_queue, (min_distances[neighbor], neighbor))
    return -1

if __name__ == '__main__':
    assert dijkstra([[0, 1, 1], [4, 0, 1], [2, 1, 0]], 2, 1) == 3, 'Test 1'
    n, start, end = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    print(dijkstra(graph, start, end))

    