#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6


# Imports
import argparse
import csv

# Variables
csv_file = 'listeVals.csv'
listeVals = []
lengthListe = len(listeVals)


# Functions

# Read in a file
def read_in_file():
    with open(csv_file, "r") as f:
        read = csv.reader(f)
        for row in read:
            for l in range(len(row)):
                if len(row) > 0:
                    listeVals.append(row[l])


# Write to a file
def write_in_file(msg):
    with open(csv_file, 'w') as f:
        write = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write.writerow(msg)


# Suppr all items in list
def suppr_all_items():
    while lengthListe != 0:
        listeVals.remove([0])
    write_in_file(listeVals)
    print('Toutes les valeurs sont effaces !')


# Get max value
def max_val(arr):
    max = arr[0]
    for item in arr:
        if item > max:
            max = item
    return max


# Get min value
def min_val(arr):
    min = arr[0]
    for item in arr:
        if item < min:
            min = item
    return min


# Args
parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add_argument("-l", action="store_true", help="Affiche le contenu de la liste")
parser.add_argument("-a", nargs="*", help="Ajoute les items dans la liste")
parser.add_argument("-c", action="store_true", help="Supprime tous les éléments de la liste")
parser.add_argument("-s", "--max", action="store_true", help="Affiche la valeur maximum contenu dans la liste")
parser.add_argument("-s", "--min", action="store_true", help="Affiche la valeur minimum contenu dans la liste")
parser.add_argument("-s", "--moy", action="store_true", help="Affiche la moyenne de tous les éléments dans la liste.")
parser.add_argument("-s", "--sum", action="store_true", help="Affiche la somme de tous les éléments dans la liste.")
parser.add_argument("-t", action="store_true", help="Trie la liste dans l’ordre croissant.")
parser.add_argument("--desc", action="store_true", help="Trie la liste dans l’ordre decroissant.")
parser.add_argument("--help", action="store_true", help="Affiche le manuel d’utilisation de cette commande.")
args = parser.parse_args()

# Program

if args.l:
    read_in_file()
    for nbr in listeVals:
        print(nbr)

elif args.a:
    for val in args.a:
        if val.isdigit():
            listeVals.append(val)
            write_in_file(listeVals)
            print('Valeur', val, 'ajoute')
        else:
            print('Entrez un nombre entier svp')
            exit()

elif args.c:
    suppr_all_items()

elif args.max:
    read_in_file()
    rows = [int(row) for row in listeVals]
    highest = max_val(rows)
    print('La plus grosse valeur est', highest)

elif args.min:
    read_in_file()
    rows = [int(row) for row in listeVals]
    lowest = min_val(rows)
    print('La plus petite valeur est', lowest)

elif args.moy:
    read_in_file()
    rows = [int(row) for row in listeVals]
    moy = (sum(rows) / len(listeVals))
    print('La moyenne des valeurs est de', moy)

elif args.sum:
    read_in_file()
    rows = [int(row) for row in listeVals]
    total = sum(rows)
    print('La somme total est de', total)

elif args.t:
    read_in_file()
    rows = [int(row) for row in sorted(listeVals, key=int)]
    print('Trie par ordre croissant:', rows)

elif args.desc:
    read_in_file()
    rows = [int(row) for row in sorted(listeVals, key=int, reverse=True)]
    print('Trie par ordre decroissant:', rows)

else:
    parser.print_help()
