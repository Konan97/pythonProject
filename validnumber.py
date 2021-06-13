# given a string s, return true if s is a valid number.

# convert all the number to a float
# ex: valid numbers: ["2", "0089", "-0.1", "+3.14", "-90E3"]
# digits, plus, minus, dot, letters
input = "-90E3"


def validnumber():
    digit, plus, minus, dot, letters = True, True, True, True, True
    numbers = list(input)

    if "+" in numbers:
        if numbers[0] == "+":
            plus = True
            minus = False
        else:
            plus = False

    if "-" in numbers:
        if numbers[0] == "-":
            minus = True
            plus = False
        else:
            minus = False


    # find e or E
    count = 0
    for num in numbers:
        if "e" or "E" in numbers:
            count += 1

    if count > 1:
        letters = False

    # find dot
    countdot = 0
    for num in numbers:
        if "." in numbers:
            countdot += 1

    if countdot > 1:
        dot = False

    if minus is True and plus is True:
        print("false")
        return False
    else:
        if digit is True and dot is True and letters is True:
            print("true")
            return True



