import math
import random

def aleator(max, min):
    """_summary_

    Args:
        max (_type_): _description_
        min (_type_): _description_

    Returns:
        _type_: _description_
    """
    return random.randint(min, max)

# array aleatorio
def aleator_array(max, min, size):
    """_summary_

    Args:
        max (_type_): _description_
        min (_type_): _description_
        size (_type_): _description_

    Returns:
        _type_: _description_
    """
    return [aleator(max, min) for i in range(size)]

print(aleator_array(10, 0, 10))