from sublimify.editor.edit import Editor, Subliminals
from sublimify.subliminals.sub import SkipMethods


POSSIBLE_IMAGES = [
    "Saveriu_#92.png",
    "Sixten_#88.png",
    "Stojko_#89.png",
    "Theodotus_#97.png",
    "Visvaldas_#94.png",
    "Bonifacio_#97.png",
    "jordan.jpg",
    "fam.jpg",
    "dad.jpg"
]


def main(image):
    subliminals = Subliminals(["SEX"], 20, 5, skip_method=SkipMethods.POS)
    editor = Editor(image, subliminals, True, True)

    editor.add_subliminals()


if __name__ == '__main__':
    image = "images/" + POSSIBLE_IMAGES[-1]
    main(image)