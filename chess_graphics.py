import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
screen.fill((143, 109, 88))
black = (255, 255, 255)
white = (50, 50, 50)
square = 80


def board():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, black, (i * square, j * square, square, square))
            else:
                pygame.draw.rect(screen, white, (i * square, j * square, square, square))
    return True


running = True

while running:
    board()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            event.quit()
            running = False

# fkgrp,g