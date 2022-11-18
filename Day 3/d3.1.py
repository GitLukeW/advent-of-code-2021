import sys
from pathlib import Path


def da_power(input):
    data = input.split()
    print(data)
    zeros = []
    ones = []

    for col in range(len(data[0])):
        for row in range(len(data)):
            print(data[row][col])
            
        



    

# [‘11010’, ‘11110’][0][0]
# ‘1’    


    

if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        da_power(Path.read_text(file))
    else:
        raise TypeError("This is not a file")