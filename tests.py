def table_multiplication(nb, max=10):
    # docstring :
    """Fonction affichant la table de multiplication par nb

    de 1 * nb à max * nb

    (max >= 0)"""
    print(">> Table des {}".format(nb))
    for num in range(1, max+1):
        print(" {} * {} = {}".format(num, nb, num * nb))


table_multiplication(2)
