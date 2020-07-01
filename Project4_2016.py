name_and_sector_ids = {}

with open('Project4_2016') as file:
    for line in file:
        coded_name = line.rstrip('\n').split('-')
        sector_id, checksum = coded_name[-1].rstrip(']').split('[')
        checksum_calculated = {}
        encrypted_name = ''.join(coded_name[:-1])
        for char in encrypted_name:
            checksum_calculated[char] = encrypted_name.count(char)
        # Sort checksum_calcd dictionary
        sorted_checksum_calculated = sorted(checksum_calculated.items(), key=lambda item: (-item[1], item[0]))
        real_checksum = ''.join([x[0] for x in sorted_checksum_calculated[:5]])

        if real_checksum == checksum:
            name_and_sector_ids['-'.join(coded_name[:-1])] = (int(sector_id))


def decoder(coded_item, shift_amount):
    result = ''
    lower_case_alpha_start = 96

    for code in coded_item:
        if code == '-':
            letter_value = 32 - lower_case_alpha_start # chr() value for space
        else:
            letter_value = ord(code)-lower_case_alpha_start
            letter_value += shift_amount % 26
            if letter_value > 26:
                letter_value -= 26
        result += chr(lower_case_alpha_start + letter_value)

    return result


real_room_names = {}
for encoded_name, sector_id_value in name_and_sector_ids.items():
    real_name = decoder(encoded_name, sector_id_value)
    real_room_names[real_name] = sector_id_value
    if 'north' in real_name:
        print('The room {} has a sector id of: {}'.format(real_name, sector_id_value))
print(sum(name_and_sector_ids.values()))
