'''
Автобусы в Васюках
Между некоторыми деревнями края Васюки ходят автобусы.
Поскольку пассажиропотоки здесь не очень большие, то автобусы ходят всего несколько раз в день.
Марии Ивановне требуется добраться из деревни d в деревню v как можно быстрее
(считается, что в момент времени 0 она находится в деревне d).

Формат ввода
Сначала вводится число N – общее число деревень (1<=N<=100), затем номера деревень d и v,
за ними следует количество автобусных рейсов R (0<=R<=10000).
Далее идут описания автобусных рейсов. Каждый рейс задается номером деревни отправления,
временем отправления, деревней назначения и временем прибытия (все времена – целые от 0 до 10000).
Если в момент t пассажир приезжает в какую-то деревню, то уехать из нее он может в любой момент времени, начиная с t.

Формат вывода
Выведите минимальное время, когда Мария Ивановна может оказаться в деревне v.
Если она не сможет с помощью указанных автобусных рейсов добраться из d в v, выведите -1.

Пример
Ввод
3
1 3
4
1 0 2 5
1 1 2 3
2 3 3 5
1 1 3 10
Вывод
5
'''

import heapq
from typing import List


class Bus:
    def __init__(self, departure: int, departure_time: int, destination: int, arrival_time: int):
        self.departure = departure
        self.departure_time = departure_time
        self.destination = destination
        self.arrival_time = arrival_time

class State:
    def __init__(self, village: int, time: int):
        self.village = village
        self.time = time

    def __gt__(self, other):
        return self.time > other.time

def dijkstra_algorithm(buses: List[List[Bus]], start: int, end: int) -> int:
    pq = []
    min_time = [[float('inf')] * 10001 for _ in range(len(buses))]

    heapq.heappush(pq, State(start, 0))
    min_time[start][0] = 0

    while pq:
        current = heapq.heappop(pq)

        if current.village == end:
            return current.time

        for bus in buses[current.village]:
            if bus.departure_time >= current.time and bus.arrival_time < min_time[bus.destination][bus.departure_time]:
                min_time[bus.destination][bus.departure_time] = bus.arrival_time
                heapq.heappush(pq, State(bus.destination, bus.arrival_time))

    return -1

if __name__ == '__main__':
    N = int(input())
    d, v = map(int, input().split())
    R = int(input())
    buses = [[] for _ in range(N + 1)]

    for _ in range(R):
        departure, departure_time, destination, arrival_time = map(int, input().split())
        bus = Bus(departure, departure_time, destination, arrival_time)
        buses[bus.departure].append(bus)

    print(dijkstra_algorithm(buses, d, v))
