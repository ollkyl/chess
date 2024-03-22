from firstlev import chess_menu
from settings import Settings
from firstlev import chess_logic

def main_func():
    color_of_board = (109, 70, 166)
    value_music = 1
    status = 5
    while status != 3:
        if __name__ == "__main__":   
            status = chess_menu.menu()
            if status == 1:
                chess_logic.start_logic(color_of_board, value_music)
            elif status == 2:
                color_of_board, value_music = Settings.start_settings()
                chess_menu.menu()

main_func()