import sys
from pathlib import Path


def da_power(input):
    data = input.split()

    gamma = ""
    epsilon = ""

    for col in range(len(data[0])):
        ones = 0
        zeros = 0
        for row in range(len(data)):
            if data[row][col] == "1":
                ones += 1
            else:
                zeros += 1
        if ones < zeros:
            epsilon += "1"
            gamma += "0"
        else: 
            epsilon += "0"
            gamma += "1"

    print(int(gamma))
    print(int(epsilon))
    print(int(gamma, 2) * int(epsilon, 2))


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        da_power(Path.read_text(file))
    else:
        raise TypeError("This is not a file")