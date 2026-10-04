#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

def numbers_to_letters(text):
    tokens = text.split(' ')

    result = []
    for token in tokens:
        if token.isdigit():
            num = int(token)
            if num == 0:
                result.append(' ')
            elif 1 <= num <= 26:
                result.append(chr(num + 96))
            else:
                result.append(token)
        else:
            result.append(token)

    return ''.join(result)


print(numbers_to_letters("8 5 12 12 15"))
