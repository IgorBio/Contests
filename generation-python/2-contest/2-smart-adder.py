'''
Умный сумматор
Реализуйте вызываемый объект add(), который складывает целые числа при последовательных вызовах:

print(add(1))                # 1
print(add(1)(2))             # 3
Количество последовательных вызовов должно быть неограниченным:

print(add(1)(2)(3))          # 6
print(add(1)(2)(3)(4))       # 10
print(add(1)(2)(3)(4)(5))    # 15
Также должна быть возможность повторно использовать возвращаемые объектом add() значения:

add_two = add(2)

print(add_two)               # 2
print(add_two + 5)           # 7
print(add_two(3))            # 5
print(add_two(3)(5))         # 10
'''

class add(int):
    def __call__(self, value):
        return add(self + value)


if __name__ == '__main__':
    print(add(1))
    print(add(1)(2))
    print(add(1)(2)(3))
    print(add(1)(2)(3)(4))
    print(add(1)(2)(3)(4)(5))