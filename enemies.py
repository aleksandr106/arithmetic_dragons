# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice
import random

class Enemy(Attacker):
    pass

def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy

def generate_enemy_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list

class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer
    def check_answer(self, answer):
        return answer == self.__answer

class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer
    def check_answer(self, answer):
        return answer == self.__answer

class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 300
        self._attack = 20
        self._color = 'красный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 150
        self._attack = 40
        self._color = 'чёрный дракон'

    def question(self):
        x = randint(2,20)
        y = randint(2,20)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest
class ПещерныйTroll(Troll):
    def __init__(self):
        self._health = 150
        self._attack = 5
        self._color='пещерный тролль'
    def question(self):
        x = randint(1,6)
        self.__quest ='Угадай число от 1 до 5'
        self.set_answer(x)
        return self.__quest
class ГорныйTroll(Troll):
    def __init__(self):
        self._health = 250
        self._attack = 25
        self._color='горный тролль'
    def question(self):
        x = randint(2,100)
        self.__quest = 'Простое ли число '+str(x)+('?(1-да,0-нет)')
        y=1
        for i in range (2,x//2+1):
            if x%i==0:
                y=0
        self.set_answer(y)
        return self.__quest
class ЛеснойTroll(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 100
        self._color='лесный тролль'
    def question(self):
        x = randint(2,100)
        self.__quest ='Напишите  в порядке возрастания множители числа '+str(x)+('(без пробелов и запятых)')
        y=''
        i=2
        while x>1:
            if x%i==0:
                y=y+str(i)
                x=x//i
            else:
                i+=1
        self.set_answer(int(y))
        return self.__quest

enemy_types =  [GreenDragon,RedDragon,BlackDragon,ГорныйTroll,ЛеснойTroll,ПещерныйTroll]


