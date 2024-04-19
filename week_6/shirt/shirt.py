import sys
import os.path
from PIL import Image, ImageOps

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")

    input_file, output_file = args

    if not (input_file.lower().endswith(('.jpg', '.jpeg', '.png')) and output_file.lower().endswith(('.jpg', '.jpeg', '.png'))):
        sys.exit("Invalid output")
    elif os.path.splitext(input_file)[1].lower() != os.path.splitext(output_file)[1].lower():
        sys.exit("Input and output have different extensions")
    elif not os.path.exists(input_file):
        sys.exit("Input does not exist")

    process_img(input_file, output_file)


def process_img(input_file, output_file):
    try:
        with Image.open("shirt.png") as shirt, Image.open(input_file) as input_img:
            input_cropped = ImageOps.fit(input_img, shirt.size)
            input_cropped.paste(shirt, (0,0), mask=shirt)
            input_cropped.save(output_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
