import pygame

def split_text(screen, x, y, text, width, font_size, color):

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
            text1 = font.render(f, True, color)
            screen.blit(text1, (x, y))
            i = 0
            f = ''
            y += font_size

        if k == len(words):
            text1 = font.render(f, True, color)
            screen.blit(text1, (x, y))
            
