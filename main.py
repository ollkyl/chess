# import pygame
# from chess_logic import *
# from chess_graphics import *

# pygame.init()


# class Game(Common):
#     @staticmethod
#     def start_game(new_coordinate_x, new_coordinate_y, coordinate_x, coordinate_y):
#         now_piece = chess_board[coordinate_x][coordinate_y]
#         if isinstance(now_piece, Pawn):
#             if now_piece.move(new_coordinate_x, new_coordinate_y):
#                 chess_board[new_coordinate_x][new_coordinate_y] = now_piece
#                 chess_board[coordinate_x][coordinate_y] = Common('____', '____', coordinate_x,
#                                                                  coordinate_y, None)
#         elif isinstance(now_piece, Knight):
#             if now_piece.move(new_coordinate_x, new_coordinate_y):
#                 chess_board[new_coordinate_x][new_coordinate_y] = now_piece
#                 chess_board[coordinate_x][coordinate_y] = Common('____', '____', coordinate_x,
#                                                                  coordinate_y, None)
#         elif isinstance(now_piece, Bishop):
#             if now_piece.move(new_coordinate_x, new_coordinate_y):
#                 chess_board[new_coordinate_x][new_coordinate_y] = now_piece
#                 chess_board[coordinate_x][coordinate_y] = Common('____', '____', coordinate_x,
#                                                                  coordinate_y, None)
#         elif isinstance(now_piece, Rook):
#             if now_piece.move(new_coordinate_x, new_coordinate_y):
#                 chess_board[new_coordinate_x][new_coordinate_y] = now_piece
#                 chess_board[coordinate_x][coordinate_y] = Common('____', '____', coordinate_x,
#                                                                  coordinate_y, None)
#         elif isinstance(now_piece, Queen):
#             if now_piece.move(new_coordinate_x, new_coordinate_y):
#                 chess_board[new_coordinate_x][new_coordinate_y] = now_piece
#                 chess_board[coordinate_x][coordinate_y] = Common('____', '____', coordinate_x,
#                                                                  coordinate_y, None)
#         elif isinstance(now_piece, King):
#             if now_piece.move(new_coordinate_x, new_coordinate_y):
#                 chess_board[new_coordinate_x][new_coordinate_y] = now_piece
#                 chess_board[coordinate_x][coordinate_y] = Common('____', '____', coordinate_x,
#                                                                  coordinate_y, None)
#         else:
#             print("Not find")


# end_of_game = 0

# running = True
# board()
# pygame.display.update()
# while running:
#     board()
#     pygame.display.update()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             running = False


#test fgfghf