'''
Путешествие по Москве
Мэрия Москвы основательно подготовилась к празднованию тысячелетия города в 2147 году,
построив под столицей бесконечную асфальтированную площадку, чтобы заменить все существующие
в городе автомобильные дороги. В память о кольцевых и радиальных дорогах разрешили двигаться
по площадке только двумя способами:

1. В сторону точки начала координат или от неё. При этом из точки начала координат разрешено двигаться в любом направлении.
2. Вдоль окружности с центром в начале координат и радиусом, который равен текущему расстоянию до начала координат.
Двигаться вдоль такой окружности разрешается в любом направлении (по или против часовой стрелки).
Вам, как ведущему программисту ответственной инстанции поручено разработать модуль,
который будет определять кратчайший путь из точки A, с координатами (xA, yA) в точку B с координатами (xB, yB).
Считайте, что менять направление движения можно произвольное количество раз, но оно должно
всегда соответствовать одному из двух описанных выше вариантов.

Формат ввода
В первой строке ввода заданы четыре целых числа xA, yA, xB и yB, по модулю не превосходящие 106.

Формат вывода
Выведите одно число — минимальное расстояние, которое придётся преодолеть по пути из точки A в точку B,
если не нарушать правил дорожного движения. Ваш ответ будет принят, если его абсолютная
или относительная погрешность не превосходит 10-6.

Пример 1
Ввод
0 5 4 3
Вывод
4.636476090008
Пример 2
Ввод
0 5 4 -3
Вывод
10.000000000000
'''

import math

def distance(xA, yA, xB, yB):
    start_radius = math.sqrt(xA**2 + yA**2)
    end_radius = math.sqrt(xB**2 + yB**2)

    start_angle = math.atan2(yA, xA)
    end_angle = math.atan2(yB, xB)

    angle_difference = abs(end_angle - start_angle)
    arc_length = min(angle_difference, 2 * math.pi - angle_difference) * start_radius

    straight_distance = abs(end_radius - start_radius)

    return straight_distance + arc_length


if __name__ == "__main__":
    xA, yA, xB, yB = map(int, input().split())
    print(distance(xA, yA, xB, yB))