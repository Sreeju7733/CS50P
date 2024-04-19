def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    numofchar = ""
    numofnum = ""


    for chars in s:
        if chars.isalpha():
            numofchar += chars
        else:
            if chars == ".":
                return False
            else:
                numofnum += chars


    if numofnum != "":
        if (len(s) <= 6) and (len(numofchar) >= 2) and (numofnum[0] != "0") and (numofnum == s[len(numofchar):]):
                return True
        else:
            return False
    else:
        if (len(s) <= 6) and (len(numofchar) >= 2):
            return True
        else:
            return False



if __name__ == "__main__":
    main()
