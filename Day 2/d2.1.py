import sys
from pathlib import Path

def get_position(input):
    depth = 0
    horizontal = 0 
    data = input.split()
    d = [(data[i], data[i+1]) for i in range(0, len(data), 2)]
    for x in d:
        num = eval(x[1])
        index = x[0]
        if index == 'forward':
            horizontal += num
        if index == 'up':
            depth -= num
        if index == 'down':
            depth += num
        
    print ('Horizontal distance:', horizontal)
    print ('Vertical depth:', depth)
    print('Multiplied:', horizontal * depth)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        get_position(Path.read_text(file))
    else:
        raise TypeError("This is not a file")