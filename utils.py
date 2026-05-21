def to_binary(value):

    if value < 0:
        return "-" + bin(abs(value))[2:]

    return bin(value)[2:]