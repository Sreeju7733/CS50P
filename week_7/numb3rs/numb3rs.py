import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    splited_ip = ip.split(".")
    if re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip) and len(splited_ip) == 4:
        for ips in splited_ip:
            if not ips.isdigit():
                return False
            if not int(ips) < 0 and int(ips) > 255:
                return False
    else:
        return False

    return True

if __name__ == "__main__":
    main()
