import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = r"(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM) to (0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.match(regex, s)

    if match:
        from_hour, from_minute, from_period, to_hour, to_minute, to_period = match.groups()

        def format(hour, minute, period):
            if period == "AM":
                if hour == "12":
                    hour = "00"
                else:
                    hour = f"{int(hour):02}"
            else:
                if hour != "12":
                    hour = f"{int(hour) + 12:02}"

            minute = "00" if minute is None else f"{int(minute):02}"
            return f"{hour}:{minute}"


        from_time = format(from_hour, from_minute, from_period)
        to_time = format(to_hour, to_minute, to_period)

        return f"{from_time} to {to_time}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
