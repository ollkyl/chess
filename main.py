from source import chess_menu, chess_logic, settings, constants
import pygame

def main_func():
    color_of_board = (109, 70, 166)
    value_music = 0

    def play_music(value_music):
        pygame.mixer.music.load(constants.MUSIC_CHESS)
        
        if value_music == 1:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.pause()

    status = chess_menu.menu()
    while status != 3:
        play_music(value_music)
        if status == 1:
            try:
                chess_logic.start_logic(color_of_board)
            except TypeError:
                print("invalid color argument")
                chess_logic.start_logic((109, 70, 166))
        elif status == 2:
            color_of_board, value_music = settings.start_settings(value_music)
        status = chess_menu.menu()
__name__ == "__main__"   
main_func()  