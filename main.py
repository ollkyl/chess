import pygame
from chess_graphics import board
from chess_logic import Common, Pawn, Knight, Bishop, Rook, Queen, King


pygame.init()


screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess by Ollkyl")
icon = pygame.image.load("images/chess_icon.png")
pygame.display.set_icon(icon)
screen.fill((143, 109, 88))
black = (255, 255, 255)
white = (50, 50, 50)
square = 80

white_pawn_image = pygame.image.load("images/pawn white.png")
black_pawn_image = pygame.image.load("images/pawn black.png")
white_knight_image = pygame.image.load("images/knight white.png")
black_knight_image = pygame.image.load("images/knight black.png")
white_bishop_image = pygame.image.load("images/bishop white.png")
black_bishop_image = pygame.image.load("images/bishop black.png")
white_rook_image = pygame.image.load("images/rook white.png")
black_rook_image = pygame.image.load("images/rook black.png")
white_queen_image = pygame.image.load("images/queen white.png")
black_queen_image = pygame.image.load("images/queen black.png")
white_king_image = pygame.image.load("images/king white.png")
black_king_image = pygame.image.load("images/king black.png")


pawn_1_pos_white = Pawn("pawn", "white", 0, 1, white_pawn_image)
pawn_2_pos_white = Pawn("pawn", "white", 1, 1, white_pawn_image)
pawn_3_pos_white = Pawn("pawn", "white", 2, 1, white_pawn_image)
pawn_4_pos_white = Pawn("pawn", "white", 3, 1, white_pawn_image)
pawn_5_pos_white = Pawn("pawn", "white", 4, 1, white_pawn_image)
pawn_6_pos_white = Pawn("pawn", "white", 5, 1, white_pawn_image)
pawn_7_pos_white = Pawn("pawn", "white", 6, 1, white_pawn_image)
pawn_8_pos_white = Pawn("pawn", "white", 7, 1, white_pawn_image)
knight_1_pos_white = Knight("knight", "white", 1, 0, white_knight_image)
knight_2_pos_white = Knight("knight", "white", 6, 0, white_knight_image)
bishop_1_pos_white = Bishop("bishop", "white", 2, 0, white_bishop_image)
bishop_2_pos_white = Bishop("bishop", "white", 5, 0, white_bishop_image)
rook_1_pos_white = Rook("rook", "white", 0, 0, white_rook_image)
rook_2_pos_white = Rook("rook", "white", 7, 0, white_rook_image)
queen_pos_white = Queen("queen", "white", 3, 0, white_queen_image)
king_pos_white = King("king", "white", 4, 0, white_king_image)

pawn_1_pos_black = Pawn("pawn", "black", 0, 6, black_pawn_image)
pawn_2_pos_black = Pawn("pawn", "black", 1, 6, black_pawn_image)
pawn_3_pos_black = Pawn("pawn", "black", 2, 6, black_pawn_image)
pawn_4_pos_black = Pawn("pawn", "black", 3, 6, black_pawn_image)
pawn_5_pos_black = Pawn("pawn", "black", 4, 6, black_pawn_image)
pawn_6_pos_black = Pawn("pawn", "black", 5, 6, black_pawn_image)
pawn_7_pos_black = Pawn("pawn", "black", 6, 6, black_pawn_image)
pawn_8_pos_black = Pawn("pawn", "black", 7, 6, black_pawn_image)
knight_1_pos_black = Knight("knight", "black", 1, 7, black_knight_image)
knight_2_pos_black = Knight("knight", "black", 6, 7, black_knight_image)
bishop_1_pos_black = Bishop("bishop", "black", 2, 7, black_bishop_image)
bishop_2_pos_black = Bishop("bishop", "black", 5, 7, black_bishop_image)
rook_1_pos_black = Rook("rook", "black", 0, 7, black_rook_image)
rook_2_pos_black = Rook("rook", "black", 7, 7, black_rook_image)
queen_pos_black = Queen("queen", "black", 3, 7, black_queen_image)
king_pos_black = King("king", "black", 4, 7, black_king_image)

chess_board = [[Common('____', '____', -1, -1, None) for _ in range(8)] for _ in range(8)]

#  список белых фигур
white_figures = [pawn_1_pos_white, pawn_2_pos_white, pawn_3_pos_white, pawn_4_pos_white,
                 pawn_5_pos_white, pawn_6_pos_white, pawn_7_pos_white, pawn_8_pos_white, knight_1_pos_white,
                 knight_2_pos_white, bishop_1_pos_white, bishop_2_pos_white, rook_1_pos_white, rook_2_pos_white,
                 queen_pos_white, king_pos_white]

#  список черных фигур
black_figures = [pawn_1_pos_black, pawn_2_pos_black, pawn_3_pos_black, pawn_4_pos_black,
                 pawn_5_pos_black, pawn_6_pos_black, pawn_7_pos_black, pawn_8_pos_black, knight_1_pos_black,
                 knight_2_pos_black, bishop_1_pos_black, bishop_2_pos_black, rook_1_pos_black, rook_2_pos_black,
                 queen_pos_black, king_pos_black]

for figure in white_figures:
    chess_board[figure.coordinate_x][figure.coordinate_y] = figure

for figure in black_figures:
    chess_board[figure.coordinate_x][figure.coordinate_y] = figure


class Game(Common):
    @staticmethod
    def start_game(new_coordinate_x, new_coordinate_y, coordinate_x, coordinate_y):
        now_piece = chess_board[coordinate_x][coordinate_y]
        if isinstance(now_piece, Pawn):
            if now_piece.move(new_coordinate_x, new_coordinate_y):
                chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                chess_board[coordinate_x][coordinate_y] = Common('____', '____', coordinate_x,
                                                                 coordinate_y, None)
        elif isinstance(now_piece, Knight):
            if now_piece.move(new_coordinate_x, new_coordinate_y):
                chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                chess_board[coordinate_x][coordinate_y] = Common('____', '____', coordinate_x,
                                                                 coordinate_y, None)
        elif isinstance(now_piece, Bishop):
            if now_piece.move(new_coordinate_x, new_coordinate_y):
                chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                chess_board[coordinate_x][coordinate_y] = Common('____', '____', coordinate_x,
                                                                 coordinate_y, None)
        elif isinstance(now_piece, Rook):
            if now_piece.move(new_coordinate_x, new_coordinate_y):
                chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                chess_board[coordinate_x][coordinate_y] = Common('____', '____', coordinate_x,
                                                                 coordinate_y, None)
        elif isinstance(now_piece, Queen):
            if now_piece.move(new_coordinate_x, new_coordinate_y):
                chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                chess_board[coordinate_x][coordinate_y] = Common('____', '____', coordinate_x,
                                                                 coordinate_y, None)
        elif isinstance(now_piece, King):
            if now_piece.move(new_coordinate_x, new_coordinate_y):
                chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                chess_board[coordinate_x][coordinate_y] = Common('____', '____', coordinate_x,
                                                                 coordinate_y, None)
        else:
            print("Not find")


end_of_game = 0

while end_of_game != 1:
    #  ввод координат
    now_coordinate_x, now_coordinate_y = map(int, input().split())
    next_coordinate_x, next_coordinate_y = map(int, input().split())
    current_piece = Game(next_coordinate_x, next_coordinate_y, now_coordinate_x, now_coordinate_y, None)
    current_piece.start_game(next_coordinate_x, next_coordinate_y, now_coordinate_x, now_coordinate_y)
    end_of_game = current_piece.mat


def board():
    for i in range(8):
        for j in range(8):
            if chess_board[i][j] != white_figures:
                if ((i + j) % 2) == 0:
                    pygame.draw.rect(screen, black, (i * square, j * square, square, square))
                else:
                    pygame.draw.rect(screen, white, (i * square, j * square, square, square))
            else:
                if isinstance(white_figures, Pawn):
                    screen.blit(white_pawn_image, (i * square, j * square))
                elif isinstance(figure, Rook):
                    screen.blit(white_rook_image, (i * square, j * square))
    return True


running = True

while running:
    board()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            event.quit()
            running = False
