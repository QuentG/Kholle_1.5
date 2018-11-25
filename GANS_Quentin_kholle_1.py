#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

# Title : Kholle 1.5
# Description : utility for a work of simple operations, on which it will be written in a file in csv format.
# Last update : 25/11/18
# Author : Gans Quentin

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


# Create listeVals.csv
def create_file():
    with open(csv_file, "w") as new_file:
        csv.writer(new_file)
        new_file.close()
    print('The file has just been created !')


# Suppr all items in list
def suppr_all_items():
    while lengthListe != 0:
        listeVals.remove([0])
    write_in_file(listeVals)
    print('All values ​​are cleared !')


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
parser.add_argument("-l", action="store_true", help="Display the contents of the list.")
parser.add_argument("-a", nargs="*", help="Add the items to the list.")
parser.add_argument("-c", action="store_true", help="Removes all items from the list.")
parser.add_argument("-s", "--max", action="store_true", help="Displays the maximum value in the list.")
parser.add_argument("-s", "--min", action="store_true", help="Displays the minimum value in the list.")
parser.add_argument("-s", "--moy", action="store_true", help="Shows the average of all items in the list.")
parser.add_argument("-s", "--sum", action="store_true", help="Displays the sum of all items in the list.")
parser.add_argument("-t", action="store_true", help="Sort the list in ascending order.")
parser.add_argument("--desc", action="store_true", help="Sort the list in descending order.")
parser.add_argument("--help", action="store_true", help="Displays the user manual of this command.")
args = parser.parse_args()

# Program

try:

    if args.l:
        read_in_file()
        for nbr in listeVals:
            print(nbr)

    elif args.a:
        read_in_file()
        for val in args.a:
            if val.isdigit():
                listeVals.append(val)
                write_in_file(listeVals)
                print('Value', val, 'added')
            else:
                print('Please enter an integer')
                exit()

    elif args.c:
        suppr_all_items()

    elif args.max:
        read_in_file()
        rows = [int(row) for row in listeVals]
        highest = max_val(rows)
        print('The biggest value is', highest)

    elif args.min:
        read_in_file()
        rows = [int(row) for row in listeVals]
        lowest = min_val(rows)
        print('The smallest value is', lowest)

    elif args.moy:
        read_in_file()
        rows = [int(row) for row in listeVals]
        moy = (sum(rows) / len(listeVals))
        print('The average value is', moy)

    elif args.sum:
        read_in_file()
        rows = [int(row) for row in listeVals]
        total = sum(rows)
        print('The total sum is', total)

    elif args.t:
        read_in_file()
        rows = [int(row) for row in sorted(listeVals, key=int, reverse=False)]
        print('Sort in ascending order:', rows)

    elif args.desc:
        read_in_file()
        rows = [int(row) for row in sorted(listeVals, key=int, reverse=True)]
        print('Sort in descending order:', rows)

    else:
        parser.print_help()

except FileNotFoundError:
    create_file()
