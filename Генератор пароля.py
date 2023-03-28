import random
def generate_password(length, chars):
    dig_count = 1
    low_let = 1
    up_let = 1
    punct = 1
    punctuation = '!#$%&*+-=?@^_'
    #Проверка доступных символов
    for i in chars:
        if i.isdigit():
            dig_count = 0
        elif i.islower():
            low_let = 0
        elif i.isupper():
            up_let = 0
        for j in punctuation:
            if i == j:
                punct = 0
    dc = dig_count
    ll = low_let
    ul = up_let
    p = punct
    while dc * ll * ul * p == 0: #Генерируется пароль до тех пор пока в нем не будут все необходимые символы
        dc = dig_count
        ll = low_let
        ul = up_let
        p = punct
        chr = ''
        for _ in range(length):
            chr += random.choice(chars)
        for i in chr:
            if i.isdigit():
               dc += 1
            elif i.islower():
                ll += 1
            elif i.isupper():
                ul += 1
            for j in punctuation:
                if i == j:
                   p += 1
    return chr

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
min_length = 1
n = int(input('Количество паролей для генерации: '))
add_digit = input('Включить цифры? (да или нет) ').strip()
if add_digit.lower() == 'да':
    chars += digits
    min_length += 1
add_lowerletters = input('Включить прописные буквы? (да или нет) ').strip()
if add_lowerletters.lower() == 'да':
    chars += lowercase_letters
    min_length += 1
add_upperletters = input('Включить строчные буквы? (да или нет) ').strip()
if add_upperletters.lower() == 'да':
    chars += uppercase_letters
    min_length += 1
add_punctuation = input('Включить специальные символы !#$%&*+-=?@^_? (да или нет) ').strip()
if add_punctuation.lower() == 'да':
    chars += punctuation
    min_length += 1
remove_symbols = input('Исключить ли неоднозначные символы il1Lo0O? (да или нет) ').strip()
if remove_symbols.lower() == 'да':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')
length = list()
for i in range(n): #Выбор длины для паролей
    print('Введите длину пароля # ', i + 1,':', sep = '')
    length_password = int(input())
    if length_password < min_length: #Проверка на условие минимальной длины пароля
        while length_password < min_length:
            print('Минимальная длина пароля =', min_length, 'введите длину пароля не менее минимального значения')
            length_password = int(input())
    length.append(length_password)

for i in range(n):
    print(generate_password(length[i], chars))