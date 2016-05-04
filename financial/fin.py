
def kaufkraftverlust(betrag, zins, jahre=1):
    return(betrag * (1-(1/1+(zins/100.0)))**jahre)
