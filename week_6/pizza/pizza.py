import sys
from csv import reader
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        print(open_file(sys.argv[1]))



def open_file(filename):
    try:
        with open(filename) as file:
            table = reader(file)

            return tabulate(table, headers="firstrow", tablefmt="grid")

    except FileNotFoundError:
        return sys.exit("File does not exist")



if __name__ == "__main__":
    main()
