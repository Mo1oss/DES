# decryption.py

from key_schedule import apply_permutation, xor, generate_subkeys
from encryption import feistel_function, IP, FP


def des_decrypt_block_64(ciphertext_64, key_64):
    ciphertext_64_IP = apply_permutation(IP, ciphertext_64)
    left_32, right_32 = ciphertext_64_IP[:32], ciphertext_64_IP[32:]
    sub16keys_48 = generate_subkeys(key_64)[::-1]

    for i in range(16):
        new_left  = right_32
        new_right = xor(left_32, feistel_function(right_32, sub16keys_48[i]))
        left_32, right_32 = new_left, new_right

    swapped_64 = right_32 + left_32
    plaintext_64 = apply_permutation(FP, swapped_64)

    return plaintext_64
