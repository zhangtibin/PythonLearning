#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-

import os

a = 12
b = "30"
print(a)
firstLetter = "I"
secondLetter = " Love"
thirdLetter = " You"
totalLetter = firstLetter + secondLetter + thirdLetter
print(totalLetter)
print(firstLetter + secondLetter + thirdLetter)
print(thirdLetter.upper())
print(secondLetter.lower())
c = int(b)
print(a+c)
words = "words " * 3
print(words)

word = "a loooooong word"
num = 12
string = 'bang!'
total = string * (len(word) - num)
print(total)
print(total[0])
print(total[-2])
print(total[-3:-1])
print(total[6:18])
print(total[8:])
print(total[:9])
phone_number = "132-4823-8953"
hiding_number = phone_number.replace(phone_number[:9], '*'*9)
print(hiding_number)
search = "168"
num_a = "1386-168-0006"
num_b = "1681-222-0006"
print(search + ' is at ' + str(num_a.find(search)) + ' to ' + str(num_a.find(search)) + ' of num_a')
print('{} a word she can get what she {} for.'.format('with', 'came'))
print('{preposition} a word she can get what she {verb} for.'.format(preposition = 'with', verb = 'came'))
print('{0} a word she can get what she {1} for.'.format('with', 'came'))
'''
city = input("write down the name of city:")
url = "https://www.sojson.com/open/api/weather/json.shtml?city={}".format(city)
'''
m = 10
n = 2
h = 8
S = (m + n) * h/2
print(S)
def areaCalculator(le, pe, qe):
    return (le + pe) * qe / 2
print(areaCalculator(10, 12, 4))

def weight_transfor(w):
    return w / 1000.0
print(str(weight_transfor(2308)) + ' kg')

def trapezoid_area(base_up, base_down, height):
    return 1 / 2 * (base_up + base_down) * height
print(trapezoid_area(1, 2, 3))
def text_create(name, msg):
    full_path = '/Users/zhangtibin/Desktop/ios.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')
text_create('Hello', 'Hello World, No deceive！')
def text_filter(word,censored_word = 'lame', change_word = 'Awesome'):
    return word.replace(censored_word, change_word)
text_filter('Python is lame !')
def censored_text_create(name, msg):
    clean_msg = text_filter(msg)
    text_create(name, clean_msg)
censored_text_create('Try', 'lame!lame!lame!')
album = ['Black Star','David Bowie',25,True]
print(album)
album.append('new song')
print(album)
print(album[2])
print(album[-1])
print(bool('Black Star' in album))
'''
def account_login():
    password = input('Password:')
    if password == '12345':
        print ('Login Success!')
    else:
        print ('Wrong password or invalid input!')
account_login()

def account_login():
    password = input('Password:')
    password_correct = password == "123"
    if password_correct:
        print ('Login success!')
    else:
        print ('Wrong password or invalid input!')
        account_login()
account_login()
'''

password_list = ['*#*#', '123']
def account_login():
    tries = 3
    while tries > 0:
        password = input('Password:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]
        if password_correct:
            print('Login success!')
        elif password_reset:
            new_password = input('Enter a new password:')
            password_list.append(new_password)
            print('Your password has changed successfully!')
            account_login()
        else:
            print('Wrong password or invalid input!')
            tries = tries - 1
            print(tries, 'times left')
    print('Your account has been suspended')
account_login()

for every_letter in 'Hello world':
    print(every_letter)
count = 10
while count >= 3:
    print(count)
    count = count - 1

import random

def roll_dice(numbers=3, points=None):
    print('<<<<<< ROLL THE DICE! >>>>>>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1, 7)
        points.append(point)
        numbers = numbers - 1
    return points

def roll_result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10
    if isBig:
        return 'Big'
    else:
        return 'Small'

def start_game():
    print('<<<<<<<<< GAMES STARTS! >>>>>>>>>>>')
    choices = ['Big', 'Small']
    your_choice = input('Big or Small:')
    if your_choice in choices:
        points = roll_dice()
        total = sum(points)
        youWin = your_choice == roll_result(total)
        if youWin:
            print('The points are', points, 'you win!')
        else:
            print('The points are', points, 'you lose!')
    else:
        print('Invalid Words!')
        start_game()
start_game()
weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(weekday)
all_in_list = [
    1,                  # 整数
    1.0,                # 浮点数
    'a word',           # 字符串
    print(1),           # 函数
    True,               # 布尔值
    [1, 2],             # 列表中套列表
    (1, 2),             # 元组
    {'key': 'value'}    # 字典
]
print(all_in_list)
weekday.insert(5, 'Sunday')
print(weekday)
weekday.insert(5, 'Saturday')
print(weekday)
weekday.remove('Friday')
print(weekday, weekday[3])
NASDAQ_Code = {'BAIDU': 'Baidu',
               'SINA': 'Sina',
               'FB': 'FaceBook'}
print(NASDAQ_Code)
print(NASDAQ_Code['FB'])
NASDAQ_Code.update({'BAIDU': 'baidu'})
del NASDAQ_Code['FB']
print(NASDAQ_Code)
a_set = {1, 2, 3, 4}
print(a_set)
a_set.add(5)
print(a_set)
a_set.add(3)
print(a_set)
a_set.discard(2)
print(a_set)
num_list = [1, 4, 2, 6, 8, 3, 5]
print(sorted(num_list))
print(sorted(num_list, reverse=True))

import time
a = []
t0 = time.clock()
for i in range(1, 2000):
    a.append(i)
print(time.clock() - t0, "seconds process time")
t0 = time.clock()
b = [i for i in range(1, 2000)]
print(time.clock() - t0, "seconds process time")

import string

lyric = 'The night begin to shine, the night begin to shine'
words = lyric.split()

class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']
    def drink(self, how_much):
        if how_much == 'a sip':
            print('Cool')
        elif how_much == 'whole bottle':
            print('Headache!')
        print('Energy!')
    def __init__(self):
        self.local_logo = '可口可乐'
ice_coke = CocaCola()
print(ice_coke.drink('a sip'))
coke = CocaCola()
print(coke.local_logo)
coke_for_me = CocaCola()
coke_for_you = CocaCola()
print(CocaCola.formula)
print(coke_for_me.formula)
print(coke_for_you.formula)
for element in coke_for_me.formula:
    print(element)
coke_for_China = CocaCola
coke_for_China.local_logo = '可口可乐'
print(coke_for_China.local_logo)
class TestA:
    attr = 1
obj_a = TestA()
obj_b = TestA()
TestA.attr = 42
print(obj_a.attr)
print(obj_b.attr)
print(TestA.__dict__)
round(1.234)    # 保留一位小数的四舍五入
round(1.234, 2) # 保留两位小数的四舍五入
abs(-10)        # 绝对值
pow(2, 3)       # 2的3次幂

import math
math.floor(32.8)    # 取整
math.sqrt(4)        # 开平方

import sys
try:
    file = open('ios.txt', 'w')
    sys.stdout = file
    print('hhhhhhh')
finally:
    if not file:
        file.close()





