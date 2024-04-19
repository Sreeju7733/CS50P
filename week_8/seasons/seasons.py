from datetime import date
import inflect
import sys
import operator

p = inflect.engine()


def main():
    try:
        user_input = input("Date of Birth: ")
        difference = operator.sub(date.today(), date.fromisoformat(user_input))
        print(f"{(p.number_to_words(convert(difference.days), andword='')).capitalize()} minutes")
    except ValueError:
        sys.exit("Invalid date")


def convert(time):
    minutes = time * 24 * 60
    return minutes


if __name__ == "__main__":
    main()
