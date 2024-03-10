import pygame

pygame.init()
#menu


def board_color(color):    
    for i in range(8):
        for j in range(8):
            if color == wood:
                screen.blit(wood, (390, 175))
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, white, (390 + (i * square), 175 + (j * square), square, square))
            else:
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, white, (390 + (i * square), 175 + (j * square), square, square))
                else:
                    pygame.draw.rect(screen, color, (390 + (i * square), 175 + (j * square), square, square))
    pygame.display.update()
    return True               


screen = pygame.display.set_mode((800, 800))
icon = pygame.image.load('images/chess_icon.png')
button_1 = pygame.Surface((160,  40))
button_2 = pygame.Surface((16,  16))
font_1 = pygame.font.Font('fonts/mokoto.ttf', 22)
font_2 = pygame.font.Font('fonts/mokoto2.ttf', 16)
square = 35
white = (250, 250, 250)
black = (10, 10, 10)
green = (46, 139, 87)
purple = (109, 70, 166)
wood = pygame.image.load('images/wood_settings.jpg')

text_button_music = font_2.render("MUSIC", False, (255, 160, 122))
text_button_sound = font_2.render("SOUND", False, (255, 160, 122))
text_button_back = font_1.render("BACK", False, (26, 11, 75))
text_button_apply = font_1.render("APPLY", False, (26, 11, 75))

text_button_color = font_2.render("COLOR", False, (255, 160, 122))
text_button_purple = font_2.render("purple", False, (255, 160, 122))
text_button_green = font_2.render("green", False, (255, 160, 122))
text_button_black = font_2.render("black", False, (255, 160, 122))
text_button_wood = font_2.render("wood", False, (255, 160, 122))

text_button_type = font_2.render("TYPE", False, (255, 160, 122))
text_button_type1 = font_2.render("first type", False, (255, 160, 122))
text_button_type2 = font_2.render("second type", False, (255, 160, 122))


button_1_rect = pygame.Rect(145, 590, 160, 40)
button_2_rect = pygame.Rect(445, 590, 160, 40)
button_3_rect = pygame.Rect(280, 80, 16, 16)
button_4_rect = pygame.Rect(280, 120, 16, 16)
button_5_rect = pygame.Rect(280, 205, 16, 16)
button_6_rect = pygame.Rect(280, 245, 16, 16)
button_7_rect = pygame.Rect(280, 285, 16, 16)
button_8_rect = pygame.Rect(280, 450, 16, 16)
button_9_rect = pygame.Rect(280, 325, 16, 16)
button_10_rect = pygame.Rect(280, 405, 16, 16)
button_8_rect = pygame.Rect(280, 445, 16, 16)

pygame.display.set_caption("Chess by Ollkyl")
pygame.display.set_icon(icon)
button_1.fill((147, 112, 219))
button_2.fill((147, 112, 219))
running = True
clock = pygame.time.Clock()

def settings():
    running = True
    screen.fill((10, 32, 73))
    while running:
        clock.tick(10)
    
        board_color(green)
        screen.blit(button_1, (145, 590, 160, 40))
        screen.blit(button_1, (445, 590, 160, 40))
        screen.blit(button_2, (280, 80, 16, 16))
        screen.blit(button_2, (280, 120, 16, 16))
        screen.blit(button_2, (280, 205, 16, 16))
        screen.blit(button_2, (280, 245, 16, 16))
        screen.blit(button_2, (280, 285, 16, 16))
        screen.blit(button_2, (280, 325, 16, 16))
        screen.blit(button_2, (280, 405, 16, 16))
        screen.blit(button_2, (280, 445, 16, 16))

        screen.blit(text_button_music, (90, 80))
        screen.blit(text_button_sound, (90, 120))

        screen.blit(text_button_color, (40, 165))
        screen.blit(text_button_purple, (90,205))
        screen.blit(text_button_green, (90,245))
        screen.blit(text_button_black, (90,285))
        screen.blit(text_button_wood, (90,325))
        
        screen.blit(text_button_type, (40, 365))
        screen.blit(text_button_type1, (90,405))
        screen.blit(text_button_type2, (90,445))

        screen.blit(text_button_apply, (477, 600))
        screen.blit(text_button_back, (182, 600))
    

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:        
                if event.button == (1):  #back
                    if button_1_rect.collidepoint(pygame.mouse.get_pos()):
                        import chess_graphics
                        chess_graphics.menu()
                    elif button_2_rect.collidepoint(pygame.mouse.get_pos()):
                        import chess_graphics
                        chess_graphics.menu()   
                    elif button_3_rect.collidepoint(pygame.mouse.get_pos()):
                        print("music")
                    elif button_4_rect.collidepoint(pygame.mouse.get_pos()):
                        print("sound")
                    elif button_5_rect.collidepoint(pygame.mouse.get_pos()):
                        board_color(purple)  
                        print("purple")
                    elif button_6_rect.collidepoint(pygame.mouse.get_pos()):
                        board_color(green)
                    elif button_7_rect.collidepoint(pygame.mouse.get_pos()):
                        board_color(black)  
                        print("black")
                    elif button_8_rect.collidepoint(pygame.mouse.get_pos()):
                        board_color(wood) 
                        print("wood")         
                    elif button_9_rect.collidepoint(pygame.mouse.get_pos()):
                        print("first type")        
                    elif button_10_rect.collidepoint(pygame.mouse.get_pos()):
                        print("second type")  
                        
                              
settings()

