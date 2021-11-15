"""
El font del mensaje para el subliminal.
"""
from PIL import ImageFont
import random
import os


# Fonts son la familia de Roboto, la fuente de Google.
FONTS = [
    'Roboto-Regular',
    'Roboto-Medium',
    'Roboto-Bold',
    'Roboto-Thin',
    'Roboto-Light',
    'Roboto-Black',
    'Roboto-Italic',
    'Roboto-MediumItalic',
    'Roboto-BoldItalic',
    'Roboto-ThinItalic',
    'Roboto-LightItalic',
    'Roboto-BlackItalic',
]


def choose_font(font_name: str = None, size: int = None):
    """
    Selectar el font.

    Params:
        - font_name: str
            El nombre del font.
        - size: int
            El size del font.

    Returns:
        - ImageFont 
    """
    base_font_path = "C:/Users/jorda/Documents/Python_Projects/Sublimify/fonts/" + 'Roboto/'
    if font_name is None:
        font_name = FONTS[random.randint(0, len(FONTS) - 1)]
    if size is None:
        size = random.randint(30, 50)

    # print(f"Font: {font_name}, size: {size}")

    font_path = base_font_path + font_name + ".ttf"

    image_font = ImageFont.truetype(font_path, size)
    return image_font