import random
import time
import os

print("Привет, давай сыграем с тобой в одну занимательную игру!")
print("Чтобы начать игру нажмите enter ")
# input()
fs = open("baza.txt", encoding="Windows-1251")
a = fs.readlines()
ps = []
for b in a:
    ps.append(b[:-1])  # убирает enter
print(ps)
otvet=4
points=0
n = 2
while otvet!=0:
    n = n + 1
    ne = (random.sample(ps, n))  # выбирает несколько слов рандомно
    print(ne)
    time.sleep(5)
    os.system('cls')
    input()
    i = input('Вводите слова через пробел: ').split()
    print(i)
    k = 0
    for e in ps:
        if e in i:
            k += 1
    print(k)
    points =points+k
    otvet =int(input("Если хотите закончить игру нажмите 0:  "))
print("Поздравляю, ваше количество очков составило: ")
print(points)  # конец игры,вывод очков
