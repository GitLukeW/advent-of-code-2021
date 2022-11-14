import sys
from pathlib import Path

def get_position(input):
    depth = 0
    horizontal = 0 
    aim = 0
    data = input.split()
    d = [(data[i], data[i+1]) for i in range(0, len(data), 2)]
    for x in d:
        num = eval(x[1])
        index = x[0]
        if index == 'down':
            aim += num
        if index == 'up':
            aim -= num
        if index == 'forward':
            horizontal += num
            depth += (aim * num)
            
            
            
    
    print ('Horizontal distance:', horizontal)
    print ('Vertical depth:', depth)
    print('Aim:', aim)
    print('Multiplied:', horizontal * depth)
    


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        get_position(Path.read_text(file))
    else:
        raise TypeError("This is not a file")