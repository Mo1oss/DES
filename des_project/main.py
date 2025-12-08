# main.py

# Import DES encryption function
from encryption import des_encrypt_block_64
# Import DES decryption function
from decryption import des_decrypt_block_64


# Convert 16-hex-character string into 64-bit binary string
def hex16_to_bin64(hexa16):
    # Convert hex string → decimal
    decimal = int(hexa16, 16)
    # Convert decimal → 64-bit binary string
    bin64 = format(decimal, "064b")
    # Return binary result
    return bin64


# Convert 64-bit binary string back into 16-hex-character uppercase string
def bin64_to_hex16(bin64):
    # Convert binary → decimal → hex (16 characters)
    return format(int(bin64, 2), "016X")


# Run test only when script is executed directly
if __name__ == "__main__":
    # Test plaintext in hexadecimal (64 bits)
    plaintext_hex = "0123456789ABCDEF"
    # Test key in hexadecimal (64 bits)
    key_hex       = "133457799BBCDFF1"

    # Convert plaintext to 64-bit binary
    plaintext_bin = hex16_to_bin64(plaintext_hex)
    # Convert key to 64-bit binary
    key_bin       = hex16_to_bin64(key_hex)

    # Encrypt plaintext using DES
    ciphertext_bin = des_encrypt_block_64(plaintext_bin, key_bin)
    # Convert binary ciphertext → hexadecimal
    ciphertext_hex = bin64_to_hex16(ciphertext_bin)

    # Validate against known DES test vector
    assert ciphertext_hex == "85E813540F0AB405"

    # Decrypt ciphertext back to plaintext
    decrypted_bin = des_decrypt_block_64(ciphertext_bin, key_bin)
    # Convert decrypted binary → hexadecimal
    decrypted_hex = bin64_to_hex16(decrypted_bin)

    # Ensure decrypted text matches original plaintext
    assert decrypted_hex == plaintext_hex

    # Print results for verification
    print("Plaintext (hex): ", plaintext_hex)
    print("Key       (hex): ", key_hex)
    print("Cipher    (hex): ", ciphertext_hex)
    print("Decrypted (hex): ", decrypted_hex)
    # Indicate successful encryption/decryption
    print("✔ All DES tests passed successfully!")
