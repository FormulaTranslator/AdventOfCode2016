with open('Project1_2016') as file:
    directions = file.readline().split(', ')


def change_orientation(current_orientation, move_direction):
    """This function sets the orientation to a value between 1 and 4"""
    result = current_orientation + move_direction
    if result < 1:
        result = 4
    elif result > 4:
        result = 1
    return result


def add_coordinates(coordinates, next_move, current_orientation):
    result = coordinates
    start_position = result[-1].copy()
    x_move = ((current_orientation % 2) - 1) * (current_orientation - 3)
    y_move = (current_orientation % 2) * (2 - current_orientation)
    duplicate_found = False
    duplicate_coordinate = None
    for i in range(1, next_move+1):
        next_coordinate = [start_position[0] + y_move*i, start_position[1] + x_move*i]
        if next_coordinate in result and not duplicate_found:
            duplicate_found = True
            duplicate_coordinate = next_coordinate.copy()
        result.append(next_coordinate)
    return duplicate_found, duplicate_coordinate


position = [0, 0]
coordinate_tracker = [[0, 0]]
HQ_found = False
orientation = 1  # 1 is north, 2 is east, 3 is south, 4 is west
for direction in directions:
    # Get the new orientation after turning
    if 'R' in direction:
        orientation = change_orientation(orientation, 1)
    else:
        orientation = change_orientation(orientation, -1)
    # Travel the required blocks in the new direction
    match_found, match_position = add_coordinates(coordinate_tracker, int(direction[1:]), orientation)
    if not HQ_found and match_found:
        HQ = match_position.copy()
        HQ_found = True
    # Determine if road has been crossed before


print(sum(abs(x) for x in coordinate_tracker[-1]))
print(sum(abs(x) for x in HQ))
