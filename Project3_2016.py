possible_triangles = 0
sides_list = []


def triangle_tester(side_list):
    if sum(side_list[:-1]) > side_list[-1]:
        if sum(side_list[1:]) > side_list[0]:
            if sum(side_list[::2]) > side_list[1]:
                return True
    return False


with open('Project3_2016') as file:
    for line in file:
        sides = [int(x) for x in line.rstrip('\n').split()]
        if triangle_tester(sides):
            possible_triangles += 1
        sides_list.append(sides)

# Part 2
possible_triangles_columns = 0
for i in range(0, len(sides_list), 3):
    # 1st Column
    if triangle_tester([sides_list[i][0], sides_list[i+1][0], sides_list[i+2][0]]):
        possible_triangles_columns += 1
    # 2nd Column
    if triangle_tester([sides_list[i][1], sides_list[i+1][1], sides_list[i+2][1]]):
        possible_triangles_columns += 1
    # 3rd Column
    if triangle_tester([sides_list[i][2], sides_list[i+1][2], sides_list[i+2][2]]):
        possible_triangles_columns += 1

print(possible_triangles)
print(possible_triangles_columns)
