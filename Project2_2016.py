# real denotes part 2
max_x_coordinate = 2
min_x_coordinate = 0
max_y_coordinate = 2
min_y_coordinate = 0
code = []
real_code = []


def get_position_value(current_position):
    return current_position[0]*3 + current_position[1]+1


def get_real_position_value(current_position):
    if current_position[0] == 0:
        return 1
    if current_position[0] == 1:
        return 1 + current_position[1]
    if current_position[0] == 2:
        return 4 + current_position[1] + 1
    if current_position[0] == 3:
        if current_position[1] == 1:
            return 'A'
        if current_position[1] == 2:
            return 'B'
        else:
            return 'C'
    if current_position[0] == 4:
        return 'D'
    return


position = [1, 1]  # position[0] is the y coordinate
real_position = [2, 0]

moves = {
    'U': lambda coordinate, coordinate_limit = min_y_coordinate: [max(coordinate[0] - 1, coordinate_limit), coordinate[1]],
    'L': lambda coordinate, coordinate_limit = min_x_coordinate: [coordinate[0], max(coordinate_limit, coordinate[1] - 1)],
    'R': lambda coordinate, coordinate_limit = max_x_coordinate: [coordinate[0], min(coordinate[1] + 1, coordinate_limit)],
    'D': lambda coordinate, coordinate_limit = max_y_coordinate: [min(coordinate[0] + 1, coordinate_limit), coordinate[1]]
}


def get_real_move_limit(coordinate, next_instruction):
    max_y_limit = (coordinate[1]+1) % 3 + 1 + ((coordinate[1]+1)//3 * (3 - (2 * ((coordinate[1]+1) % 3))))
    min_y_limit = 2 - (max_y_limit - 2)
    max_x_limit = (coordinate[0]+1) % 3 + 1 + ((coordinate[0]+1)//3 * (3 - (2 * ((coordinate[0]+1) % 3))))
    min_x_limit = 2 - (max_x_limit - 2)
    if next_instruction == 'U':
        return min_y_limit
    if next_instruction == 'L':
        return min_x_limit
    if next_instruction == 'R':
        return max_x_limit
    if next_instruction == 'D':
        return max_y_limit


with open('Project2_2016') as file:
    for line in file:
        for instruction in line.rstrip('\n'):
            position = moves[instruction](position)
            real_position = moves[instruction](*[real_position, get_real_move_limit(real_position, instruction)])
        code.append(get_position_value(position))
        real_code.append(get_real_position_value(real_position))

print(code)
print(real_code)
