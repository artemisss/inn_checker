import csv


def validate_iins_from_csv(file_path: str) -> str:
    output_rows = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for iin in reader:
            if validate_iin(iin[0]):
                gender = get_gender_from_iin(iin[0])
                output_rows.append([iin[0], 'True', gender])
            else:
                output_rows.append([iin[0], 'False', 'Unknown'])

    output_file = 'output.csv'
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(output_rows)

    return output_file


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

def get_gender_from_iin(iin: str) -> str:
    seventh_digit = int(iin[6])
    if seventh_digit == 1 or seventh_digit == 3:
        return 'male'
    elif seventh_digit == 2 or seventh_digit == 4:
        return 'female'
    elif seventh_digit == 5:
        return 'male' if int(iin[0:2]) < 22 else 'unknown'
    elif seventh_digit == 6:
        return 'female' if int(iin[0:2]) < 22 else 'unknown'
    else:
        return 'unknown'


input_file = 'iins.csv'
output_file = validate_iins_from_csv(input_file)
print(f'Результат проверки ИИНов сохранен в файл: {output_file}')
