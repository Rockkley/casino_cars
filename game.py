from ast import While
import random
import time
from random import randint

class Vehicle(object):
    def __init__(self, id, name, speed, distance, win):
        self.id = id
        self.name = name
        self.speed = speed
        self.distance = distance
        self.win = win

    def start(self):
        print(f'{self.name} стартует!\n')

    def new_speed(self, boost):
        self.speed += boost

    def stop(self):
        print(f'Машина остановилась')

    def winner(self):
        print(f'{self.name} выиграл и проехал {self.distance} метров')
        self.win = 1

    def loser(self):
        print(f'{self.name} проиграл и проехал {self.distance} метров')
        self.win = 0
    
bank = 1000

car_one = Vehicle('1', 'УАЗ', 1, 0, 0)
car_two = Vehicle('2', 'Camry', 1, 0, 0)

def race():

    global bank

    print(f'Выберите машину:\n1) "УАЗ"\n2) "Camry"')
    car_selected = input()

    while True:
        if car_selected not in ('1','2'):
            print(f'Выберите машину:\n1) "УАЗ"\n2) "Camry"')
            car_selected = input()
        else:
            break
        
    print(f'Ваш банк: {bank}\nВведите вашу ставку:')
    bet = input()

    while True:
        if int(bet) > bank:
            print(f'У вас нет столько денег!\nВведите другую сумму!{bank}')
            bet = input()
        else:
            break
    
    print('\n')

    car_one.start()
    car_two.start()

    for i in range (11):

        boost = randint(5, 15)
        car_one.new_speed(boost=boost)
        car_one.distance = i * car_one.speed

        boost = randint(5, 15)
        car_two.new_speed(boost=boost)
        car_two.distance = i * car_two.speed

        print(f'{i} секунда')

        if car_one.distance > car_two.distance:
            print( f'{car_one.name} лидирует со скоростью {car_one.speed}\nПройденное расстояние: {car_one.distance} метра')

        elif car_one.distance < car_two.distance:
            print( f'{car_two.name} лидирует со скоростью {car_two.speed}\nПройденное расстояние: {car_one.distance} метра')

        else:
            print(f'Удивительно, но оба автомобиля идут ноздря в ноздрю')

        print('---------------------------------------------------------------------------')
        time.sleep(3)

    if car_one.distance>car_two.distance:
        car_one.winner()
        car_two.loser()
    else:
        car_two.winner()
        car_one.loser()

    time.sleep(3)

    if car_selected == car_one.id and car_one.win == 1:
        cost = int(bet) * 0.25
        bank = bank + cost
        print(f'\nВаша машина выиграла!\nВаш выигрыш составил {cost}$\nВаш банк в данный момент составляет {bank}$')
    else:
        bank = bank - int(bet)
        print(f'Вы проиграли(\nВаш банк в данный момент составляет {bank}$')

    car_one.speed = 1
    car_two.speed = 1
    car_one.distance = 0
    car_two.distance = 0

while True:
    race()
    print('Ещё?')
    txt = input()
    if txt == 'Да':
        race()
    if txt == 'Нет':
        print('Конец игры!')
        break

print('123')