def add_integer(a, b=98):
    # Check if a and b are either integers or floats
    if not (isinstance(a, int) or isinstance(a, float)) or not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    # Return the addition of a and b
    return a + b
