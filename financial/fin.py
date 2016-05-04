
def kaufkraftverlust(betrag, inflation, jahre=1):
    return(betrag * (-1/(1+(inflation/100.0)))**jahre)

def zinszins(betrag, zins, jahre=1):
    return(betrag*(1+(zins/100.0))**jahre)


