"""
This file is used specifically to generate the starter images for the
sublimifier.
"""
from PIL import Image


IMAGES_BASE = "images/"


def create_image(path, color):
    image = Image.new("RGB", (500, 500), color)
    image.save(path)


def white_image():
    create_image(IMAGES_BASE + "white.png", (255, 255, 255))
    return IMAGES_BASE + "white.png"


def black_image():
    create_image( IMAGES_BASE + "black.png", (0, 0, 0))
    return  IMAGES_BASE + "black.png"


def red_image():
    create_image (IMAGES_BASE + "red.png", (255, 0, 0))
    return  IMAGES_BASE + "red.png"


def orange_image():
    create_image (IMAGES_BASE + "orange.png", (255, 165, 0))
    return  IMAGES_BASE + "orange.png"


def blue_image():
    create_image (IMAGES_BASE + "blue.png", (0, 0, 255))
    return  IMAGES_BASE + "yellow.png"


def green_image():
    create_image (IMAGES_BASE + "green.png", (0, 255, 0))
    return  IMAGES_BASE + "green.png"


def green_blue_image():
    create_image (IMAGES_BASE + "green_blue.png", (0, 255, 255))
    return  IMAGES_BASE + "green_blue.png"


def yellow_image():
    create_image (IMAGES_BASE + "yellow.png", (255, 255, 0))
    return  IMAGES_BASE + "yellow.png"