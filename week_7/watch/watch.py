import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r'<iframe\s+src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)"\s*></iframe>', s)
    if matches:
        matches = matches.group(1)
        return f"https://youtu.be/{matches}"
    else:
        return None


if __name__ == "__main__":
    main()
