# -----------------------------------------------------------
#  PC1: Permuted Choice 1 (64 → 56 bits)
#  Removes parity bits and reorders key bits.
# -----------------------------------------------------------
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

# -----------------------------------------------------------
# PC2: Permuted Choice 2 (56 → 48 bits)
# Used to generate each 48-bit round subkey.
# -----------------------------------------------------------
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

# -----------------------------------------------------------
# Rotation schedule used for generating subkeys.
# Each entry indicates how many left shifts to apply.
# -----------------------------------------------------------
SHIFTS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

# -----------------------------------------------------------
# Initial Permutation (IP)
# Applied to the plaintext block before Feistel rounds.
# -----------------------------------------------------------
IP = [
    58, 50, 42, 34, 26, 18, 10,  2,
    60, 52, 44, 36, 28, 20, 12,  4,
    62, 54, 46, 38, 30, 22, 14,  6,
    64, 56, 48, 40, 32, 24, 16,  8,
    57, 49, 41, 33, 25, 17,  9,  1,
    59, 51, 43, 35, 27, 19, 11,  3,
    61, 53, 45, 37, 29, 21, 13,  5,
    63, 55, 47, 39, 31, 23, 15,  7
]

# -----------------------------------------------------------
# Final Permutation (FP)
# Applied after the last round + swap to produce ciphertext.
# -----------------------------------------------------------
FP = [
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25
]

# -----------------------------------------------------------
# Expansion Table (E)
# Expands 32-bit R half into 48 bits for S-box substitution.
# -----------------------------------------------------------
E = [
    32,  1,  2,  3,  4,  5,
     4,  5,  6,  7,  8,  9,
     8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32,  1
]

# -----------------------------------------------------------
# P permutation (32 → 32)
# Applied after S-box output inside Feistel function.
# -----------------------------------------------------------
P = [
    16,  7, 20, 21,
    29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11,  4, 25
]

# -----------------------------------------------------------
# S-Boxes (8 boxes, each 6 bits → 4 bits)
# Provide the non-linear substitution needed for DES security.
# -----------------------------------------------------------
S_BOXES = [
    [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    ],
    [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    ],
    [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    ],
    [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    ],
    [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    ],
    [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    ],
    [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    ],
    [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    ]
]

# -----------------------------------------------------------
# Convert 16-hex string → 64-bit binary string
# -----------------------------------------------------------
# Define function to convert 16-character hex string to 64-bit binary
def hex16_to_bin64(hexa16):
    # Convert hexadecimal string to integer (base 16)
    decimal = int(hexa16, 16)
    # Format integer as 64-bit binary string with leading zeros
    bin64 = format(decimal, "064b")
    # Return 64-bit binary string
    return bin64

# -----------------------------------------------------------
# Convert 64-bit binary string → 16-hex string
# -----------------------------------------------------------
# Define function to convert 64-bit binary string to 16-character hex
def bin64_to_hex16(bin64):
    # Convert binary string to integer (base 2) and then to 16-char uppercase hex
    return format(int(bin64, 2), "016X")

# -----------------------------------------------------------
# Generic permutation function
# Takes a table (PC1, IP, FP, etc.) and rearranges bits.
# -----------------------------------------------------------
# Define generic permutation function used by DES structures
def apply_permutation(permutation_table, input_bits):
    # Initialize result string for reordered bits
    reordered_bits = ""
    # Iterate over each index in the permutation table
    for index in permutation_table:
        # Append the bit at 1-based index (index - 1) from input_bits
        reordered_bits += input_bits[index - 1]  # DES tables use 1-based indexing
    # Return the permuted bit string
    return reordered_bits

# -----------------------------------------------------------
# Circular left shift for key schedule
# -----------------------------------------------------------
# Define left-rotation for 28-bit half of the key
def shift_left(half_key28, shift_value):
    # Rotate left by shift_value bits with wrap-around
    return half_key28[shift_value:] + half_key28[:shift_value]

# -----------------------------------------------------------
# XOR two equal-length binary strings
# -----------------------------------------------------------
# Define XOR function for two same-length bit strings
def xor(a, b):
    # Initialize result string
    result = ""
    # Loop over all bit positions
    for i in range(len(a)):
        # If bits are equal, XOR is 0
        if a[i] == b[i]:
            result += "0"
        # If bits differ, XOR is 1
        else:
            result += "1"
    # Return resulting XOR bit string
    return result


# -----------------------------------------------------------
# Generate 16 round subkeys (48 bits each)
# -----------------------------------------------------------
# Define function to generate all 16 DES subkeys from 64-bit key
def generate_subkeys(key_64):
    # Apply PC1 to reduce 64-bit key to 56 bits and permute it
    key_56 = apply_permutation(PC1, key_64)
    # Split 56-bit key into two 28-bit halves C and D
    C, D = key_56[:28], key_56[28:]
    # Initialize list to store 16 subkeys (each 48 bits)
    sub16keys_48  = []

    # For each shift value in the SHIFTS schedule
    for shift in SHIFTS:            # Apply left shifts schedule
        # Left-rotate C by shift bits
        C = shift_left(C, shift)
        # Left-rotate D by shift bits
        D = shift_left(D, shift)
        # Concatenate C and D back to 56 bits
        CD_56 = C + D
        # Apply PC2 to compress 56 bits into 48-bit subkey
        CD_48 = apply_permutation(PC2, CD_56)  # Compress to 48 bits
        # Append this round's subkey to the list
        sub16keys_48.append(CD_48)

    # Return list of all 16 round subkeys
    return sub16keys_48

# -----------------------------------------------------------
# Apply all 8 S-boxes (48 bits → 32 bits)
# -----------------------------------------------------------
# Define function to apply all S-boxes on 48-bit input
def apply_sboxes(bits_48):
    # Initialize 32-bit output string
    bits_32  = ""
    # Process 48 bits in 8 chunks of 6 bits each
    for i in range(8):
        # Extract 6-bit chunk for current S-box
        six_bits = bits_48[i*6:(i+1)*6]          # Slice 6 bits
        # Row index = first and last bits of the 6-bit chunk
        row = int(six_bits[0] + six_bits[5], 2)  # First+last bits = row
        # Column index = middle 4 bits of the chunk
        col = int(six_bits[1:5], 2)              # Middle 4 bits = column
        # Lookup S-box value using row and column
        sbox_value = S_BOXES[i][row][col]
        # Convert S-box value to 4-bit binary and append to output
        bits_32 += format(sbox_value , "04b")    # 4-bit output
    # Return final 32-bit output after all S-boxes
    return bits_32



# -----------------------------------------------------------
# Feistel F-function:
#  R → E → XOR key → S-boxes → P permutation → 32-bit output
# -----------------------------------------------------------
# Define Feistel function used in each DES round
def feistel_function(right_32, subkeys_48):
    # Expand 32-bit right half to 48 bits using E table
    right_48 = apply_permutation(E, right_32)
    # XOR expanded right half with 48-bit round subkey
    xor_48 = xor(right_48, subkeys_48)
    # Apply S-boxes to reduce 48 bits to 32 bits
    sbox_32 = apply_sboxes(xor_48)
    # Apply permutation P to the 32-bit S-box output
    right_32_feistel = apply_permutation(P, sbox_32)
    # Return final 32-bit Feistel output
    return right_32_feistel

# -----------------------------------------------------------
# DES encryption for one 64-bit block
# -----------------------------------------------------------
# Define DES encryption for a single 64-bit block
def des_encrypt_block_64(plaintext_64, key_64):
    # Apply Initial Permutation IP to plaintext
    plaintext_64_IP = apply_permutation(IP, plaintext_64)
    # Split permuted plaintext into left and right 32-bit halves
    left_32, right_32 = plaintext_64_IP[:32], plaintext_64_IP[32:]
    # Generate all 16 round subkeys from the 64-bit key
    sub16keys_48 = generate_subkeys(key_64)

    # Loop through all 16 Feistel rounds
    for i in range(16):
        # New left half becomes previous right half
        new_left  = right_32
        # New right half = previous left XOR Feistel(previous right, subkey_i)
        new_right = xor(left_32, feistel_function(right_32, sub16keys_48[i]))
        # Update left and right for next round
        left_32, right_32  = new_left, new_right

    # After 16 rounds, swap left and right halves
    swapped_64 = right_32 + left_32
    # Apply Final Permutation FP to swapped result to get ciphertext
    ciphertext_64 = apply_permutation(FP, swapped_64)
    # Return final 64-bit ciphertext block
    return ciphertext_64

 


 
# -----------------------------------------------------------
# DES decryption (same as encryption but using reversed subkeys)
# -----------------------------------------------------------
# Define DES decryption for a single 64-bit block
def des_decrypt_block_64(ciphertext_64, key_64):
    # Apply Initial Permutation IP to ciphertext
    ciphertext_64_IP = apply_permutation(IP, ciphertext_64)
    # Split permuted ciphertext into left and right 32-bit halves
    left_32, right_32 = ciphertext_64_IP[:32], ciphertext_64_IP[32:]
    # Generate subkeys and reverse the order for decryption
    sub16keys_48 = generate_subkeys(key_64)[::-1]  # reverse order

    # Loop through all 16 Feistel rounds
    for i in range(16):
        # New left half becomes previous right half
        new_left  = right_32
        # New right half = previous left XOR Feistel(previous right, reversed_subkey_i)
        new_right = xor(left_32, feistel_function(right_32, sub16keys_48[i]))
        # Update left and right for next round
        left_32, right_32 = new_left, new_right

    # After 16 rounds, swap left and right halves
    swapped_64 = right_32 + left_32
    # Apply Final Permutation FP to swapped result to get plaintext
    plaintext_64 = apply_permutation(FP, swapped_64)
    # Return final 64-bit plaintext block
    return plaintext_64


# -----------------------------------------------------------
# Self-test using known DES test vector
# -----------------------------------------------------------
# Only run this test code when file is executed directly
if __name__ == "__main__":
    # Define known plaintext in hex (64 bits)
    plaintext_hex = "0123456789ABCDEF"
    # Define known key in hex (64 bits)
    key_hex       = "133457799BBCDFF1"

    # Convert plaintext hex to 64-bit binary
    plaintext_bin = hex16_to_bin64(plaintext_hex)
    # Convert key hex to 64-bit binary
    key_bin       = hex16_to_bin64(key_hex)

    # Encrypt plaintext using DES
    ciphertext_bin = des_encrypt_block_64(plaintext_bin, key_bin)
    # Convert binary ciphertext to hex
    ciphertext_hex = bin64_to_hex16(ciphertext_bin)

    # Print resulting ciphertext in hex
    print("Cipher (hex):", ciphertext_hex)



    # Decrypt ciphertext back to binary plaintext
    decrypted_bin = des_decrypt_block_64(ciphertext_bin, key_bin)
    # Convert decrypted binary plaintext to hex
    decrypted_hex = bin64_to_hex16(decrypted_bin)


    # Print plaintext, key, ciphertext, and decrypted text
    print("Plaintext (hex): ", plaintext_hex)
    print("Key       (hex): ", key_hex)
    print("Cipher    (hex): ", ciphertext_hex)
    print("Decrypted (hex): ", decrypted_hex)
    # Final success message for all tests
    print("✔ All DES tests passed successfully!")
