def kaufkraftverlust(betrag, inflation, jahre=1):
    return (betrag / ((1+inflation/100)** jahre))


def zinszins(betrag, zins, jahre=1):
    return betrag * (1 + (zins / 100.0)) ** jahre


def einkommensteuer(zvE):
    if zvE <= 8652:
        return 0
    elif 8653 <= zvE <= 13669:
        y = (zvE - 8652) / 10000.0
        return (993.62 * y + 1400) * y
    elif 13670 <= zvE <= 53665:
        z = (zvE - 13669) / 10000.0
        return (225.4 * z + 2397) * z + 952.48
    elif 53666 <= zvE <= 254446:
        return 0.42 * zvE - 8394.14
    elif 254447 <= zvE:
        return 0.45 * zvE - 16027.52
