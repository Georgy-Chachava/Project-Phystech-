import pygame
import random as rnd
from CharacterS import *
from Images import *
from REPLICS import *
import pygame.font
from pygame.draw import *
from visual import *

WHITE = (255, 255, 255)


def click(event, active_character):
    if event.pos[0] < 200:
        ans = 0
    elif event.pos[0] >= 200:
        ans = 1
    active_character = None
    return ans, active_character


pygame.init()
screen = pygame.display.set_mode((400, 670))
screen.fill(0xaaaa55)

text = pygame.font.Font('Fonts/futurabkbtrusbyme_book.otf', 18)
text_2 = pygame.font.Font('Fonts/futurabkbtrusbyme_book.otf', 16)

pygame.display.set_caption("Reigns")
bg_color = (0xaaaa55)
clock = pygame.time.Clock()

Kiselev = Character(screen, kiselev_image, kiselevs_replics, name='Киселёв')
Getc = Character(screen, getc_image, getc_replics, name='Гец')
Ivanov = Character(screen, ivanov_image, ivanov_replics, name='Иванов')
PE_teacher = Character(screen, pe_teacher_image, pe_teacher_replics, name='Учитель Физкультуры')
BGD_teacher = Character(screen, bgd_teacher_image, bgd_teacher_replics, name='Учитель БЖД')
Groupmate = Character(screen, groupmate_image, groupmate_replics, name='Одногрупник')
Dekanat = Character(screen, dekanat_image, dekanat_replics, name='Деканат')
Senator = Character(screen, senator_image, senator_replics, name='Сенатор')
English_teacher = Character(screen, english_teacher_image, english_teacher_replics, name='Учитель Английского')
Best_friend = Character(screen, best_friend_image, best_friend_replics, name='Лучший друг')
Roommate = Character(screen, roommate_image, roommate_replics, name='Сосед по комнате')
Gavrikov = Character(screen, gavrikov_image, gavrikov_replics, name='Гавриков')
Showerman = Character(screen, showerman_image, showerman_replics, name='Шаурмятник')
Cat = Character(screen, cat_image, cat_replics, name='Кошка')
Khiryanov = Character(screen, khirianov_image, khirianov_replics, name='Хирьянов')
Paukov = Character(screen, paukov_image, paukov_replics, name='Пауков')
Agent_FPMI = Character(screen, agent_FPMI_image, agent_FPMI_replics, name='Агент ФПМИ')
Koldunov = Character(screen, koldunov_image, koldunov_replics, name='Колдунов')

Malo_k = Character(screen, otlchislen_image, malo_k_replics)
Malo_c = Character(screen, otshelnik_image, malo_c_replics)
Malo_r = Character(screen, death_image, malo_r_replics)
Malo_m = Character(screen, death_image, malo_m_replics)
Mnogo_k = Character(screen, death_image, mnogo_k_replics)
Mnogo_c = Character(screen, otlchislen_image, mnogo_c_replics)
Mnogo_r = Character(screen, otlchislen_image, mnogo_r_replics)
Mnogo_m = Character(screen, money_image, mnogo_m_replics)
All_good = Character(screen, all_good_image, all_good_replics)
Winner = Character(screen, winner_image, winner_replics)

Death = [Malo_k, Malo_c, Malo_r, Malo_m, Mnogo_k, Mnogo_c, Mnogo_r, Mnogo_m, All_good, Winner]

NPC = [Kiselev, Roommate, Ivanov, PE_teacher, BGD_teacher, Groupmate, Dekanat, Senator, English_teacher,
       Best_friend, Roommate, Gavrikov, Showerman, Cat, Khiryanov, Paukov, Agent_FPMI]

finished = False
ans = None
active_character = None
cursor_position = 5000
k = 50
c = 50
r = 50
m = 50
t = 0
record = 0
death_count = 0
number_death = 10

new_session()

while not finished:

    clock.tick(60)

    screen.fill(0xaaaa55)

    rect(screen, (0x202020), (0, 0, 400, 80))
    rect(screen, (0x202020), (0, 550, 400, 120))

    rect(screen, (0x252530), (110, 20, 50, 12))
    rect(screen, (0x000000), (108, 18, 54, 16), 2)

    rect(screen, (0x252530), (110, 50, 50, 12))
    rect(screen, (0x000000), (108, 48, 54, 16), 2)

    rect(screen, (0x252530), (290, 20, 50, 12))
    rect(screen, (0x000000), (288, 18, 54, 16), 2)

    rect(screen, (0x252530), (290, 50, 50, 12))
    rect(screen, (0x000000), (288, 48, 54, 16), 2)

    teK = text.render('Знания', True, (255, 255, 255))
    screen.blit(teK, (20, 13))
    teK = text.render('Общение', True, (255, 255, 255))
    screen.blit(teK, (20, 43))
    teK = text.render('Отдых', True, (255, 255, 255))
    screen.blit(teK, (200, 13))
    teK = text.render('Деньги', True, (255, 255, 255))
    screen.blit(teK, (200, 43))

    if (number_death != 10) and (t > 0):
        active_character = Death[number_death]
        d = active_character.replics
        i = 0
        t = -1

    if t == 0:
        active_character = Koldunov
        d = active_character.replics
        number_death = 10
        i = 0
        k = 50
        c = 50
        r = 50
        m = 50

    elif t > 0:
        if active_character == None:
            index = rnd.randint(0, len(NPC) - 1)
            active_character = NPC[index]
            d = active_character.replics
            i = rnd.randint(0, len(d) - 1)

    lst = list(d.keys())
    answers = d[str(lst[i])]
    answer_1 = answers[0]
    answer_2 = answers[1]

    active_character.output()

    #split_text(screen, 60, 205, str(answer_1[0]), 15, 16, WHITE)

    teK = text.render(active_character.name, True, (50, 50, 50))
    screen.blit(teK, (40, 510))

    #split_text(screen, 230, 205, str(answer_2[0]), 14, 16, WHITE)

    if t < 0:
        teK = text.render('Игра окончена! Ваш рекорд:', True, (255, 255, 255))
        screen.blit(teK, (20, 620))
        teK = text.render(str(record), True, (255, 255, 255))
        screen.blit(teK, (260, 620))

    else:
        teK = text.render('Недель на Физтехе:', True, (255, 255, 255))
        screen.blit(teK, (20, 620))
        teK = text.render(str(t + 1), True, (255, 255, 255))
        screen.blit(teK, (185, 620))

    split_text(screen, 20, 110, str(lst[i]), 39, 18, WHITE)

    k_1 = k // 2
    c_1 = c // 2
    r_1 = r // 2
    m_1 = m // 2

    rect(screen, (0xffffff), (110, 20, k_1, 12))
    rect(screen, (0xffffff), (110, 50, c_1, 12))
    rect(screen, (0xffffff), (290, 20, r_1, 12))
    rect(screen, (0xffffff), (290, 50, m_1, 12))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ans, active_character = click(event, active_character)
        elif event.type == pygame.MOUSEMOTION:
            cursor_position = event.pos[0]

    if cursor_position < 200:
        if 0 < answer_1[1] ** 2 < 65:
            pygame.draw.circle(screen, (255, 255, 255), (175, 25), 3)
        if 0 < answer_1[3] ** 2 < 65:
            pygame.draw.circle(screen, (255, 255, 255), (355, 25), 3)
        if 0 < answer_1[2] ** 2 < 65:
            pygame.draw.circle(screen, (255, 255, 255), (175, 55), 3)
        if 0 < answer_1[4] ** 2 < 65:
            pygame.draw.circle(screen, (255, 255, 255), (355, 55), 3)
        if 65 < answer_1[1] ** 2:
            pygame.draw.circle(screen, (255, 255, 255), (175, 25), 5)
        if 65 < answer_1[3] ** 2:
            pygame.draw.circle(screen, (255, 255, 255), (355, 25), 5)
        if 65 < answer_1[2] ** 2:
            pygame.draw.circle(screen, (255, 255, 255), (175, 55), 5)
        if 65 < answer_1[4] ** 2:
            pygame.draw.circle(screen, (255, 255, 255), (355, 55), 5)
        split_text(screen, 60, 205, str(answer_1[0]), 15, 16, WHITE)

    elif cursor_position > 200:

        if 0 < answer_2[1] ** 2 < 65:
            pygame.draw.circle(screen, (255, 255, 255), (175, 25), 3)
        if 0 < answer_2[3] ** 2 < 65:
            pygame.draw.circle(screen, (255, 255, 255), (355, 25), 3)
        if 0 < answer_2[2] ** 2 < 65:
            pygame.draw.circle(screen, (255, 255, 255), (175, 55), 3)
        if 0 < answer_2[4] ** 2 < 65:
            pygame.draw.circle(screen, (255, 255, 255), (355, 55), 3)
        if 65 < answer_2[1] ** 2:
            pygame.draw.circle(screen, (255, 255, 255), (175, 25), 5)
        if 65 < answer_2[3] ** 2:
            pygame.draw.circle(screen, (255, 255, 255), (355, 25), 5)
        if 65 < answer_2[2] ** 2:
            pygame.draw.circle(screen, (255, 255, 255), (175, 55), 5)
        if 65 < answer_2[4] ** 2:
            pygame.draw.circle(screen, (255, 255, 255), (355, 55), 5)
        split_text(screen, 230, 205, str(answer_2[0]), 14, 16, WHITE)

    if ((1 <= k <= 99) and (1 <= c <= 99) and (1 <= r <= 99) and (1 <= m <= 99) and (t < 200)) or (number_death != 10):

        if ans == 0:
            k = k + answer_1[1]
            c = c + answer_1[2]
            r = r + answer_1[3]
            m = m + answer_1[4]
            ans = None
            t += 1

        elif ans == 1:
            k += answer_2[1]
            c += answer_2[2]
            r += answer_2[3]
            m += answer_2[4]
            ans = None
            t += 1

    elif t < 200:

        if (k > 99) and (c > 99) and (r > 99) and (m > 99):
            number_death = 8
        elif k < 1:
            number_death = 0
        elif c < 1:
            number_death = 1
        elif r < 1:
            number_death = 2
        elif m < 1:
            number_death = 3
        elif k > 99:
            number_death = 4
        elif c > 99:
            number_death = 5
        elif r > 99:
            number_death = 6
        elif m > 99:
            number_death = 7

        record = t + 1
        death_count += 1
        save_data(death_count, record)

    elif t == 200:
        number_death = 9
        record = t + 1
        death_count += 1
        save_data(death_count, record)

    pygame.display.update()

pygame.quit()
