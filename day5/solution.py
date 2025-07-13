file = 'input.txt'

instructions = []
ins_dict = {}

already_sorted = []

to_sort = []
all_sorted = []

with open(file, 'r') as data:
    for line in data:
        if '|' in line:
            instructions.append(line.strip().split('|'))
        elif ',' in line:
            to_sort.append(line.strip().split(','))
        else:
            continue

for key, val in instructions:
    ins_dict.setdefault(key, []).append(val)


def sort_list_by_rules(group: list) -> list:
    sorted = group
    for element in sorted:
        if element in ins_dict.keys():
            index = sorted.index(element)
            for item in ins_dict[element]:
                if item in sorted:
                    if sorted.index(element) > sorted.index(item) and index > sorted.index(item):
                        index = sorted.index(item)

            sorted.insert(index, sorted.pop(sorted.index(element)))
    return sorted


def sum_centers(sorteddata: list[list]) -> int:
    centers = []
    for group in sorteddata:
        centers.append(int(group[round((len(group)-1)/2)]))
    return sum(centers)


for element in to_sort:
    sorted_list = element.copy()
    sorted_list = sort_list_by_rules(sorted_list)

    same = True
    for key, value in list(zip(element, sorted_list)):
        if key != value:
            same = False

    if same is True:
        already_sorted.append(element)
    else:
        all_sorted.append(sorted_list)


solution1 = sum_centers(already_sorted)
solution2 = sum_centers(all_sorted)

print('The sum of all middle page numbers is: ' + str(solution1))
print('The sum of all sorted middle page numbers is: ' + str(solution2))
