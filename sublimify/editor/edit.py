from sublimify.subliminals.sub import Subliminals
from sublimify.utils.add_text import add_text
from PIL import Image
import numpy as np
import threading
from multiprocessing.pool import ThreadPool
import random

from sublimify.utils.decide_color import decide_color


class Editor:
    """
    Edits the images and puts the subliminals on it.

    Attributes:
        image_path (str): The path to the image.
        subliminals (Subliminals): The subliminals object.
        show (bool): Si deberiamos dibujar una imagen para ver los subliminales.
        image (Image): La imagen.
        show_image (Image): La imagen con los subliminales.

    // Properties:

    Methods:
        add_subliminal: Pone un subliminal en la imagen.
        add_subliminals: Pone los subliminales en la imagen.
    """
    def __init__(self, image_path, subliminals: Subliminals, show=False, save_seperate=False, image=None) -> None:
        self.image_path = image_path
        self.subliminals = subliminals
        self.image = None
        self.show_image = None

        self.__setup__(image, show, save_seperate)

    def __setup__(self, image, show, save_seperate):
        """
        Configura el editor.
        """
        # Abre el imagen
        self.image = image if image else Image.open(self.image_path)

        # Chequea si queremos guardar la imagen seperado al source.
        if save_seperate:
            # Guarda la vaina!
            self.image_path = self.image_path.split('.')[0] + '_subliminal.png'

        # Actualiza el show_image
        if show:
            self.show_image = self.image.copy()

    def __document_subliminal__(self, x, y, subliminal):
        """
        Dibuja un circulo en la imagen.

        Args:
            x (int): La posicion x del circulo.
            y (int): La posicion y del circulo.
            subliminal (str): El subliminal.
        """
        # draw = ImageDraw.Draw(self.show_image)
        # draw.ellipse((x - 20, y - 20, x + 20, y + 20), outline='blue')
        add_text(self.show_image, subliminal, color='black', position=(x, y), save=False, font=self.subliminals.font)
        self.show_image.save(self.image_path.split('.')[0] + '_obvious.png')

    def add_subliminal(self, subliminal: str, save=True, position=None):
        """
        Pon un subliminal en la imagen.

        Args:
            subliminal (str): El subliminal a poner.
            save (bool): Si guardar la imagen o no.
            position (tuple): La posicion del subliminal.
        """
        # Converte el imagen a un array de numpy.
        image_array = np.array(self.image)
        # Busca sizeo de text
        text_size = self.subliminals.get_message_size(subliminal)
        # El max que puede ser un x o y del mensaje
        max_x = self.image.width - text_size[0]
        max_y = self.image.height - text_size[1]
        
        # Hacemos loop para cada vez que deberiamos poner este subliminal.
        for _ in range(self.subliminals.amount):
            # Chequea si el usario paso un position.
            if position:
                x, y = position
            else:
                # Obtenemos una posicion random.
                x, y = np.random.randint(0, max_x), \
                    np.random.randint(0, max_y)

            # Pon el text
            add_text(self.image, subliminal, 'black', (x, y), font=self.subliminals.font, save=False)
            if self.show_image:
                self.__document_subliminal__(x, y, subliminal)
            # Si ya pasaron un position significa que solo estamos haciendo uno
            if position:
                break

        # Creamos un nuevo objeto de imagen.
        cia = np.array(self.image)

        # Buscamos la differencia en los pixels de image y changed_image.
        difference = (image_array != cia).nonzero()
        # Differencias en x y y.
        x_difference = difference[1]
        y_difference = difference[0]
        
        # Ahora un loop desde los differencias para camuflar los subliminales.
        for i in range(len(x_difference)):
            # Obtenemos la posicion de la imagen.
            loc_x = x_difference[i]
            loc_y = y_difference[i]

            skip = self.subliminals.skip_pixel((loc_x, loc_y))

            # Buscamos el pixel currentamente y lo cambiamos.
            current_pixel = image_array[loc_y, loc_x]
            color_to_change_into = decide_color(current_pixel, self.subliminals.visibility)
            # Chequea si deberiamos cambiar el pixel o no
            if skip:
                color_to_change_into = current_pixel

            # Ahora cambia la vaina
            # cia[loc_y, loc_x] = color_to_change_into
            self.image.putpixel((loc_x, loc_y), tuple(color_to_change_into))

        # Set el imagen a el changed_image con fromArray
        # self.image = Image.fromarray(cia)

        if save:
            self.image.save(self.image_path)

    def add_subliminals(self):
        """
        Pon los subliminales en el photo.
        """
        # print(self.subliminals.messages)
        threads = []
        for subliminal in self.subliminals.messages:
            thread = threading.Thread(target=self.add_subliminal, args=(subliminal, False))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        self.image.save(self.image_path)


def find_best(subliminals: Subliminals, image_path):
    """
    Find the best arguments for this picture.
    
    Important:
        Use a large Subliminal.visibility, this method will loop through each level of visibility,
        starting with the highest and dropping until the lowest.
        The images will go into a folder based on the name of the file with a _train at the end of the name.
    
    Params:
        subliminals (Subliminals): The subliminals object.
        image_path (str): The path to the image.
    """
    from pathlib import Path
    import os

    pool = ThreadPool(processes=subliminals.visibility)
    requests = []

    base_path = f"images/{image_path.split('/')[-1].split('.')[0]}_train/"

    # Chequea si ya exista un path para los imagenes
    if not Path("images").exists():
        # Crea lo
        os.mkdir("images")

    if not Path(base_path).exists():
        os.mkdir(base_path)

    def find(path, subliminals):
        new_image = Image.open(path)
        new_image_path = base_path + path.split('/')[-1].split('.')[0] + f'_train{subliminals.visibility}.png'
        new_image.save(new_image_path)
        Editor(new_image_path, subliminals).add_subliminals()

    for i in range(subliminals.visibility, 0, -1):
        subs = Subliminals(messages=subliminals.messages, visibility=i, amount=subliminals.amount)
        requests.append(pool.apply_async(find, (image_path, subs)))

    for req in requests:
        req.get()
        print(f"Terminado {requests.index(req) + 1} out of {len(requests)}")