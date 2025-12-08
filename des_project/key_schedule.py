# key_schedule.py

# PC1 table: reduces 64-bit key → 56 bits by discarding parity bits
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

# PC2 table: reduces 56-bit key → 48-bit round subkey
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

# Rotation schedule: determines how many left shifts per round
SHIFTS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]


# Apply any permutation table to an input string of bits
def apply_permutation(permutation_table, input_bits):
    # Build the permuted output bit-by-bit
    reordered_bits = ""
    # For each index in the permutation table
    for index in permutation_table:
        # Append the corresponding bit (tables are 1-based indexing)
        reordered_bits += input_bits[index - 1]
    # Return permuted output
    return reordered_bits


# Circular left shift for a 28-bit key half
def shift_left(half_key28, shift_value):
    # Move bits left by shift_value with wrap-around
    return half_key28[shift_value:] + half_key28[:shift_value]


# XOR function for two equal-length bit strings
def xor(a, b):
    # Build result bit-by-bit
    result = ""
    for i in range(len(a)):
        # If bits are equal → 0; different → 1
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    # Return XOR output
    return result


# Generate the 16 DES round subkeys (each 48 bits)
def generate_subkeys(key_64):
    # Apply PC1 to get the 56-bit key
    key_56 = apply_permutation(PC1, key_64)
    # Split into two 28-bit halves
    C, D = key_56[:28], key_56[28:]
    # Prepare list to store all 16 subkeys
    sub16keys_48  = []
    # Apply round-by-round key shifts
    for shift in SHIFTS:
        # Rotate left half C
        C = shift_left(C, shift)
        # Rotate right half D
        D = shift_left(D, shift)
        # Combine halves again
        CD_56 = C + D
        # Apply PC2 to produce 48-bit subkey
        CD_48 = apply_permutation(PC2, CD_56)
        # Store this round's subkey
        sub16keys_48.append(CD_48)

    # Return list of 16 subkeys
    return sub16keys_48
