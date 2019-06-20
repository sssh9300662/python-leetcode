import numpy

def find_next_square(sq):
    result = numpy.sqrt(sq)
    if result.is_integer():
        return int(numpy.square(result+1))
    # Return the next square if sq is a square, -1 otherwise
    return -1


if __name__ == "__main__":
    print(find_next_square(121))