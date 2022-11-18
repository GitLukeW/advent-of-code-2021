import sys
from pathlib import Path


def da_power(input):
    data = input.split()
    print(data)

    for col in range(len(data[0])):
        ones = []
        zeros = []
        for row in range(len(data)):
            if data[row][col] == '1':
                ones.append(1)
            if data[row][col] == '0':
                zeros.append(0)
        print(ones)
        print(zeros)
    
            

    

# [‘11010’, ‘11110’][0][0]
# ‘1’    

#   print(data[row][col])
    

if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        da_power(Path.read_text(file))
    else:
        raise TypeError("This is not a file")