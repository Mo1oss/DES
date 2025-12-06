# key_schedule.py

PC1 = [
    57,49,41,33,25,17,9,
     1,58,50,42,34,26,18,
    10, 2,59,51,43,35,27,
    19,11, 3,60,52,44,36,
    63,55,47,39,31,23,15,
     7,62,54,46,38,30,22,
    14, 6,61,53,45,37,29,
    21,13, 5,28,20,12, 4
]

PC2 = [
    14,17,11,24, 1, 5,
     3,28,15, 6,21,10,
    23,19,12, 4,26, 8,
    16, 7,27,20,13, 2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

SHIFTS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]


def apply_permutation(permutation_table, input_bits):
    reordered_bits = ""
    for index in permutation_table:
        reordered_bits += input_bits[index - 1]
    return reordered_bits


def shift_left(half_key28, shift_value):
    return half_key28[shift_value:] + half_key28[:shift_value]


def xor(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result


def generate_subkeys(key_64):
    key_56 = apply_permutation(PC1, key_64)
    C, D = key_56[:28], key_56[28:]
    sub16keys_48  = []
    for shift in SHIFTS:
        C = shift_left(C, shift)
        D = shift_left(D, shift)
        CD_56 = C + D
        CD_48 = apply_permutation(PC2, CD_56)
        sub16keys_48.append(CD_48)

    return sub16keys_48
