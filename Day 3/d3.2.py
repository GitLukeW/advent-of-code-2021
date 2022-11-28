import sys
from pathlib import Path


def total_function(input):
    data = input.split()
    oxygen = function_ones(data)
    co2 = function_zeros(data)

    oxygen = ''.join(map(str, oxygen)) 
    co2 = ''.join(map(str, co2)) 

    print("The Oxygen Generator Rating is", int(oxygen, 2))
    print("The CO2 Scrub Rating is", int(co2, 2))
    print("The Life Support Rating of the Submarine is", (int(oxygen, 2) * int(co2, 2)))



def function_ones(data):
    for col in range(len(data[0])):
        ones = []
        zeros = []
        for row in range(len(data)):
            if data[row][col] == "1":
                ones.append(data[row])
            else:
                zeros.append(data[row])
        if len(ones) >= len(zeros):
            data = ones
        if len(ones) < len(zeros):
            data = zeros
        if len(data) == 1:
            return(data)


def function_zeros(data):
    for col in range(len(data[0])):
        ones = []
        zeros = []
        for row in range(len(data)):
            if data[row][col] == "1":
                ones.append(data[row])
            else:
                zeros.append(data[row])
        if len(ones) >= len(zeros):
            data = zeros
        if len(ones) < len(zeros):
            data = ones
        if len(data) == 1:
            return(data)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        total_function(Path.read_text(file))
    else:
        raise TypeError("This is not a file")
