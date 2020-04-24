def afficher_flottant(value):
    if type(value) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")

    text = str(value)
    # tab = text.split(".")
    # decimals = tab[1]
    # return tab[0] + "," + decimals[0:3]

    partie_entiere, partie_flottante = text.split(".")
    return ",".join([partie_entiere, partie_flottante[:3]])


print(afficher_flottant(3.999999999))
