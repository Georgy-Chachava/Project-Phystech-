import pygame
import math
import datetime

def save_data(counter, data):
    '''Запись данных о рекордах в файл.'''
    with open('data.txt', 'a') as f:
        print('Score #', counter, ': ', data, file = f)

def new_session():
    '''Объявляет о начале новой игровой сессии в файле data'''
    now = datetime.datetime.now()
    with open('data.txt', 'a') as f:
        print('Game started at', now.strftime("%d-%m-%Y %H:%M"), file = f)

def split_text(screen, x, y, text, width, font_size, color):

    '''Осуществляет переносы текста.'''

    if text is not None:

        font = pygame.font.Font('Fonts/futurabkbtrusbyme_book.otf', font_size)
        words = text.split()
        i = 0
        k = 0
        f = ''
        while k < len(words):

            wrd = str(words[k])
            if i + len(wrd) <= width:
                f = f + wrd + ' '
                i += len(wrd) + 1
                k += 1

            else:

                if len(wrd) > width:
                    text1 = font.render(f, True, color)
                    screen.blit(text1, (x, y))
                    f = wrd
                    k+=1
                    if k!=0:
                        y += font_size

                text1 = font.render(f, True, color)
                screen.blit(text1, (x, y))
                i = 0
                f = ''
                y += font_size

            if k == len(words):
                text1 = font.render(f, True, color)
                screen.blit(text1, (x, y))

def bound(x, x_min, x_max):

    '''Простейший ограничитель параметра.'''

    if x < x_min:
        return x_min
    if x > x_max:
        return x_max
    return x

def rotate_image(screen, image, x, y):
    '''
    Поворот изображения на малые углы относительно центра нижней стороны.
    x, y - координаты начального положения центра изображения.
    '''

    correction_angle = 90

    image_rect = image.get_rect(center = (x, y))

    mx, my = pygame.mouse.get_pos()
    dx, dy = mx - image_rect.centerx, my - image_rect.centery
    angle = math.degrees(math.atan2(-dy, dx)) - correction_angle

    if angle < 0: angle+=360
    if angle >180: angle = -(360-angle)
    angle = -angle/2

    angle = bound(angle, -7, 7)

    rot_image = pygame.transform.rotate(image, angle)
    h = image.get_size()[1]/2
    ctr = list(image_rect.center)
    ctr[0] = ctr[0] + h*math.tan(-angle/180*math.pi)
    rot_image_rect = rot_image.get_rect(center = ctr)

    screen.blit(rot_image, rot_image_rect.topleft)
