decoy_message = ''
real_message = ''

with open('Project6_2016') as file:
    transposed_message = []
    for line in file:
        for index, char in enumerate(line.rstrip('\n')):
            if index > len(transposed_message)-1:
                transposed_message.append(char)
            else:
                transposed_message[index] += char

alphabet_start = 97
line_characterization = {}
for message in transposed_message:
    line_characterization.clear()
    for i in range(alphabet_start, alphabet_start+26):
        line_characterization[chr(i)] = message.count(chr(i))
    sorted_list = sorted(line_characterization.items(), key=lambda item: item[1])
    reversed_sorted_list = sorted(line_characterization.items(), key=lambda item: item[1], reverse=True)
    decoy_message += reversed_sorted_list[0][0]
    real_message += sorted_list[0][0]

print(decoy_message)
print(real_message)
