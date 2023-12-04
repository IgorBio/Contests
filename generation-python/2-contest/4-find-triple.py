'''
Даны три положительных целых числа a, b, c.  Вычисляются их всевозможные суммы: a + b, a + c, b + c, a + b + c.
Эти суммы и сами числа a, b, c в произвольном порядке записываются в список nums.

Реализуйте функцию find_triple(), которая принимает один аргумент:

nums – указанный выше список чисел, содержащий числа a, b, c, a + b, a + c, b + c, a + b + c в произвольном порядке.
Функция должна вернуть список, состоящий из трех начальных чисел a, b и c.
Числа в списке должны быть расположены в порядке неубывания.
'''

def find_triple(nums):
    a, b, *rest, mx = sorted(nums)
    return [a, b, mx - a - b]

if __name__ == '__main__':
    assert find_triple([3, 1, 8, 4, 5, 7, 4]) == [1, 3, 4]
    assert find_triple([2, 1, 2, 1, 1, 3, 2]) == [1, 1, 1]
    assert find_triple([5, 2, 7, 3, 6, 1, 4]) == [1, 2, 4]
    assert find_triple([300000000, 600000000, 300000000, 600000000, 300000000, 600000000, 900000000]) == [300000000, 300000000, 300000000]
    assert find_triple([1, 3, 2, 5, 2, 3, 4]) == [1, 2, 2]
    assert find_triple([999999999, 1, 2, 999999998, 1000000000, 999999999, 1]) == [1, 1, 999999998]
    assert find_triple([8633036, 9062130, 11196828, 2134698, 17695166, 19829864, 10767734]) == [2134698, 8633036, 9062130]
    assert find_triple([10708035, 4802079, 4655456, 15363491, 9457535, 10561412, 5905956]) == [4655456, 4802079, 5905956]
    assert find_triple([9016735, 433464, 10047451, 9613987, 9450199, 597252, 1030716]) == [433464, 597252, 9016735]
    assert find_triple([1169701, 171665, 4567418, 3226052, 4395753, 3397717, 1341366]) == [171665, 1169701, 3226052]