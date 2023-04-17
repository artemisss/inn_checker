def validate_iin(iin: str) -> bool:
    iin = str(iin)
    if len(iin) != 12:
        print(f'Длина ИИН должна быть 12 символов, текущая длина: {len(iin)}')
        return False
    try:
        iin = list(map(int, iin))
    except ValueError:
        print('ИИН может содержать только цифры')
        return False
    control_sum = sum([(i + 1) * int(iin[i]) for i in range(11)]) % 11
    if control_sum == 10:
        control_sum = sum([(3 if i % 2 == 0 else 4) * int(iin[i]) for i in range(11)]) % 10
    if control_sum != int(iin[11]):
        print('Контрольное число ИИН неверное')
        return False
    return True






iin = '980412050397'
if validate_iin(iin):
    print(f'ИИН {iin} корректный')
else:
    print(f'ИИН {iin} некорректный')
