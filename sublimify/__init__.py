from sublimify.editor.edit import Editor, Subliminals
from sublimify.subliminals.sub import SkipMethods


def sublimify(image_path, subliminals: Subliminals, position=None, debug=False, seperate_files=False, show_locations=False, image=None):
    """
    Ponemos subliminales en una posición.

    Params:
        - image_path (str): El path al archivo del imagen.
        - subliminals (Subliminals): Los subliminales para poner en el imagen.
        - position (tuple[int, int]): La posición en la que se quiere poner el subliminal.
        - debug (bool): Si se quiere ver el resultado.
        - seperate_files (bool): Si se quiere guardar los resultados en archivos separados.
        - show_locations (bool): Si se quiere ver las ubicaciones de los subliminales.
    """
    if debug:
        print(f'Subliminals.messages: {subliminals.messages}')
        print(f'Subliminals.spacing: {subliminals.spacing}')
        print(f'Subliminals.visibility: {subliminals.visibility}')
        print(f'Subliminals.amount: {subliminals.amount}')
        print(f'Subliminals.font: {subliminals.font}')

    if position:
        sublimify_on_position(image_path, subliminals, position, debug, seperate_files, show_locations, image)
    else:    
        editor = Editor(image_path, subliminals, show_locations, seperate_files, image)
        editor.add_subliminals()

    if debug:
        print("Subliminals added")


def sublimify_on_position(image_path, subliminals: Subliminals, position, debug=False, seperate_files=False, show_locations=False, image=None):
    """
    Ponemos subliminales en una posición.

    Params:
        - image_path (str): El path al archivo del imagen.
        - subliminals (Subliminals): Los subliminales para poner en el imagen.
        - position (int): La posición en la que se quiere poner el subliminal.
    """
    editor = Editor(image_path, subliminals, show_locations, seperate_files, image)
    editor.add_subliminal(subliminal=subliminals.messages[0], position=position)
