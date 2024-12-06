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
            print(direction)
            print('XMAS!!!')
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
    pass


matches = 0

for x in range(len(input_text)):
    for y in range(len(input_text[x])):
        if input_text[x][y] == 'X':
            for xd, yd in directions:
                search_coords = [x+xd, y+yd]

                matches += search('MAS', search_coords,
                                  input_text, [xd, yd])


x_mases = -

for x in range(len(input_text)):
    for y in range(len(input_text[x])):
        if input_text[x][y] == 'X':
            for xd, yd in directions:
                search_coords = [x+xd, y+yd]

                matches += search('MAS', search_coords,
                                  input_text, [xd, yd])


print(input_text)
print(matches)
