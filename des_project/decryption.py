# decryption.py

# Import permutation function, XOR helper, and subkey generation routine
from key_schedule import apply_permutation, xor, generate_subkeys

# Import Feistel round function and DES initial/final permutation tables
from encryption import feistel_function, IP, FP


def des_decrypt_block_64(ciphertext_64, key_64):
    # Apply the Initial Permutation (IP) to the 64-bit ciphertext
    ciphertext_64_IP = apply_permutation(IP, ciphertext_64)

    # Split the permuted block into 32-bit left and right halves
    left_32, right_32 = ciphertext_64_IP[:32], ciphertext_64_IP[32:]

    # Generate all 16 subkeys and reverse the order for decryption
    sub16keys_48 = generate_subkeys(key_64)[::-1]

    # Perform the 16 DES Feistel rounds
    for i in range(16):
        # Left half for the next round is simply the previous right half
        new_left  = right_32
        
        # Right half becomes: previous left XOR Feistel(previous right, subkey_i)
        new_right = xor(left_32, feistel_function(right_32, sub16keys_48[i]))

        # Update left and right for the next iteration
        left_32, right_32 = new_left, new_right

    # After the final round, swap the halves (DES final swap)
    swapped_64 = right_32 + left_32

    # Apply the Final Permutation (FP) to get the decrypted 64-bit plaintext
    plaintext_64 = apply_permutation(FP, swapped_64)

    # Return the 64-bit plaintext block
    return plaintext_64

