'''
Простая задача коммивояжера
Неориентированный взвешенный граф задан матрицей смежности.
Найдите кратчайший цикл, который начинается и заканчивается в вершине номер 1
и проходит через все вершины по одному разу.

Формат ввода
В первой строке вводится число N (N≤10) — количество вершин графа.
Следующие N строк содержат по N целых неотрицательных чисел и задают матрицу смежности.
Число 0 означает, что ребро отстутствует. Любое другое число задаёт вес ребра.

Формат вывода
Выведите минимальную суммарную длину цикла или число -1, если цикл построить невозможно.

Пример 1
Ввод
1
0
Вывод
0
Пример 2
Ввод
2
0 1
1 0
Вывод
2
Пример 3
Ввод
2
0 85 
85 0 
Вывод
170
'''

from itertools import permutations
from typing import List

def traveling_salesman_problem(graph: List[List[int]]) -> int:
    n = len(graph)
    min_path = float("inf")

    for permutation in permutations(range(1, n)):
        path = 0
        vertex = 0
        visited = set()

        for next_vertex in permutation:
            if graph[vertex][next_vertex] == 0 or next_vertex in visited:
                break
            path += graph[vertex][next_vertex]
            visited.add(next_vertex)
            vertex = next_vertex
        
        path += graph[vertex][0]

        if len(visited) == n - 1:
            min_path = min(min_path, path)

    return min_path if min_path != float("inf") else -1


if __name__ == '__main__':
    assert traveling_salesman_problem([[0]]) == 0, 'Test 1'
    assert traveling_salesman_problem([[0, 1], [1, 0]]) == 2, 'Test 2'
    assert traveling_salesman_problem([[0, 85], [85, 0]]) == 170, 'Test 3'
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    print(traveling_salesman_problem(graph))
