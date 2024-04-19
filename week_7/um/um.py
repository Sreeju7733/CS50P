import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = re.findall("(^|\W)um($|\W)", s, re.IGNORECASE)
    return len(s)


if __name__ == "__main__":
    main()
