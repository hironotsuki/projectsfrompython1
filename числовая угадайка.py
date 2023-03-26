import random # импортирую модуль random

start = input('Добро пожаловать в числовую угадайку! Начать игру? (y - да, n - нет): ') # спрашиваю начинать ли игру

def is_valid(num, x): # функция, которая проверяет, входит ли введенное число в рамки заданного (от 1 до заданного)
    if num.isdigit() == True and int(num) >= 0 and int(num) <= x:
        return True
    else:
        return False


def continue_game(a): # проверка на продолжение игры
    if a == 'y':
        return True
    else:
        return False


def game(): # сама игра
    count = 1 # счётчик для кол-ва попыток
    if start == 'y':
        x = int(input('Введите число, до которого будем угадывать: ')) # заданное число
        number = random.randint(1, x)
        while True:
            data = input(f'Введите число от 1 до {x}: ')
            type = is_valid(data, x)
            if type == False:
                print(f'А может быть все-таки введем целое число от 1 до {x}?')
                data = input(f'Введите число от 1 до {x}: ')
            if type == True:
                data = int(data)
            if data < number:
                print('Ваше число меньше загаданного, попробуйте ещё разок')
                count += 1
                continue
            elif data > number:
                print('Ваше число больше загаданного, попробуйте ещё разок')
                count += 1
                continue
            elif data == number:
                print('Вы угадали, поздравляем!')
                print('Спасибо, что играли в числовую угадайку! Вы угадали за', count, 'попыток!')
                replay = input('Сыграть ещё? (y - да, n - нет): ') # запрос на продолжение
                if continue_game(replay) == True:
                    game()
                else:
                    print('Жаль... До новых встреч!')
                    break
            break
    elif start == 'n':
        print('Как жаль. Пока...')


game() # вызов функции (игры)



