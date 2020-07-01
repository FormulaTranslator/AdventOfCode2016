from re import split


def abba_detector(string_var):
    for index, char in enumerate(string_var[:-3]):
        if string_var[index+3] == char and string_var[index+1] == string_var[index+2] != char:
            return True
    return False


def aba_bab_detector(string_var, aba_result):
    result_set = set()
    for index, char in enumerate(string_var[:-2]):
        if string_var[index+2] == char != string_var[index+1]:
            if aba_result:
                result_set.add(string_var[index:index+3])
            else:  # Converts the string into ABA notation
                result_set.add(string_var[index+1]+string_var[index]+string_var[index+1])
    return result_set


IP_TLS_count = 0
IP_SSL_count = 0
with open('Project7_2016') as file:
    for i, line in enumerate(file):
        fragments = split('\[|\]', line)
        supernet_sequences = ' '.join(fragments[::2])
        hypernet_sequences = ' '.join(fragments[1::2])
        supports_TLS = False
        TLS_error = False
        aba_set = set()
        bab_aba_set = set()
        # ABBA Detection
        if abba_detector(hypernet_sequences):
            TLS_error = True
            supports_TLS = False
        if abba_detector(supernet_sequences) and not TLS_error:
            supports_TLS = True
        # ABA/BAB Detection
        bab_result = aba_bab_detector(hypernet_sequences, False)
        aba_result = aba_bab_detector(supernet_sequences, True)
        if bab_result:
            bab_aba_set.update(bab_result)

        if aba_result:
            aba_set.update(aba_result)
        if supports_TLS:
            IP_TLS_count += 1

        total_set = aba_set.union(bab_aba_set)
        if total_set:
            if len(total_set) < len(aba_set) + len(bab_aba_set):
                IP_SSL_count += 1

print(IP_TLS_count)
print(IP_SSL_count)


# Reddit Answer
def abba(x):
    return any(a == d and b == c and a != b for a, b, c, d in zip(x, x[1:], x[2:], x[3:]))


lines = [split(r'\[([^\]]+)\]', line) for line in open('Project7_2016')]
parts = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in lines]
print('Answer #1:', sum(abba(sn) and not(abba(hn)) for sn, hn in parts))
print('Answer #2:', sum(any(a == c and a != b and b+a+b in hn for a, b, c in zip(sn, sn[1:], sn[2:])) for sn, hn in parts))