import pygame


pygame.init()
#menu

screen = pygame.display.set_mode((800, 800))
icon = pygame.image.load('images/chess_icon.png')
button = pygame.Surface((210, 50))
font_1 = pygame.font.Font('fonts/Honk.ttf', 36)
text_button_1 = font_1.render("START GAME", True, 'Black' )
text_button_2 = font_1.render("SETTINGS", True, 'Black')
text_button_3 = font_1.render("EXIT", True, 'Black')
text_texture_1 = pygame.image.load('fonts/texture1.png')
text_texture_2 = pygame.image.load('fonts/texture2.png')
text_texture_3 = pygame.image.load('fonts/texture3.png')
button_1_rect = pygame.Rect(300, 250, 210, 50)
button_2_rect = pygame.Rect(300, 350, 210, 50)
button_3_rect = pygame.Rect(300, 450, 210, 50)
pygame.display.set_caption("Chess by Ollkyl")
pygame.display.set_icon(icon)
button.fill((0,0,0))
screen.fill((34, 85, 178))
running = True
clock = pygame.time.Clock()


while running:
    clock.tick(10)
    screen.blit(button, (300, 250))
    screen.blit(button, (300, 350))
    screen.blit(button, (300, 450))
    screen.blit(text_texture_1, (312, 266))
    screen.blit(text_texture_2, (336, 366))
    screen.blit(text_texture_3, (373, 466))
    screen.blit(text_button_1, (312,253))
    screen.blit(text_button_2, (336,353))
    screen.blit(text_button_3, (373,453))
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
                    print("start game")
            if event.button == (1):
                if button_2_rect.collidepoint(pygame.mouse.get_pos()):
                    print("settings")
            if event.button == (1):
                if button_3_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    running = False
