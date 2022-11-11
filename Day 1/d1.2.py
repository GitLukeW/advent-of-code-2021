import sys
from pathlib import Path

def add_ups(input):
    data = (input.split())
    nums = [eval(i) for i in data]
    group_sum = []
    window_size = 3
    for i in range(len(nums) - window_size + 1):
        group_sum.append(sum(nums[i: i + window_size]))
    return depth_increases(group_sum)
    

def depth_increases(group_sum):
    data = group_sum
    count = 0
    for i in range(1, len(data)):
        if(data[i] > data[i - 1]):
            count += 1
    print(count)
    


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        add_ups(Path.read_text(file))
    else:
        raise TypeError("This is not a file")
