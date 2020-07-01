from hashlib import md5
from itertools import count

project_input = 'cxdnnyjw'


def hash_solver(password, prefixes, results=1):
    numbers_to_add = count()
    results_found = 0
    for prefix in prefixes:
        for number_to_add in numbers_to_add:
            secret_code = password + str(number_to_add)
            hash_result = md5(secret_code.encode())
            hex_result = hash_result.hexdigest()
            if hex_result.startswith(prefix):
                results_found += 1
                yield number_to_add, hex_result
                if results_found == results:
                    break


password_length = 8
door_prefix = ['00000']
password_codes = hash_solver(project_input, door_prefix, password_length)
first_password = ''
for number, code in password_codes:
    first_password += code[5]
print(first_password)

second_password_codes = hash_solver(project_input, door_prefix, password_length ** 2)
second_password = [False, False, False, False, False, False, False, False]
for number, code in second_password_codes:
    password_index = code[5]
    if password_index.isnumeric():
        password_index = int(password_index)
        if password_index < 8:
            if not second_password[password_index]:
                second_password[password_index] = code[6]
    if False not in second_password:
        break
print(''.join(second_password))
