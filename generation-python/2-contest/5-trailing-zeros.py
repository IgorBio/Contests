'''
Реализуйте функцию trailing_zeros(), которая принимает один аргумент: n – неотрицательное целое число (0≤n≤10^9)
Функция должна возвращать количество нулей в конце записи факториала числа n.
'''

def trailing_zeros(n):
    if n == 0:
        return 0
    return n // 5 + trailing_zeros(n // 5)


if __name__ == '__main__':
    assert trailing_zeros(0) == 0
    assert trailing_zeros(4) == 0
    assert trailing_zeros(5) == 1
    assert trailing_zeros(10) == 2
    assert trailing_zeros(50) == 12
    assert trailing_zeros(500) == 124
    assert trailing_zeros(10000) == 2499
    assert trailing_zeros(10**5 + 1) == 24999
    assert trailing_zeros(10**6 + 1) == 249998
    assert trailing_zeros(10**8 + 999) == 25000245