# chess_logic.py



def start_logic(color_of_board, value_music):
    import time
    import pygame
    pygame.mixer.init()
    pygame.init()
    font_1 = pygame.font.Font('fonts/mokoto.ttf', 60)


    
    class Chess_piece:
        def __init__(self, piece, color, coordinate_x, coordinate_y, image, mat):
            self.piece = piece
            self.color = color
            self.coordinate_x = coordinate_x
            self.coordinate_y = coordinate_y
            self.image = image 
            self.new_coordinate_x = None
            self.new_coordinate_y = None
            self.mat = 0
        
        def cheking_position(self, new_coordinate_x, new_coordinate_y):  # checking for board boundaries
            if not (0 <= new_coordinate_y <= 7) and not (0 <= new_coordinate_x <= 7):
                print("False  cheking_position (0 <=  <= 7)")
                return False
            elif chess_board[new_coordinate_x][new_coordinate_y].color == self.color:
                print("False  cheking_position color")
                return False
            elif chess_board[new_coordinate_x][new_coordinate_y].piece == "king":
                print("MAT")
                current_piece.mat = 1
                end_game()
                return True
            else:
                return True

        @staticmethod
        #  obstacles on the way
        def way(coordinate_x, coordinate_y, new_coordinate_x, new_coordinate_y, direction_x, direction_y):
            way_x = coordinate_x + direction_x
            way_y = coordinate_y + direction_y
            if direction_x == 0 or direction_y == 0:
                while way_x != new_coordinate_x or way_y != new_coordinate_y:
                    if chess_board[way_x][way_y].piece == "_":
                        way_x += direction_x
                        way_y += direction_y
                    else:
                        print("False  def way horizontal vertical movement")
                        return False
                return True
            else:
                while (way_x != new_coordinate_x) or (way_y != new_coordinate_y):
                    if chess_board[way_x][way_y].piece == "_":
                        way_x += direction_x
                        way_y += direction_y
                    else:
                        print("False  def way diagonal movement")
                        return False
                return True

    class Pawn(Chess_piece):
        def move(self, new_coordinate_x, new_coordinate_y):
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
            if (new_coordinate_y == start_side + 2 * direction) and (new_coordinate_x - self.coordinate_x == 0):
                self.coordinate_x = new_coordinate_x
                self.coordinate_y = new_coordinate_y
                return True
            # direction and empty cell checking
            elif (new_coordinate_y - self.coordinate_y == direction) and (new_coordinate_x - self.coordinate_x == 0):
                if (chess_board[new_coordinate_x][new_coordinate_y].piece == "_"):
                    self.coordinate_x = new_coordinate_x
                    self.coordinate_y = new_coordinate_y
                    return True
                else:
                    False
            # diagonal capture
            elif (abs(new_coordinate_x - self.coordinate_x) == 1) and (abs(new_coordinate_y - self.coordinate_y) == 1):
                target_piece = chess_board[new_coordinate_x][new_coordinate_y]
                if target_piece.piece != "_" and target_piece.color != self.color:
                    self.coordinate_x = new_coordinate_x
                    self.coordinate_y = new_coordinate_y
                    return True
                else:
                    return False
            else:
                return False


    class Knight(Chess_piece):
        def move(self, new_coordinate_x, new_coordinate_y):
            self.new_coordinate_x = new_coordinate_x
            self.new_coordinate_y = new_coordinate_y
            if self.cheking_position(new_coordinate_x, new_coordinate_y):
                # L-shape movement check
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
            else:
                return False
            

    class Bishop(Chess_piece): 
        def move(self, new_coordinate_x, new_coordinate_y):
            self.new_coordinate_x = new_coordinate_x
            self.new_coordinate_y = new_coordinate_y
            if self.cheking_position(new_coordinate_x, new_coordinate_y):
                # diagonal movement check
                if abs(new_coordinate_x - self.coordinate_x) == abs(new_coordinate_y - self.coordinate_y):
                    direction_x = int((new_coordinate_x - self.coordinate_x) / abs(new_coordinate_x - self.coordinate_x))
                    direction_y = int((new_coordinate_y - self.coordinate_y) / abs(new_coordinate_x - self.coordinate_x))
                    if self.way(self.coordinate_x, self.coordinate_y, new_coordinate_x, new_coordinate_y, direction_x, direction_y):
                        self.coordinate_x = new_coordinate_x
                        self.coordinate_y = new_coordinate_y
                        return True
                else:
                    return False
            else:
                return False


    class Rook(Chess_piece):
        def move(self, new_coordinate_x, new_coordinate_y):
            self.new_coordinate_x = new_coordinate_x
            self.new_coordinate_y = new_coordinate_y
            direction_x = new_coordinate_x - self.coordinate_x
            direction_y = new_coordinate_y - self.coordinate_y
            if direction_x == 0:
                direction_y = int(direction_y / abs(direction_y))
            else:
                direction_x = int(direction_x / abs(direction_x))
            if self.cheking_position(new_coordinate_x, new_coordinate_y):
                # vertical only movement check
                if (new_coordinate_x - self.coordinate_x == 0) and (new_coordinate_y - self.coordinate_y != 0):
                    if self.way(self.coordinate_x, self.coordinate_y, new_coordinate_x, new_coordinate_y, direction_x, direction_y):
                        self.coordinate_x = new_coordinate_x
                        self.coordinate_y = new_coordinate_y
                        return True
                    else:
                        return False
                # пhorizontal only movement check
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
            self.new_coordinate_x = new_coordinate_x
            self.new_coordinate_y = new_coordinate_y
            direction_x = new_coordinate_x - self.coordinate_x
            direction_y = new_coordinate_y - self.coordinate_y
            if self.cheking_position(new_coordinate_x, new_coordinate_y):
                    # diagonal movement check
                if abs(new_coordinate_x - self.coordinate_x) == abs(new_coordinate_y - self.coordinate_y):
                    direction_x = int((new_coordinate_x - self.coordinate_x) / abs(new_coordinate_x - self.coordinate_x))
                    direction_y = int((new_coordinate_y - self.coordinate_y) / abs(new_coordinate_x - self.coordinate_x))
                    if self.way(self.coordinate_x, self.coordinate_y, new_coordinate_x, new_coordinate_y, direction_x, direction_y):
                        self.coordinate_x = new_coordinate_x
                        self.coordinate_y = new_coordinate_y
                        return True
                # vertical only movement check
                elif (new_coordinate_x - self.coordinate_x == 0) and (new_coordinate_y - self.coordinate_y != 0):
                    direction_y = int(direction_y / abs(direction_y))
                    if self.way(self.coordinate_x, self.coordinate_y, new_coordinate_x, new_coordinate_y, direction_x, direction_y):
                        self.coordinate_x = new_coordinate_x
                        self.coordinate_y = new_coordinate_y
                        return True
                # horizontal only movement check
                elif (new_coordinate_x - self.coordinate_x != 0) and (new_coordinate_y - self.coordinate_y == 0):
                    direction_x = int(direction_x / abs(direction_x))
                    if self.way(self.coordinate_x, self.coordinate_y, new_coordinate_x, new_coordinate_y, direction_x, direction_y):
                        self.coordinate_x = new_coordinate_x
                        self.coordinate_y = new_coordinate_y
                        return True
                else:
                    return False
            else:
                return False


    class King(Chess_piece):
        def move(self, new_coordinate_x, new_coordinate_y):
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
            
    
    def music(value_music):
            if value_music == 1:
                pygame.mixer.music.load('chess_music.mp3')
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.pause()

        
    chess_board = [[Chess_piece('_', '_', -1, -1, None, 0) for _ in range(8)] for _ in range(8)]
    wood = pygame.image.load('images/wood.jpg')

    def board(color_of_board):
        if color_of_board == 11:
            screen.blit(wood, (0, 0))
            for i in range(8):
                for j in range(8):
                    if (i + j) % 2 == 0:
                        pygame.draw.rect(screen, white, (i * square,j * square, square, square))
        else:
            for i in range(8):
                for j in range(8):
                    if (i + j) % 2 == 0:
                        pygame.draw.rect(screen, white, (i * square, j * square, square, square))
                    else:
                        pygame.draw.rect(screen, color_of_board, (i * square, j * square, square, square))

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

    def end_game():
            end_mat = pygame.Surface((400, 200))
            text_mat = font_1.render("MAT", False, 'Red')
            screen.blit(end_mat, (200, 300))
            screen.blit(text_mat, (315, 370))
            pygame.display.update()  
            time.sleep(3)
            global running
            running = False


    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Chess by Ollkyl")
    icon = pygame.image.load("images/chess_icon.png")
    pygame.display.set_icon(icon)
    screen.fill((143, 109, 88))
    white = (255, 255, 255)
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


    pawn_1_pos_white = Pawn("pawn", "white", 0, 1, white_pawn_image, 0)
    pawn_2_pos_white = Pawn("pawn", "white", 1, 1, white_pawn_image, 0)
    pawn_3_pos_white = Pawn("pawn", "white", 2, 1, white_pawn_image, 0)
    pawn_4_pos_white = Pawn("pawn", "white", 3, 1, white_pawn_image, 0)
    pawn_5_pos_white = Pawn("pawn", "white", 4, 1, white_pawn_image, 0)
    pawn_6_pos_white = Pawn("pawn", "white", 5, 1, white_pawn_image, 0)
    pawn_7_pos_white = Pawn("pawn", "white", 6, 1, white_pawn_image, 0)
    pawn_8_pos_white = Pawn("pawn", "white", 7, 1, white_pawn_image, 0)
    knight_1_pos_white = Knight("knight", "white", 1, 0, white_knight_image, 0)
    knight_2_pos_white = Knight("knight", "white", 6, 0, white_knight_image, 0)
    bishop_1_pos_white = Bishop("bishop", "white", 2, 0, white_bishop_image, 0)
    bishop_2_pos_white = Bishop("bishop", "white", 5, 0, white_bishop_image, 0)
    rook_1_pos_white = Rook("rook", "white", 0, 0, white_rook_image, 0)
    rook_2_pos_white = Rook("rook", "white", 7, 0, white_rook_image, 0)
    queen_pos_white = Queen("queen", "white", 3, 0, white_queen_image, 0)
    king_pos_white = King("king", "white", 4, 0, white_king_image, 0)

    pawn_1_pos_black = Pawn("pawn", "black", 0, 6, black_pawn_image, 0)
    pawn_2_pos_black = Pawn("pawn", "black", 1, 6, black_pawn_image, 0)
    pawn_3_pos_black = Pawn("pawn", "black", 2, 6, black_pawn_image, 0)
    pawn_4_pos_black = Pawn("pawn", "black", 3, 6, black_pawn_image, 0)
    pawn_5_pos_black = Pawn("pawn", "black", 4, 6, black_pawn_image, 0)
    pawn_6_pos_black = Pawn("pawn", "black", 5, 6, black_pawn_image, 0)
    pawn_7_pos_black = Pawn("pawn", "black", 6, 6, black_pawn_image, 0)
    pawn_8_pos_black = Pawn("pawn", "black", 7, 6, black_pawn_image, 0)
    knight_1_pos_black = Knight("knight", "black", 1, 7, black_knight_image, 0)
    knight_2_pos_black = Knight("knight", "black", 6, 7, black_knight_image, 0)
    bishop_1_pos_black = Bishop("bishop", "black", 2, 7, black_bishop_image, 0)
    bishop_2_pos_black = Bishop("bishop", "black", 5, 7, black_bishop_image, 0)
    rook_1_pos_black = Rook("rook", "black", 0, 7, black_rook_image, 0)
    rook_2_pos_black = Rook("rook", "black", 7, 7, black_rook_image, 0)
    queen_pos_black = Queen("queen", "black", 3, 7, black_queen_image, 0)
    king_pos_black = King("king", "black", 4, 7, black_king_image, 0)
    current_piece = Chess_piece(None, None, None, None, None, 0)


    #  list of white pieces
    white_figures = [pawn_1_pos_white, pawn_2_pos_white, pawn_3_pos_white, pawn_4_pos_white,
                    pawn_5_pos_white, pawn_6_pos_white, pawn_7_pos_white, pawn_8_pos_white, knight_1_pos_white,
                    knight_2_pos_white, bishop_1_pos_white, bishop_2_pos_white, rook_1_pos_white, rook_2_pos_white,
                    queen_pos_white, king_pos_white]

    #  list of black pieces
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
        def game(new_coordinate_x, new_coordinate_y, coordinate_x, coordinate_y, color):
            now_piece = chess_board[coordinate_x][coordinate_y]
            print("Chosen ", now_piece.color, "Turn ", color)
            if now_piece.color == color:
                if isinstance(now_piece, Pawn):
                    if now_piece.move(new_coordinate_x, new_coordinate_y):
                        chess_board[new_coordinate_x][new_coordinate_y].image = pygame.Surface((0, 0))
                        chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                        chess_board[coordinate_x][coordinate_y] = Chess_piece('_', '_', coordinate_x, coordinate_y, None, 0)
                        return True
                elif isinstance(now_piece, Knight):
                    if now_piece.move(new_coordinate_x, new_coordinate_y):
                        chess_board[new_coordinate_x][new_coordinate_y].image = pygame.Surface((0, 0))
                        chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                        chess_board[coordinate_x][coordinate_y] = Chess_piece('_', '_', coordinate_x, coordinate_y, None, 0)
                        return True
                elif isinstance(now_piece, Bishop):
                    if now_piece.move(new_coordinate_x, new_coordinate_y):
                        chess_board[new_coordinate_x][new_coordinate_y].image = pygame.Surface((0, 0))
                        chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                        chess_board[coordinate_x][coordinate_y] = Chess_piece('_', '_', coordinate_x, coordinate_y, None, 0)
                        return True
                elif isinstance(now_piece, Rook):
                    if now_piece.move(new_coordinate_x, new_coordinate_y):
                        chess_board[new_coordinate_x][new_coordinate_y].image = pygame.Surface((0, 0))
                        chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                        chess_board[coordinate_x][coordinate_y] = Chess_piece('_', '_', coordinate_x, coordinate_y, None, 0)
                        return True
                elif isinstance(now_piece, Queen):
                    if now_piece.move(new_coordinate_x, new_coordinate_y):
                        chess_board[new_coordinate_x][new_coordinate_y].image = pygame.Surface((0, 0))
                        chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                        chess_board[coordinate_x][coordinate_y] = Chess_piece('_', '_', coordinate_x,  coordinate_y, None, 0)
                        return True
                elif isinstance(now_piece, King):
                    if now_piece.move(new_coordinate_x, new_coordinate_y):
                        chess_board[new_coordinate_x][new_coordinate_y].image = pygame.Surface((0, 0))
                        chess_board[new_coordinate_x][new_coordinate_y] = now_piece
                        chess_board[coordinate_x][coordinate_y] = Chess_piece('_', '_', coordinate_x,  coordinate_y, None, 0)
                        return True
                else:
                    print("Not find")
                    return False
            else:
                print("False turn")
                return False
            

        def start_match(color_of_board, value_music):
            global color
            color = 'white'
            global running
            running = True
            board(color_of_board)
            music(value_music)
            pygame.display.update()
            click_counter = 0
            while running:
                board(color_of_board)
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
                            click_counter = 0
                            if Game.game(int(new_row), int(new_col), int(now_row), int(now_col), color): 
                                if color == 'white':
                                    color = 'black'
                                else:
                                    color = 'white'
                        pygame.display.update()  
                        pygame.display.flip() 
                        
            print("Game Over") 
    Game.start_match(color_of_board, value_music)  
