import random
from random import randint

k = 50
c = 50
r = 50
m = 50
t = 0
d = {'Не хотите ли вы сегодня посетить нермех?': [['Да', 3, -3, -10, 0], ['Нет', -3, -3, 5, 0]],'Сегодня на нермехе будут проходить …, не хотите ли посетить занятия?': [['Да', 5, 5, 5, 0],['Нет', -5, -5, -5, 0]],'Вы прекрасно справляетесь с учебной нагрузкой. Не хотите ли пойти на кафедру теоретической физики': [['Да', 10, -5, 10, -10], ['Нет', -3, 5, 5, 10]]}
vls = d.values()
lst = list(d.keys())

while (0 < k < 100) & (0 < c < 100) & (0 < r < 100) & (0 < m < 100):
    i = randint(0, len(d) - 1)
    t +=1

    print(lst[i])
    answers = d[str(lst[i])]
    answer_1 = answers[0]
    answer_2 = answers[1]

    print(answer_1[0])
    print(answer_2[0])
    ans = int(input())

    if ans == 0:
        k = k + answer_1[1]
        c = c + answer_1[2]
        r = r + answer_1[3]
        m = m + answer_1[4]

    elif ans == 1:
        k += answer_2[1]
        c += answer_2[2]
        r += answer_2[3]
        m += answer_2[4]

    print(k, c, r, m)
    print('неделя', t)
print('Конец')