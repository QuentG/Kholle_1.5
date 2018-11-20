#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6


# Imports
import argparse
import csv
import sys

# Functions


# Args
parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add_argument("-l", action="store_true", help="Affiche le contenu de la liste")
parser.add_argument("-a liste", action="store_true", help="Ajoute les items dans la liste")
parser.add_argument("-c", action="store_true", help="Supprime tous les éléments de la liste")
parser.add_argument("-s", "--max", action="store_true", help="Affiche la valeur maximum contenu dans la liste")
parser.add_argument("-s", "--min", action="store_true", help="Affiche la valeur minimum contenu dans la liste")
parser.add_argument("-s", "--moy", action="store_true", help="Affiche la moyenne de tous les éléments dans la liste.")
parser.add_argument("-s", "--sum", action="store_true", help="Affiche la somme de tous les éléments dans la liste.")
parser.add_argument("-t", action="store_true", help="Trie la liste dans l’ordre croissant.")
parser.add_argument("-t", "--desc", action="store_true", help="Trie la liste dans l’ordre decroissant.")
parser.add_argument("--help", action="store_true", help="Affiche le manuel d’utilisation de cette commande.")
args = parser.parse_args()

# Variables

# Program

