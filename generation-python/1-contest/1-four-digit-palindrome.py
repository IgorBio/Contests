'''
Какое число загадал Тимур, если известно, что оно является четырёхзначным палиндромом,
и сумма его цифр совпадает с числом, образуемым первыми двумя цифрами?
'''


def get_number():
    for num in range(1000, 9999):
        if str(num) == str(num)[::-1] and sum(map(int, str(num))) == int(str(num)[:2]):
            print(num)
    return 0

if __name__ == '__main__':
    get_number()