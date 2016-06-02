
def kaufkraftverlust(betrag, inflation, jahre=1):
    return(betrag * (-1/(1+(inflation/100.0)))**jahre)

def zinszins(betrag, zins, jahre=1):
    return(betrag*(1+(zins/100.0))**jahre)

def einkommensteuer(zvE):
    if zvE <= 8652:
        return 0
    elif zvE >= 8653 and zvE <= 13669:
        y=(zvE-8652)/10000.0
        return (993.62 * y + 1400) * y
    elif zvE >= 13670 and zvE <= 53665:
        z=(zvE - 13669)/10000.0
        return (225.4 * z + 2397) * z + 952.48
    elif zvE >= 53666 and zvE <= 254446:
        return 0.42 * zvE - 8394.14
    elif zvE >= 254447:
        return 0.45 * zvE - 16027.52


