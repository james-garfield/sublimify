# """
# Hacemos un enhance para que es mas facil poner los subliminales en un photo.
# """
# from typing import Union
# import cv2
# from PIL import Image
# import numpy as np


# def enhance_image(image: Union[Image.Image, str]):
#     """
#     Enhance un imagen desde el path del imagen.

#     Params:
#         - image (Image | str): El path al archivo.
#     """
#     if isinstance(image, str):
#         # Abre la imagen con opencv
#         img = cv2.imread(image)
#     else:
#         # Converte el imagen (Pillow) a un OPEN CV
#         array = np.array(image)
#         # El imagen viene del numpy array
#         img = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
#     # Aplica una transformacion de la imagen
#     dst = cv2.detailEnhance(img, 10, 100)

#     return Image.fromarray(dst)