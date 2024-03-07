import pygame


pygame.init()


class Chess_piece:
    def __init__(self, piece, color, coordinate_x, coordinate_y, image):
        self.piece = piece
        self.color = color
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.image = image 
        self.new_coordinate_x = None
        self.new_coordinate_y = None
        self.mat = 0
     
    def cheking_position(self, new_coordinate_x, new_coordinate_y):  # проверка выхода за границы доски
        if not (0 <= new_coordinate_y <= 7) and not (0 <= new_coordinate_x <= 7):
            print("False  cheking_position (0 <=  <= 7)")
            return False
        elif chess_board[new_coordinate_x][new_coordinate_y].color == self.color:
            print("False  cheking_position color")
            return False
        elif chess_board[new_coordinate_x][new_coordinate_y].piece == "king":
            print("MAT")
            current_piece.mat = 1
            return True
        else:
            return True

    @staticmethod
    #  препятствия на пути
    def way(coordinate_x, coordinate_y, new_coordinate_x, new_coordinate_y, direction_x, direction_y):
        way_x = coordinate_x
        way_y = coordinate_y
        while (way_x != new_coordinate_x) or (way_y != new_coordinate_y):
            if chess_board[way_x + direction_x][way_y + direction_y].piece == "_":
                way_x += direction_x
                way_y += direction_y
            else:
                print("False  def way")
                return False
        return True


class Pawn(Chess_piece):  # пешка
    def move(self, new_coordinate_x, new_coordinate_y):
        print("Inside Pawn move method")
        self.new_coordinate_x = new_coordinate_x
        self.new_coordinate_y = new_coordinate_y
        if self.color == "white":
            direction = 1
            start_side = 1
        elif self.color == "black":
            direction = -1
            start_side = 6
        else:
            return False
        if not (0 <= new_coordinate_y <= 7):
            return False
        if new_coordinate_y == start_side + 2 * direction:
            self.coordinate_x = new_coordinate_x
            self.coordinate_y = new_coordinate_y
            return True
        # проверка на направление и пустую клетку
        elif (new_coordinate_y - self.coordinate_y == direction) and (chess_board[new_coordinate_x][new_coordinate_y].piece == "_"):
            self.coordinate_x = new_coordinate_x
            self.coordinate_y = new_coordinate_y
            return True
        # поедание фигуры на искосок
        elif self.cheking_position(new_coordinate_x, new_coordinate_y) and (abs(new_coordinate_x - self.coordinate_x) == 1):
            self.coordinate_x = new_coordinate_x
            self.coordinate_y = new_coordinate_y
            return True
        else:
            return False


class Knight(Chess_piece):  # конь
    def move(self, new_coordinate_x, new_coordinate_y):
        print("Inside Knight move method")
        self.new_coordinate_x = new_coordinate_x
        self.new_coordinate_y = new_coordinate_y
        if self.cheking_position(new_coordinate_x, new_coordinate_y):
            # проверка движения буквой Г
            if (abs(new_coordinate_y - self.coordinate_y) == 2) and (abs(new_coordinate_x - self.coordinate_x) == 1):
                self.coordinate_x = new_coordinate_x
                self.coordinate_y = new_coordinate_y
                return True
            elif (abs(new_coordinate_x - self.coordinate_x) == 2) and (abs(new_coordinate_y - self.coordinate_y) == 1):
                self.coordinate_x = new_coordinate_x
                self.coordinate_y = new_coordinate_y
                return True
            else:
                return False


class Bishop(Chess_piece):  # слон
    def move(self, new_coordinate_x, new_coordinate_y):
        print("Inside Bishop move method")
        self.new_coordinate_x = new_coordinate_x
        self.new_coordinate_y = new_coordinate_y
        direction_x = int((new_coordinate_x - self.coordinate_x) / abs(new_coordinate_x - self.coordinate_x))
        direction_y = int((new_coordinate_y - self.coordinate_y) / abs(new_coordinate_x - self.coordinate_x))
        if self.cheking_position(new_coordinate_x, new_coordinate_y):
            # проверка движения по диагонали
            if abs(new_coordinate_x - self.coordinate_x) == abs(new_coordinate_y - self.coordinate_y):
                if self.way(self.coordinate_x, self.coordinate_y, new_coordinate_x, new_coordinate_y, direction_x, direction_y):
                    self.coordinate_x = new_coordinate_x
                    self.coordinate_y = new_coordinate_y
                    return True
            return False
        else:
            return False


class Rook(Chess_piece):  # ладья
    def move(self, new_coordinate_x, new_coordinate_y):
        print("Inside Rook move method")
        self.new_coordinate_x = new_coordinate_x
        self.new_coordinate_y = new_coordinate_y
        direction_x = new_coordinate_x - self.coordinate_x
        direction_y = new_coordinate_y - self.coordinate_y
        if direction_x == 0:
            direction_y = int(direction_y / abs(direction_y))
        else:
            direction_x = int(direction_x / abs(direction_x))
        if self.cheking_position(new_coordinate_x, new_coordinate_y):
            # проверка на движение только по вертикали
            if (new_coordinate_x - self.coordinate_x == 0) and (new_coordinate_y - self.coordinate_y != 0):
                if self.way(self.coordinate_x, self.coordinate_y, new_coordinate_x, new_coordinate_y, direction_x, direction_y):
                    self.coordinate_x = new_coordinate_x
                    self.coordinate_y = new_coordinate_y
                    return True
                else:
                    return False
            # проверка на движение только по горизонтали
            elif (new_coordinate_x - self.coordinate_x != 0) and (new_coordinate_y - self.coordinate_y == 0):
                if self.way(self.coordinate_x, self.coordinate_y, new_coordinate_x, new_coordinate_y, direction_x,  direction_y):
                    self.coordinate_x = new_coordinate_x
                    self.coordinate_y = new_coordinate_y
                    return True
                else:
                    print("False 1")
                    return False
            else:
                print("False 2")
                return False
        else:
            print("False 3")
            return False


class Queen(Chess_piece):
    def move(self, new_coordinate_x, new_coordinate_y):
        print("Inside Queen move method")
        self.new_coordinate_x = new_coordinate_x
        self.new_coordinate_y = new_coordinate_y
        way_x = self.coordinate_x
        way_y = self.coordinate_y
        direction_x = new_coordinate_x - self.coordinate_x
        direction_y = new_coordinate_y - self.coordinate_y
        if self.cheking_position(new_coordinate_x, new_coordinate_y):
            # проверка движения по диагонали
            if abs(new_coordinate_x - self.coordinate_x) == abs(new_coordinate_y - self.coordinate_y):
                if self.way(way_x, way_y, new_coordinate_x, new_coordinate_y, direction_x, direction_y):
                    self.coordinate_x = new_coordinate_x
                    self.coordinate_y = new_coordinate_y
                return True
            # проверка на движение только по вертикали
            elif (new_coordinate_x - self.coordinate_x == 0) and (new_coordinate_y - self.coordinate_y != 0):
                if self.way(way_x, way_y, new_coordinate_x, new_coordinate_y, direction_x, direction_y):
                    self.coordinate_x = new_coordinate_x
                    self.coordinate_y = new_coordinate_y
                return True
            # проверка на движение только по горизонтали
            elif (new_coordinate_x - self.coordinate_x != 0) and (new_coordinate_y - self.coordinate_y == 0):
                if self.way(way_x, way_y, new_coordinate_x, new_coordinate_y, direction_x, direction_y):
                    self.coordinate_x = new_coordinate_x
                    self.coordinate_y = new_coordinate_y
                    return True
            else:
                return False
        else:
            return False


class King(Chess_piece):
    def move(self, new_coordinate_x, new_coordinate_y):
        print("Inside King move method")
        self.new_coordinate_x = new_coordinate_x
        self.new_coordinate_y = new_coordinate_y
        if self.cheking_position(new_coordinate_x, new_coordinate_y):
            if (abs(new_coordinate_x - self.coordinate_x) <= 1) and (abs(new_coordinate_y - self.coordinate_y) <= 1):
                self.coordinate_x = new_coordinate_x
                self.coordinate_y = new_coordinate_y
                return True
            else:
                return False
        else:
            return False
        

chess_board = [[Chess_piece('_', '_', -1, -1, None) for _ in range(8)] for _ in range(8)]


def board():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, white, (i * square, j * square, square, square))
            else:
                pygame.draw.rect(screen, black, (i * square, j * square, square, square))
    for figure in white_figures:               
        if isinstance(figure, Pawn):
            screen.blit(figure.image, (figure.coordinate_x * square + 16, figure.coordinate_y * square + 16))
        elif isinstance(figure, Rook):
                screen.blit(figure.image, (figure.coordinate_x * square + 16, figure.coordinate_y * square + 16))
        elif isinstance(figure, Knight):
                screen.blit(figure.image, (figure.coordinate_x * square + 16, figure.coordinate_y * square + 16))
        elif isinstance(figure, Bishop):
                screen.blit(figure.image, (figure.coordinate_x * square + 16, figure.coordinate_y * square + 16))
        elif isinstance(figure, Queen):
                screen.blit(figure.image, (figure.coordinate_x * square + 16, figure.coordinate_y * square + 16))
        elif isinstance(figure, King):
                screen.blit(figure.image, (figure.coordinate_x * square + 16, figure.coordinate_y * square + 16))
    for figure in black_figures:     
        if isinstance(figure, Pawn):
            screen.blit(figure.image, (figure.coordinate_x * square + 16, figure.coordinate_y * square + 16))
        elif isinstance(figure, Rook):
                screen.blit(figure.image, (figure.coordinate_x * square + 16, figure.coordinate_y * square + 16))
        elif isinstance(figure, Knight):
                screen.blit(figure.image, (figure.coordinate_x * square + 16, figure.coordinate_y * square + 16))
        elif isinstance(figure, Bishop):
                screen.blit(figure.image, (figure.coordinate_x * square + 16, figure.coordinate_y * square + 16))
        elif isinstance(figure, Queen):
                screen.blit(figure.image, (figure.coordinate_x * square + 16, figure.coordinate_y * square + 16))
        elif isinstance(figure, King):
                screen.blit(figure.image, (figure.coordinate_x * square + 16, figure.coordinate_y * square + 16))  

    pygame.display.update()    


def get_cell(x, y):
    row = x / 100
    col = y / 100
    return row, col


end_of_game = 0


screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess by Ollkyl")
icon = pygame.image.load("images/chess_icon.png")
pygame.display.set_icon(icon)
screen.fill((143, 109, 88))
white = (255, 255, 255)
black = (109, 70, 166)
square = 100

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
current_piece = (None, None, None, None, None)


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



class Game(Chess_piece):
    @staticmethod
    def start_game(new_coordinate_x, new_coordinate_y, coordinate_x, coordinate_y):
        now_piece = chess_board[coordinate_x][coordinate_y]
        if isinstance(now_piece, Pawn):
            if now_piece.move(new_coordinate_x, new_coordinate_y):
                chess_board[new_coordinate_x][new_coordinate_y].image = pygame.Surface((0, 0))
                chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                chess_board[coordinate_x][coordinate_y] = Chess_piece('_', '_', coordinate_x, coordinate_y, None)
        elif isinstance(now_piece, Knight):
            if now_piece.move(new_coordinate_x, new_coordinate_y):
                chess_board[new_coordinate_x][new_coordinate_y].image = pygame.Surface((0, 0))
                chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                chess_board[coordinate_x][coordinate_y] = Chess_piece('_', '_', coordinate_x, coordinate_y, None)
        elif isinstance(now_piece, Bishop):
            if now_piece.move(new_coordinate_x, new_coordinate_y):
                chess_board[new_coordinate_x][new_coordinate_y].image = pygame.Surface((0, 0))
                chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                chess_board[coordinate_x][coordinate_y] = Chess_piece('_', '_', coordinate_x, coordinate_y, None)
        elif isinstance(now_piece, Rook):
            if now_piece.move(new_coordinate_x, new_coordinate_y):
                chess_board[new_coordinate_x][new_coordinate_y].image = pygame.Surface((0, 0))
                chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                chess_board[coordinate_x][coordinate_y] = Chess_piece('_', '_', coordinate_x, coordinate_y, None)
        elif isinstance(now_piece, Queen):
            if now_piece.move(new_coordinate_x, new_coordinate_y):
                chess_board[new_coordinate_x][new_coordinate_y].image = pygame.Surface((0, 0))
                chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                chess_board[coordinate_x][coordinate_y] = Chess_piece('_', '_', coordinate_x,  coordinate_y, None)
        elif isinstance(now_piece, King):
            if now_piece.move(new_coordinate_x, new_coordinate_y):
                chess_board[new_coordinate_x][new_coordinate_y].image = pygame.Surface((0, 0))
                chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                chess_board[coordinate_x][coordinate_y] = Chess_piece('_', '_', coordinate_x,  coordinate_y, None)
        else:
            print("Not find")


running = True
board()
pygame.display.update()
click_counter = 0

while running:
    board()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and click_counter == 0:
            if event.button == (1):
                click_counter = 1
                now_row, now_col = get_cell(*pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONDOWN and click_counter == 1:        
            if event.button == (1):
                new_row, new_col = get_cell(*pygame.mouse.get_pos())
                Game.start_game(int(new_row), int(new_col), int(now_row), int(now_col))
                click_counter = 0
                # end_of_game = now_piece.mat
        

print("Game Over")       