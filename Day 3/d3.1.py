import sys
from pathlib import Path

def da_power(input):
    data = input.split()
    one_list = []
    zero_list = []
    for i in range(0, len(data)):
        one_list.append(data[i][0]) == 1
    print(one_list)


    


    
    
    


       



if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        da_power(Path.read_text(file))
    else:
        raise TypeError("This is not a file")