"""
El font del mensaje para el subliminal.
"""
from PIL import ImageFont
import random
import os


# Fonts son la familia de Roboto, la fuente de Google.
FONTS = {
    'Roboto': [
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
    ],
    'ComforterBrush': [
        'ComforterBrush-Regular'
    ],
    'Praise': [
        'Praise-Regular'
    ]
}


def choose_font(font_fam: str = None, font_name: str = None, size: int = None):
    """
    Selectar el font.

    Params:
        - font_fam: str
            El nombre de la familia de font.
        - font_name: str
            El nombre del font.
        - size: int
            El size del font.

    Returns:
        - ImageFont 
    """
    base_font_path = "C:/Users/jorda/Documents/Python_Projects/Sublimify/fonts/"

    # Check if the font family is valid.
    if font_fam is None or font_fam not in FONTS.keys():
        # Choose a random font family.
        font_fam = random.choice(list(FONTS.keys()))
    # CHeck if the font itself is valid.
    if font_name is None or font_name not in FONTS:
        # Choose a random font.
        font_name = random.choice(FONTS[font_fam])
    if size is None:
        size = random.randint(30, 50)

    # print(f"Font: {font_name}, size: {size}")

    font_path = base_font_path + f'{font_fam}/' + font_name + ".ttf"

    image_font = ImageFont.truetype(font_path, size)
    return image_font
