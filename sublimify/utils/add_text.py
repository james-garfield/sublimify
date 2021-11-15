"""
Handles adding text to any image.
"""
from PIL import ImageDraw


def add_text(image, text, color=None, position=None, font=None, save=True):
    """
    Pon texto en un imagen.

    Params:
        - image (Image): El imagen,
        - text (str): El text para poner en el imagen.
        - color (tuple): El color del texto.
        - position (tuple): La posición del texto.
        - font (ImageFont): La fuente del texto.
        - save (bool): Si se quiere guardar el archivo.
        - spacing (int): El espaciado entre letras.
    """
    # Crea un Draw
    draw = ImageDraw.Draw(image, 'RGBA')
    
    draw.text(position, text, color, font=font)
    if save:
        # Guarda la imagen
        image.save(image.filename)
        