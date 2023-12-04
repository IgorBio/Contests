'''
Чей подарок?
Эльфы помогают Санта Клаусу: подписывают подарки, чтобы он ничего не напутал.
Но что-то пошло не так! На одном из подарков написали вот такую абракадабру:

ЗЖ АЮДЮЖФВ, АДЗВ Б ЗРЮЖХ ЖЮ ДЧЪБЛ ЙЗЯЭЮКЛЫЗ. 😱

Помогите Санте понять, что пытались написать эльфы и кому предназначен этот подарок!
'''


def cesar_cipher(text, shift):
    alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ''
    for char in text:
        if char in alphabet:
            index = (alphabet.index(char) + shift) % len(alphabet)
            result += alphabet[index]
        else:
            result += char
    return result


if __name__ == '__main__':
    encrypted_message = "ЗЖ АЮДЮЖФВ, АДЗВ Б ЗРЮЖХ ЖЮ ДЧЪБЛ ЙЗЯЭЮКЛЫЗ."
    print(cesar_cipher(encrypted_message, 7))