import os
import sys

def getcwd():
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return base_path

#PATHS
ROOT_DIR = getcwd()
RESOURCES_DIR = os.path.join(ROOT_DIR, 'resources')
FONTS_DIR = os.path.join(RESOURCES_DIR, 'fonts')
IMAGES_DIR = os.path.join(RESOURCES_DIR, 'images')
MUSIC_DIR = os.path.join(RESOURCES_DIR, 'music')

# FONTS 
FONT_MOKOTO  = os.path.join(FONTS_DIR, 'mokoto.ttf')
FONT_MOKOTO2 = os.path.join(FONTS_DIR, 'mokoto2.ttf')

# IMAGES
IMG_WOOD_SETTINGS = os.path.join(IMAGES_DIR, 'wood_settings.jpg')
IMG_WOOD = os.path.join(IMAGES_DIR, 'wood.jpg')

# FIGURES
IMG_PAWN_WHITE = os.path.join(IMAGES_DIR, 'pawnwhite.png')
IMG_PAWN_BLACK = os.path.join(IMAGES_DIR, 'pawnblack.png')
IMG_KNIGHT_WHITE = os.path.join(IMAGES_DIR, 'knightwhite.png')
IMG_KNIGHT_BLACK = os.path.join(IMAGES_DIR, 'knightblack.png')
IMG_BISHOP_WHITE = os.path.join(IMAGES_DIR, 'bishopwhite.png')
IMG_BISHOP_BLACK = os.path.join(IMAGES_DIR, 'bishopblack.png')
IMG_ROOK_WHITE = os.path.join(IMAGES_DIR, 'rookwhite.png')
IMG_ROOK_BLACK = os.path.join(IMAGES_DIR, 'rookblack.png')
IMG_QUEEN_WHITE = os.path.join(IMAGES_DIR, 'queenwhite.png')
IMG_QUEEN_BLACK = os.path.join(IMAGES_DIR, 'queenblack.png')
IMG_KING_WHITE = os.path.join(IMAGES_DIR, 'kingwhite.png')
IMG_KING_BLACK = os.path.join(IMAGES_DIR, 'kingblack.png')

# MUSIC
MUSIC_CHESS = os.path.join(MUSIC_DIR, 'chess_music.mp3')