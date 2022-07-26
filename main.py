import random


def get_initial_pencils(msg="How many pencils would you like to use:\n"):
    pencils = input(msg)
    if not pencils.isnumeric():
        return get_initial_pencils("The number of pencils should be numeric\n")
    elif int(pencils) <= 0:
        return get_initial_pencils("The number of pencils should be positive\n")
    else:
        return int(pencils)


def get_first_turn(msg="Who will be the first (John, Jack):\n"):
    turn = input(msg)
    if turn in ("John", "Jack"):
        return turn
    return get_first_turn("Choose between 'John' and 'Jack'\n")


def player_turn(pencils, msg="John's turn:\n"):
    number = input(msg)
    if not number.isnumeric() or not 1 <= int(number) <= 3:
        return player_turn(pencils, "Possible values: '1', '2' or '3'\n")
    elif pencils - int(number) < 0:
        return player_turn(pencils, "Too many pencils were taken\n")
    else:
        return int(number)


def bot_turn(pencils):
    if pencils % 4 == 1:
        number = random.randrange(1, pencils + 1 if pencils <= 3 else 4)
    elif pencils % 4 in (2, 3):
        number = pencils % 4 - 1
    else:
        number = 3
    print("Jack's turn:", number, sep="\n")
    return number


def main(pencils, turn):
    print("|" * pencils)
    pencils -= bot_turn(pencils) if turn == "Jack" else player_turn(pencils)
    turn = "John" if turn == "Jack" else "Jack"
    if pencils == 0:
        return print(turn, "won!")
    return main(pencils, turn)


if __name__ == "__main__":
    main(get_initial_pencils(), get_first_turn())
