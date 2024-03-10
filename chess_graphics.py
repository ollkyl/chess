import pygame

pygame.init()
#menu

screen = pygame.display.set_mode((800, 800))
icon = pygame.image.load('images/chess_icon.png')
button = pygame.Surface((300, 50))
font_1 = pygame.font.Font('fonts/mokoto.ttf', 26)
text_button_1 = font_1.render("START GAME", True, (75, 0, 130) )
text_button_2 = font_1.render("SETTINGS", True, (75, 0, 130))
text_button_3 = font_1.render("EXIT", True, (75, 0, 130))

button_1_rect = pygame.Rect(300, 250, 300, 50)
button_2_rect = pygame.Rect(300, 350, 300, 50)
button_3_rect = pygame.Rect(300, 450, 300, 50)
pygame.display.set_caption("Chess by Ollkyl")
pygame.display.set_icon(icon)
button.fill((123, 104, 238))
screen.fill((10, 32, 73))
running = True
clock = pygame.time.Clock()

def menu():
    while running:
        clock.tick(10)
        screen.blit(button, (250, 250))
        screen.blit(button, (250, 350))
        screen.blit(button, (250, 450))
        screen.blit(text_button_1, (285,263))
        screen.blit(text_button_2, (320,363))
        screen.blit(text_button_3, (365,463))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:        
                if event.button == (1):
                    if button_1_rect.collidepoint(pygame.mouse.get_pos()):
                        import chess_logic
                        chess_logic.start_match()
                if event.button == (1):
                    if button_2_rect.collidepoint(pygame.mouse.get_pos()):
                        import Settings
                        Settings.settings()
                if event.button == (1):
                    if button_3_rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        running = False
    return True
