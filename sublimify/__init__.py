from sublimify.editor.edit import Editor, Subliminals
from sublimify.subliminals.sub import SkipMethods


def sublimify(image_path, subliminals=["sex"], debug=False, seperate_files=False, show_locations=False, **kwargs):
    """
    Ponemos los subliminals en un imagen.

    Params:
        - image_path (str): El path al archivo del imagen.
        - subliminals (list[str]): Los subliminales para poner en el imagen.
        - debug (bool): Si se quiere ver el resultado.
        - seperate_files (bool): Si se quiere guardar los resultados en archivos separados.
        - show_locations (bool): Si se quiere ver las ubicaciones de los subliminales.
    """
    amount = kwargs['amount'] if 'amount' in kwargs else 20
    visibility = kwargs['visibility'] if 'visibility' in kwargs else 2
    font_name = kwargs['font_name'] if 'font_name' in kwargs else None
    font_size = kwargs['font_size'] if 'font_size' in kwargs else None
    image = kwargs['image'] if 'image' in kwargs else None
    spacing = kwargs['spacing'] if 'spacing' in kwargs else None
    skip_method = kwargs['skip_method'] if 'skip_method' in kwargs else None

    subs = Subliminals(subliminals, amount, visibility, font_name, font_size, spacing, skip_method)
    if debug:
        print(f'Subliminals.messages: {subs.messages}')
        print(f'Subliminals.spacing: {subs.spacing}')
        print(f'Subliminals.visibility: {subs.visibility}')
        print(f'Subliminals.amount: {subs.amount}')
        print(f'Subliminals.font: {subs.font}')
    
    editor = Editor(image_path, subs, show_locations, seperate_files, image)
    editor.add_subliminals()

    if debug:
        print("Subliminals added")


def sublimify_on_position(image_path, subliminals: Subliminals, position):
    """
    Ponemos subliminales en una posición.

    Params:
        - image_path (str): El path al archivo del imagen.
        - subliminals (Subliminals): Los subliminales para poner en el imagen.
        - position (int): La posición en la que se quiere poner el subliminal.
    """
    editor = Editor(image_path, subliminals)
    editor.add_subliminal(subliminal=subliminals.messages[0], position=position)
