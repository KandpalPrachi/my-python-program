def factors(value):
    factors = []
    factor = 2
    while value != 1:
        if value % factor == 0:
            value = value / factor
            factors.append(factor)
        else:
            factor += 1
    return factors
    