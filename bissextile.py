# Une année est dite bissextile si c'est un multiple de 4, sauf si c'est un multiple de 100.
# Toutefois, elle est considérée comme bissextile si c'est un multiple de 400. Je développe :

# Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
# Si elle est multiple de 4, on regarde si elle est multiple de 100.
# Si c'est le cas, on regarde si elle est multiple de 400.
# Si c'est le cas, l'année est bissextile.
# Sinon, elle n'est pas bissextile.
# Sinon, elle est bissextile.

# ma méthode
annee = input("Saisissez une année : ")
year = int(annee)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(annee + " est bissextile ")
else:
    print(annee + " n'est pas bissextile !")
