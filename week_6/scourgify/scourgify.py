import csv
import sys


def main():
    if len(sys.argv) != 3:
        print("Too few command-line arguments")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    file_list = open_file(input_filename)
    if not file_list:
        print(f"Could not read {input_filename}")
        sys.exit(1)

    create_file(output_filename, file_list)


def open_file(filename):
    lists = []
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                lname, fname = row["name"].strip().split(",")
                lists.append({"first": fname, "last": lname, "house": row["house"]})
    except FileNotFoundError:
        return None
    return lists



def create_file(filename, file_list):
    with open(filename, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for items in file_list:
            items['first'] = items['first'].strip()
            writer.writerow(items)


if __name__ == "__main__":
    main()
