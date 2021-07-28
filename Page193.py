def repToInt(repString, base):
    """Converts the repString to an int in the base and
    returns this int."""
    decimal = 0
    exponent = len(repString) - 1
    for digit in repString:
        decimal = decimal + int(digit) * base ** exponent
        exponent -= 1
        return decimal
