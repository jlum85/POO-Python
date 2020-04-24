inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
]


def takeSecond(elem):
    return elem[1]


# tri en fonction du 2ème élément du tuple en sens décroissant
inventaire.sort(key=takeSecond, reverse=True)

print('Sorted list:', inventaire)
# [
#     ("fraises", 76),
#     ("prunes", 51),
#     ("pommes", 22),
#     ("poires", 18),
#     ("melons", 4),
# ]

#  autre méthode
# On change le sens de l'inventaire, la quantité avant le nom
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit, qtt in inventaire]
# On trie l'inventaire inversé dans l'ordre décroissant
inventaire_inverse.sort(reverse=True)
# Et on reconstitue l'inventaire
inventaire = [(nom_fruit, qtt) for qtt, nom_fruit in inventaire_inverse]
