"""
Script to decide the color to change the pixel to.
"""


def decide_color(current: tuple[int, int, int], amount: int):
    """
    Decides the color to change the pixel to.

    Params:
        - current (tuple[int, int, int]): El color currentamente.
        - amount (int): La cantidad de veces que se ha llamado a la función.

    Returns:
        - tuple[int, int, int]
    """
    # Color mas brillante
    brighther_color = tuple(map(lambda x: x + amount, current))
    # Color mas oscuro
    darker_color = tuple(map(lambda x: x - amount, current))

    if is_close_enough(current, (255, 255, 255), amount):
        return darker_color
    else:
        return brighther_color

def is_close_enough(current: tuple[int, int, int], target: tuple[int, int, int], diff=20):
    """
    Checks if the current color is close enough to the target color.

    Params:
        - current (tuple[int, int, int]): El color actual.
        - target (tuple[int, int, int]): El color objetivo.
        - difference (int): La differencia máxima permitida.

    Returns:
        - bool
    """
    # Get the mean of the numbers of the current color tuple
    current_mean = sum(current) / 3
    # Get the target mean
    target_mean = sum(target) / 3

    # Convert negative values to positive
    difference = abs(current_mean - target_mean)

    return difference <= diff