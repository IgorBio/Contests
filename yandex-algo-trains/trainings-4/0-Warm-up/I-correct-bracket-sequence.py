'''
Правильная скобочная последовательность
Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок.
Программа должна определить, является ли данная скобочная последовательность правильной.
Пустая последовательность является правильной. Если A — правильная,
то последовательности (A), [A], {A} — правильные.
Если A и B — правильные последовательности, то последовательность AB — правильная.

Формат ввода
В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.

Формат вывода
Если данная последовательность правильная, то программа должна вывести строку "yes", иначе строку "no".

Пример 1
Ввод
()[]
Вывод
yes
Пример 2
Ввод
([)]
Вывод
no
Пример 3
Ввод
(
Вывод
no
'''

def correct_bracket_sequence(sequence: str) -> bool:
    if not sequence:
        return True
    
    length = len(sequence)

    if length % 2:
        return False
    
    stack = []
    m = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != m[char]:
                return False

    return True if not stack else False
    

if __name__ == "__main__":
    sequence = input()
    print('yes' if correct_bracket_sequence(sequence) else 'no')