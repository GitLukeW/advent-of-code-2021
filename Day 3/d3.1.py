import sys
from pathlib import Path


def da_power(input):
    data = input.split()
    zeros = len(data[0])
    ones = [0] * len(data[0])
    print(data)
    for i in data:
        if i == 0:
            zeros.append[i] += 1

    print(zeros)

    


    


    
    
    


       



if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        da_power(Path.read_text(file))
    else:
        raise TypeError("This is not a file")