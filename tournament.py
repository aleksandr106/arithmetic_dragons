# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *
from random import randint, choice

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, enemy_list):
    for enemy in enemy_list:
        print('Вышел', enemy._color)
        while enemy.is_alive() and hero.is_alive():
            print('Вопрос:', enemy.question())
            answer = annoying_input_int('Ответ:')

            if enemy.check_answer(answer):
                hero.attack(enemy)
                print('Верно! \n** Враг кричит от боли **')
                hero._experience+=1
            else:
                enemy.attack(hero)
                print('Ошибка! \n** вам нанесён удар... ** \n','Ваше здоровье',hero._health)
                if hero._experience>0:
                    hero._experience-=1
        if enemy.is_alive():
            break
        print(enemy._color,  'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')





def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами и троллями!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())
        x=randint(1,7)
        enemy_number = x
        enemy_list = generate_enemy_list(enemy_number)
        assert(len(enemy_list) == x)
        print('У Вас на пути', enemy_number, 'врагов!')
        game_tournament(hero, enemy_list)
    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
