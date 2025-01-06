import random

right = int(input('Введите правую границу диапазона '))
guess = random.randint(1, right)
print('Добро пожаловать в числовую угадайку')


def is_valid(number):
    if 1 <= int(number) <= right and number.isdigit():
        return True
    else:
        return False


# print(guess)  тут можно посмотреть рандомное число

counter = 0
while True:
    askUser = input(f'Введите число от 1 до {right} ')
    if is_valid(askUser):
        askUser = int(askUser)

        if askUser < guess:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            counter += 1
        elif askUser > guess:
            print('Ваше число больше загаданного, попробуйте еще разок')
            counter += 1
        else:
            print('Вы угадали, поздравляем!')
            print(f'Вам потребовался {counter + 1} раз чтобы угадать')
            break
    else:
        print(f'А может быть все-таки введем целое число от 1 до {right}?')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
