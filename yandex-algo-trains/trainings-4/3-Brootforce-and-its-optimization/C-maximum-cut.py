'''
Максимальный разрез
Взвешенный неориентированный граф без петель задан матрицей смежности.
Распределите вершины по двум долям так, чтобы сумма весов рёбер,
соединяющих вершины из разных долей, была максимальна.

Формат ввода
Вводится число N (2≤N≤20) — количество вершин в графе.
В следующих N строках, содержащих по N целых чисел от 0 до 1000,
задаётся матрица смежности. 0 означает отсутствие ребра.

Формат вывода
В первой строке выведите суммарный вес рёбер, соединяющих вершины из разных долей.
Во второй строке выведите N чисел 1 или 2 — номера долей для каждой из вершин графа.

Пример 1
Ввод
2
0 1
1 0
Вывод
1
2 1 
Пример 2
Ввод
3
0 1 2
1 0 2
2 2 0
Вывод
4
2 2 1 
Пример 3
Ввод
4
0 10 3 0
10 0 7 2
3 7 0 9
0 2 9 0
Вывод
26
2 1 2 1 
'''

from typing import List
from itertools import combinations


def max_cut(graph: List[List[int]]) -> int:
    N = len(graph)
    max_cut_weight = 0
    partition = []

    for mask in range(1, 1 << N):
        cut_weight = 0

        bit_index = 0
        while (mask & (1 << bit_index)) == 0:
            bit_index += 1

        current_partition = [1 if (mask & (1 << i)) else 2 for i in range(N)]

        for i in range(N):
            for j in range(i + 1, N):
                if current_partition[i] != current_partition[j]:
                    cut_weight += graph[i][j]

        if cut_weight > max_cut_weight:
            max_cut_weight = cut_weight
            partition = current_partition

    return max_cut_weight, partition


def max_cut(graph: List[List[int]]) -> int:
    N = len(graph)
    max_cut_weight = 0
    partition = []

    partition_weights = [[0] * N for _ in range(N)]
    for i, j in combinations(range(N), 2):
        partition_weights[i][j] = graph[i][j]

    for mask in range(1, 1 << N):
        cut_weight = 0
        current_partition = [1 if (mask >> i) & 1 else 2 for i in range(N)]

        for i, j in combinations(range(N), 2):
            if current_partition[i] != current_partition[j]:
                cut_weight += partition_weights[i][j]

        if cut_weight > max_cut_weight:
            max_cut_weight = cut_weight
            partition = current_partition

    return max_cut_weight, partition

if __name__ == '__main__':
    assert max_cut([[0, 1], [1, 0]]) == (1, [1, 2]), 'Test 1'
    assert max_cut([[0, 1, 2], [1, 0, 2], [2, 2, 0]]) == (4, [1, 1, 2]), 'Test 2'
    assert max_cut([[0, 10, 3, 0], [10, 0, 7, 2], [3, 7, 0, 9], [0, 2, 9, 0]]) == (26, [1, 2, 1, 2]), 'Test 3'
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    max_weight, partition = max_cut(graph)
    print(max_weight)
    print(*partition)