# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
#  чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

def now_turn(swt: int, player: int):
    player_move = int(input(f'{player} игрок, сейчас Ваш ход. на столе {swt} конфет. Сколько конфет вы возьмете? '))
    while (player_move <= 0) or (player_move > 28):
        player_move = int(input("Количество конфет за 1 раз должно быть от 1 до 28: "))
    swt -= player_move
    if swt > 0:
        if player == 2:
            now_turn(swt, 1)
        else:
            now_turn(swt, 2)
    else:
        print(f'Игрок №{player}, вы победили!!!')
    
from random import randint
sweets = 2021
now_playing = randint(1,2)
print('Начнем игру!')
print(f'Игру начинает игрок номер {now_playing}')
now_turn(sweets, now_playing)
