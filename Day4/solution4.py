input_text = []

with open('input.txt', 'r') as file:
    rownum = 0

    for line in file.readlines():
        row = []
        for char in line:
            if char != '\n':
                row.append(char.upper())

        input_text.append(row)
        rownum += 1

directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1))


def search(word, coords, input, direction):
    char = word[0]
    new_coords = [coords[0]+direction[0], coords[1]+direction[1]]

    if char == word:
        if char == input[coords[0]][coords[1]]:
            return 1
        else:
            return 0
    elif new_coords[0] < 0 or new_coords[0] >= len(input) or new_coords[1] < 0 or new_coords[1] >= len(input[1]):
        return 0
    elif char == input[coords[0]][coords[1]]:
        new_word = word[1:]
        return search(new_word, new_coords, input, direction)

    else:
        return 0


def search_mas(in_search, coords, input):
    bw_in_search = in_search[::-1]
    search_coords = ((-1, -1), (-1, 1), (1, -1), (1, 1))

    for x_coords in search_coords:
        if (coords[0] + x_coords[0]) < 0 or (coords[0] + x_coords[0]) >= len(input) or (coords[1] + x_coords[1]) < 0 or (coords[1] + x_coords[1]) >= len(input[1]):
            return 0

    diag_1 = [
        [coords[0]+search_coords[0][0], coords[1]+search_coords[0][1]],
        [coords[0]+search_coords[3][0], coords[1]+search_coords[3][1]]
    ]

    diag_2 = [
        [coords[0]+search_coords[1][0], coords[1]+search_coords[1][1]],
        [coords[0]+search_coords[2][0], coords[1]+search_coords[2][1]]
    ]

    cross1 = input[diag_1[0][0]][diag_1[0][1]] + input[coords[0]
                                                       ][coords[1]] + input[diag_1[1][0]][diag_1[1][1]]

    cross2 = input[diag_2[0][0]][diag_2[0][1]] + input[coords[0]
                                                       ][coords[1]] + input[diag_2[1][0]][diag_2[1][1]]
    if (cross1 == in_search or cross1 == bw_in_search) and (cross2 == in_search or cross2 == bw_in_search):
        return 1
    else:
        return 0


matches = 0

for x in range(len(input_text)):
    for y in range(len(input_text[x])):
        if input_text[x][y] == 'X':
            for xd, yd in directions:
                search_coords = [x+xd, y+yd]

                matches += search('MAS', search_coords,
                                  input_text, [xd, yd])

x_mases = 0

for x in range(len(input_text)):
    for y in range(len(input_text[x])):
        if input_text[x][y] == 'A':
            x_mases += search_mas('MAS', [x, y], input_text)


print(matches)
print(x_mases)
