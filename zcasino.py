# Le joueur mise sur un numéro compris entre 0 et 49 (50 numéros en tout).
# En choisissant son numéro, il y dépose la somme qu'il souhaite miser.

# La roulette est constituée de 50 cases allant naturellement de 0 à 49.
# Les numéros pairs sont de couleur noire, les numéros impairs sont de couleur rouge.

# Si le numéro gagnant est celui sur lequel le joueur a misé (probabilité de 1/50, plutôt faible)
# , le croupier lui remet 3 fois la somme misée.

# Sinon, le croupier regarde si le numéro misé par le joueur est de la même couleur que le numéro gagnant
# (s'ils sont tous les deux pairs ou tous les deux impairs).
# Si c'est le cas, le croupier lui remet 50 % de la somme misée. Si ce n'est pas le cas, le joueur perd sa mise.

import random
import math


class Casino:

    def __init__(self, choice, money):
        self.choice = int(choice)
        self.money = money

    def play(self):
        draw = random.randrange(50)
        print("La roulette tourne... ... et s'arrête sur le numéro", draw)
        result = 0
        if draw == self.choice:
            result = self.money * 3
            print("Gagné  : {} * 3 = {} ".format(str(self.money), str(result)))
        elif (draw % 2 == 0 and self.choice % 2 == 0) or (draw % 2 != 0 and self.choice % 2 != 0):
            result = math.ceil(self.money * -0.5)
            print(
                "Même couleur :  {} * 0,5 = {} ".format(str(self.money), str(result)))
        else:
            result = -self.money
            print("Perdu !!g")
        return result


def select_Number():
    choice = -1
    while choice < 0 or choice > 49:
        choice = input(
            "Tapez le nombre sur lequel miser(de 0 à 49). Tapez [q] pour quitter\n")
        if choice == 'q':
            break

        # On convertit le nombre misé sauf si on quitte
        try:
            choice = int(choice)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            choice = -1
            continue

        if choice < 0:
            print("Ce nombre est négatif")
        elif choice > 49:
            print("Ce nombre est supérieur à 49")

    return choice


def select_Mise(max):
    mise = 0
    while mise <= 0 or mise > max:
        mise = input("Tapez le montant de votre mise : ")
        # On convertit la mise
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise <= 0:
            print("La mise saisie est négative ou nulle.")
        if mise > max:
            print("Vous ne pouvez miser autant, vous n'avez que", max, "$")
    return mise


def main_loop():
    funds = 50
    while True:
        print("Somme d'argent disponible {}".format(str(funds)))

        choice = select_Number()
        if choice == 'q':
            print("On quitte la partie, argent restant : ", funds)
            break

        amount = select_Mise(funds)

        game = Casino(choice, amount)
        funds += game.play()
        if funds <= 0:
            print("Partie terminé, vous n'avez plus d'argent !!!")
            break


main_loop()
