import sys
from pathlib import Path


def bingo(input):
    data = input.split()
    first_line = data[0]
    print(first_line)
    bingo_cards = data
    print(bingo_cards)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        bingo(Path.read_text(file))
    else:
        raise TypeError("This is not a file")