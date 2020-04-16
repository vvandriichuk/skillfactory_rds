import numpy as np

# random_number = np.random.randint(1, 101)  # загадали число
random_number = np.random.randint(1, 101)  # загадали число


def game_core_v1(number):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток"""
    # print(f'Загадано число {number}')
    count = 0

    while True:
        # print(f'Попытка {count}')
        count += 1
        predict = np.random.randint(1, 101)  # установим число первой попытки случайным образом
        # print(f'Предполагаю число {predict}')
        if number == predict:
            # return f'Угадано за {count} попыток'  # выход из цикла, если угадали
            # print(f'Попыток: {count}')
            return count  # выход из цикла, если угадали


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
        больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток"""
    # print(f'Загадано число {number}')
    count = 0
    predict = np.random.randint(1, 101)  # установим число первой попытки случайным образом
    while number != predict:

        count += 1

        if number > predict:
            predict += 1

        else:
            predict -= 1

    return count  # выход из цикла, если угадали


def game_core_v3(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в на половину разницы между угадываемым и текущим
       Функция принимает загаданное число и возвращает число попыток"""
    # print(f'Загадано число {number}')
    count = 0
    predict = np.random.randint(1, 101)  # установим число первой попытки случайным образом
    # print(f'Загаданное число {number}')
    # print(f'Начинаю отгадывать с числа {predict}')
    while number != predict:

        count += 1

        if number > predict:
            if number - predict == 1:
                predict += 1
                # print(predict)
            else:
                predict += int((number - predict) // 2)
                # print(predict)
        else:
            if predict - number  == 1:
                predict -= 1
                # print(predict)
            else:
                predict -= int((predict - number) // 2)

    # print(f'Угадано за {count} попыток')
    return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""

    count = 0
    result = []
    while count < 100:
        result.append(game_core(random_number))
        count += 1
        # print(count)
        # print(result)
    score = int(np.mean(result))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# запускаем
score_game(game_core_v3)

# print(game_core_v1(random_number))
