import re


test_data = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
test_data_2 = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'


def file_reader(path):
    with open(path, 'r') as file:
        data = file.read()
    return data


def part1(input):
    sumproducts = 0
    mul_list = re.findall(r'mul\(\d{1,3},\d{1,3}\)', input)

    for mul in mul_list:
        stripped = mul.lstrip('mul(').rstrip(')').split(',')
        sumproducts += int(stripped[0])*int(stripped[1])

    return sumproducts


def part2(input):
    sumproducts = 0
    do = True

    mul_list = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', input)

    for item in mul_list:
        if item == 'do()':
            do = True
        elif item == 'don\'t()':
            do = False
        elif do == True:
            stripped = item.lstrip('mul(').rstrip(')').split(',')
            sumproducts += int(stripped[0])*int(stripped[1])

    return sumproducts


data = file_reader('input.txt')

print(part1(data))
print(part2(data))
