import sys
import os
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        print("Usage: python pizza.py <csv_file>")
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        sys.exit(1)

    if not filename.endswith('.csv'):
        print("Invalid file format. Please specify a .csv file.")
        sys.exit(1)

    table = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            table.append(row)

    print(tabulate(table, headers="keys"))

if __name__ == "__main__":
    main()
