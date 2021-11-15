import random
from sublimify.subliminals.choose_font import choose_font
from enum import Enum


class SkipMethods(Enum):
    RANDOM = 0
    POS = 1
    DONT = 2


class Subliminals:
    """
    Handles the subliminal messages. It holds the messages and the amount of messages.

    Attributes:
        - messages (list): The list of messages.
        - amount (int): The amount of times each message is written.
        - visibility (int): The visibility of the messages.
        - font (tuple[str, int]): The font of the messages.
        - spacing (int): The spacing between the letters.

    Methods:
        - get_message_radius(message): Returns the radius of the message.
        - skip_pixel((x, y)): Regresa boolean si el pixel debe ser skipped.
    """
    def __init__(self, messages, amount, visibility=2, font_name=None, font_size=None, spacing=None, skip_method: SkipMethods=None):
        self.messages = messages
        self.amount = amount
        self.visibility = visibility
        self.font = choose_font(font_name or "Roboto-Medium", font_size or 35)
        self.spacing = spacing or random.randint(0, 1)
        self.__skip_method__ = skip_method or SkipMethods.POS
        # print(f"spacing: {self.spacing}")

        # Ponemos uno spacing edentro de las palabras
        for i in range(len(self.messages)):
            message = [letter + (" " * self.spacing) for letter in self.messages[i]]
            self.messages[i] = "".join(message)

    def get_message_size(self, message) -> tuple[int, int]:
        """
        Returns the size of the message.

        Args:
            message (str): The message.

        Returns:
            tuple[int, int]: The size of the message.
        """
        return self.font.getsize(message)

    def get_message_radius(self, message) -> int:
        """
        Encuentra el radio del mensaje.

        Args:
            message (str): The message.

        Returns:
            int: The radius of the message.
        """
        return len(message) * self.font.size

    def skip_pixel(self, xy=None) -> bool:
        """
        Deberiamos hacer skip con este pixel?

        Params:
            - xy (tuple[int, int]): The pixel.

        Returns:
            bool: True if we should skip this pixel.
        """
        if self.__skip_method__ == SkipMethods.RANDOM:
            # Busca el random
            rand = random.randint(0, 10)
            return rand % 2 == 0 or rand % 3 == 0
        elif self.__skip_method__ == SkipMethods.POS:
            # Chequea que xy no sea None
            if xy is None:
                raise ValueError("xy es None")

            return xy[0] % 2 == 0 or xy[1] % 2 == 0
        elif self.__skip_method__ == SkipMethods.DONT:
            return False
        else:
            raise Exception(f"Skip method es envalido: {self.__skip_method__}")