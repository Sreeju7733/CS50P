import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        print(open_file(sys.argv[1]))

def open_file(filename):
    try:
        lines = 0
        with open(filename) as file:
            for line in file:
                if not line.lstrip().startswith("#") and line.strip() != "":
                    lines += 1
            return lines
    except FileNotFoundError:
        return "File does not exist"

if __name__ == "__main__":
    main()
