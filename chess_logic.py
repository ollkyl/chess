from main import current_piece


class Common:
    def __init__(self, piece, color, coordinate_x, coordinate_y, image):
        self.piece = piece
        self.color = color
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.new_coordinate_x = None
        self.new_coordinate_y = None
        self.mat = 0

    def cheking_position(self, new_coordinate_x, new_coordinate_y):  # проверка выхода за границы доски
        if not (0 <= new_coordinate_y <= 7) and not (0 <= new_coordinate_x <= 7):
            print("False  cheking_position 1")
            return False
        elif chess_board[new_coordinate_x][new_coordinate_y].color == self.color:
            print("False  cheking_position 3")
            return False
        elif chess_board[new_coordinate_x][new_coordinate_y].piece == "king":
            print("MAT")
            current_piece.mat = 1
            return True
        else:
            return True

    @staticmethod
    #  препятствия на пути
    def way(coordinate_x, coordinate_y, new_coordinate_x, new_coordinate_, direction_x, direction_y):
        way_x = coordinate_x
        way_y = coordinate_y
        while (way_x != new_coordinate_x) and (way_y != new_coordinate_):
            if chess_board[way_x + direction_x][way_y + direction_y] == "____":
                way_x += direction_x
                way_y += direction_y
            else:
                print("False  def way")
                return False
        return True


class Pawn(Common):  # пешка
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
        elif (new_coordinate_y - self.coordinate_y == direction) and (chess_board[new_coordinate_x][new_coordinate_y].piece == "____"):
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


class Knight(Common):  # конь
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


class Bishop(Common):  # слон
    def move(self, new_coordinate_x, new_coordinate_y):
        print("Inside Bishop move method")
        self.new_coordinate_x = new_coordinate_x
        self.new_coordinate_y = new_coordinate_y
        direction_x = new_coordinate_x - self.coordinate_x
        direction_y = new_coordinate_y - self.coordinate_y
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


class Rook(Common):  # ладья
    def move(self, new_coordinate_x, new_coordinate_y):
        print("Inside Rook move method")
        self.new_coordinate_x = new_coordinate_x
        self.new_coordinate_y = new_coordinate_y
        direction_x = new_coordinate_x - self.coordinate_x
        direction_y = new_coordinate_y - self.coordinate_y
        if self.cheking_position(new_coordinate_x, new_coordinate_y):
            # проверка на движение только по вертикали
            if (new_coordinate_x - self.coordinate_x == 0) and (new_coordinate_y - self.coordinate_y != 0):
                if self.way(self.coordinate_x, self.coordinate_y, new_coordinate_x, new_coordinate_y, direction_x,
                            direction_y):
                    self.coordinate_x = new_coordinate_x
                    self.coordinate_y = new_coordinate_y
                    return True
                else:
                    return False
            # проверка на движение только по горизонтали
            elif (new_coordinate_x - self.coordinate_x != 0) and (new_coordinate_y - self.coordinate_y == 0):
                if self.way(self.coordinate_x, self.coordinate_y, new_coordinate_x, new_coordinate_y, direction_x,
                            direction_y):
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


class Queen(Common):
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


class King(Common):
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


chess_board = [[Common('____', '____', -1, -1) for _ in range(8)] for _ in range(8)]
