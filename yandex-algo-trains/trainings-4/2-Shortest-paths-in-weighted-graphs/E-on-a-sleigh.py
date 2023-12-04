'''
На санях
В начале XVIII века еще не было самолетов, поездов и автомобилей, поэтому все междугородние зимние поездки совершались на санях.
Как известно, с дорогами в России тогда было даже больше проблем, чем сейчас,
а именно на N существовавших тогда городов имелась N-1 дорога, каждая из которых соединяла два города.
Из каждого города можно было добраться в любой другой (возможно, через промежуточные города).
В каждом городе была почтовая станция («ям»), на которой можно было пересесть в другие сани.
При этом ямщики могли долго запрягать (для каждого города известно время, которое ямщики в этом городе тратят на подготовку саней к поездке)
и быстро ехать (также для каждого города известна скорость, с которой ездят ямщики из него).
Можно считать, что количество ямщиков в каждом городе не ограничено.

Если бы олимпиада проводилась 300 лет назад, то путь участников занимал бы гораздо большее время, чем сейчас.
Допустим, из каждого города в Москву выезжает участник олимпиады и хочет добраться до Москвы за наименьшее время
(не обязательно по кратчайшему пути: он может заезжать в любые города, через один и тот же город можно проезжать несколько раз).
Сначала он едет с ямщиком из своего города. Приехав в любой город, он может либо сразу ехать дальше, либо пересесть.
В первом случае он едет с той же скоростью, с какой ехал раньше. Если сменить ямщика, он сначала ждет, пока ямщик подготовит сани,
и только потом едет с ним (с той скоростью, с которой ездит этот ямщик). В пути можно делать сколько угодно пересадок.

Определите, какое время необходимо, чтобы все участники олимпиады доехали из своего города в Москву 300 лет назад.
Все участники выезжают из своих городов одновременно.

Формат ввода
В первой строке входного файла дано натуральное число N, не превышающее 2000 — количество городов, соединенных дорогами.
Город с номером 1 является столицей. Следующие N строк содержат по два целых числа: Ti и Vi —
время подготовки саней в городе i, выраженное в часах, и скорость, с которой ездят ямщики из города i, в километрах в час (0≤Ti≤100, 1≤Vi≤100).
Следующие N–1 строк содержат описания дорог того времени. Каждое описание состоит из трех чисел Aj, Bj и Sj, где Aj и Bj —
номера соединенных городов, а Sj — расстояние между ними в километрах (1≤Aj≤N, 1≤Bj≤N, Aj≠Bj, 1≤Sj≤10000).
Все дороги двусторонние, то есть если из A можно проехать в B, то из B можно проехать в A.
Гарантируется, что из всех городов можно добраться в столицу.

Формат вывода
Сначала выведите одно вещественное число — время в часах, в которое в Москву приедет последний участник.
Далее выведите путь участника, который приедет самым последним (если таких участников несколько, выведите путь любого из них).
Выведите город, из которого этот участник выехал первоначально, и перечислите в порядке посещения те города, в которых он делал пересадки.
Последовательность должна заканчиваться столицей.

При проверке ответ будет засчитан, если из трех величин «время путешествия по выведенному пути»,
«выведенное время» и «правильный ответ» каждые две отличаются менее чем на 0.0001.

Пример 1
Ввод
4
1 1
10 30
5 40
1 10
1 2 300
1 3 400
2 4 100
Вывод
31.0000000000
4 2 1

Пример 2
Ввод
3
1 1
0 10
0 55
1 2 100
2 3 10
Вывод
3.0000000000
2 3 1

Примечания
1. Участник из города 1 уже находится на своем месте и тратит на дорогу 0 часов. Участник из города 2 ждет 10 часов ямщика в своем городе,
а затем проезжает 300 км от города 2 до города 1 за 10 часов, т.е. тратит на дорогу 20 часов.
Участник из города номер 3 ждет ямщика 5 часов, а затем доезжает до города 1 за 10 часов, т.е. тратит на дорогу 15 часов.
Участник из города 4 может доехать до города 1 с ямщиком из города 4 за 1 + 40 = 41 час или доехать до города номер 2 за 1 + 10 = 11 часов,
прождать там 10 и доехать до столицы за 10 часов. Таким образом, он может добраться до города 1 минимум за 31 час.
Это и есть самое большое время и ответ к задаче.

2. Участнику из города 2 выгоднее добраться сначала до третьего города, где ездят быстрее,
а потом поехать в столицу, не делая пересадки в своём городе.
'''

