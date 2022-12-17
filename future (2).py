import pygame
import random as rnd
from CharacterS import *
from Images import *
from REPLICS import *
import pygame.font
from pygame.draw import *
from visual import *


def click(event, active_character):
    if event.pos[0] < 200:
        ans = 0
    elif event.pos[0] > 200:
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


Kiselev = Character(screen, kiselev_image, kiselevs_replics)
Getc = Character(screen, getc_image, getc_replics)
Ivanov = Character(screen, ivanov_image, ivanov_replics)
PE_teacher = Character(screen, pe_teacher_image, pe_teacher_replics)
BGD_teacher = Character(screen, bgd_teacher_image, bgd_teacher_replics)
Groupmate = Character(screen, groupmate_image, groupmate_replics)
Dekanat = Character(screen, dekanat_image, dekanat_replics)
Senator = Character(screen, senator_image, senator_replics)
English_teacher = Character(screen, english_teacher_image, english_teacher_replics)
Best_friend = Character(screen, best_friend_image, best_friend_replics)
Roommate = Character(screen, roommate_image, roommate_replics)
Gavrikov = Character(screen, gavrikov_image, gavrikov_replics)
Showerman = Character(screen, showerman_image, showerman_replics)
Cat = Character(screen, cat_image, cat_replics)
Khiryanov = Character(screen, khirianov_image, khirianov_replics)
Paukov = Character(screen, paukov_image, paukov_replics)
Agent_FPMI = Character(screen, agent_FPMI_image, agent_FPMI_replics)

NPC = [Kiselev, Roommate, Ivanov, PE_teacher, BGD_teacher, Groupmate, Dekanat, Senator, English_teacher,
       Best_friend, Roommate, Gavrikov, Showerman, Cat, Khiryanov, Paukov, Agent_FPMI]
finished = False
ans = None
active_character = None
k = 50
c = 50
r = 50
m = 50
t = 0
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

    if active_character == None:
        index = rnd.randint(0, len(NPC) - 1)
        active_character = NPC[index]
        d = active_character.replics
        i = rnd.randint(0, len(d) - 1)

    active_character.output()
    lst = list(d.keys())

    #print(lst[i])
    answers = d[str(lst[i])]
    answer_1 = answers[0]
    answer_2 = answers[1]

   # print(answer_1[0])
    #print(answer_2[0])

    #ans = rnd.randint(0, 1)

   # teK = text.render('1.', True, (255, 255, 255))
   # screen.blit(teK, (60, 200))
    #teK = text_2.render(str(answer_1[0]), True, (255, 255, 255))
    #screen.blit(teK, (60, 205))

    split_text(screen, 60, 205, str(answer_1[0]), 15, 16, (255, 255, 255))

   # teK = text.render('2.', True, (255, 255, 255))
   # screen.blit(teK, (20, 610))

    #teK = text_2.render(str(answer_2[0]), True, (255, 255, 255))
    #screen.blit(teK, (230, 205))

    split_text(screen, 230, 205, str(answer_2[0]), 14, 16, (255, 255, 255))   

    teK = text.render('Недель на Физтехе', True, (255, 255, 255))
    screen.blit(teK, (20, 620))
    teK = text.render(str(t+1), True, (255, 255, 255))
    screen.blit(teK, (175, 620))

    #teK = text.render(str(lst[i]), True, (255, 255, 255))
    #screen.blit(teK, (20, 150))

    split_text(screen, 20, 110, str(lst[i]), 39, 18, (255, 255, 255))

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

    if k<1 or k>99 or c<1 or c>99 or r<1 or r>99 or m<1 or m>99:
        print(t)
        print( k, c, r, m)
        finished = True

    pygame.display.update()
pygame.quit()
