import string


def check_pass(pwd):

    err = {
    'length': 'Длина пароля не равна 8 символам',
    'upper': 'Отсутствуют заглавные буквы',
    'lower': 'Нет строчных букв в пароле',
    'digits': 'Нет цифр в пароле',
    'spec': 'Отсутствуют спецсимволы в пароле',
    'bad_symbols': 'В пароле использованы непредусмотренные символы'
    }

    if len(pwd) == 8:
        err.pop('length')

    if pwd.lower() != pwd:
        err.pop('upper')

    if pwd.upper() != pwd:
        err.pop('lower')

    if any(map(str.isdigit, pwd)):
        err.pop('digits')

    if ('' in pwd) or ('-' in pwd) or ('#' in pwd):
        err.pop('spec')

    allowed_sym = string.ascii_uppercase + string.ascii_lowercase + string.digits + '-#'

    if (set(pwd) - set(allowed_sym)) == set():
        err.pop('bad_symbols')

    if len(err) == 0:
        print('Пароль идеален')
    else:
        print(err.values(), sep=';ы ')


# # Тесты
check_pass('qwerty')
# check_pass('@#@@u')
# check_pass('Tr56#2@@')
# check_pass('qwerty11')
# check_pass('11qweQ-s') 