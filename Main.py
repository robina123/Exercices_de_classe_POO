from math import pi
import random


class StringFoo:
    def __init__(self):
        self.string = "a"

    def set_string(self, string):
        self.string = string

    def print_string(self):
        print(self.string.upper())


class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    def calcul_aire(self):
        return self.largeur * self.longueur

    def afficher_infos(self):
        print("largeur: ", self.largeur, "longueur: ", self.longueur, "aire: ", self.calcul_aire())


class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calcul_aire(self):
        return pi * self.rayon ** 2

    def calcul_circonference(self):
        return 2 * pi * self.rayon


class Hero:
    def __init__(self, nom):
        self.point_de_vie = random.randint(1, 10) + random.randint(1, 10)
        self.attaque = random.randint(1, 6)
        self.defense = random.randint(1, 6)
        self.nom = nom

    def faire_une_attaque(self):
        return random.randint(1, 6) + self.attaque

    def recevoir_dommages(self):
        self.point_de_vie -= random.randint(1, 6) + self.defense

    def est_vivant(self):
        if self.point_de_vie > 0:
            return True
        return False
