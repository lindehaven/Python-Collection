def rectangle_area(length, width):
    return abs(length) * abs(width)

def rectangle_circ(length, width):
    return 2 * (abs(length) + abs(width))

def rectangle_aspect(length, width):
    if abs(width) != 0:
        return abs(length) / abs(width)
    else:
        return 0
